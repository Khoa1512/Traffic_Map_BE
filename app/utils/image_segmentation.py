import numpy as np
import cv2
import tensorflow as tf
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class image_Segmentation:
    _instance = None
    _model = None

    def __new__(cls, image_path=None, preprocess_func=None):
        if cls._instance is None:
            cls._instance = super(image_Segmentation, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, image_path=None, preprocess_func=None):
        if not self._initialized:
            self._load_model()
            self._initialized = True

        self.preprocess_func = preprocess_func
        self.image_path = image_path

    def _load_model(self):
        """Load model từ file"""
        try:
            model_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                'app',
                'models',
                'ml',
                'unet_backbone_resnet34_100epochs_28Dec2024.hdf5'
            )

            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"Model file not found at: {model_path}")

            logger.info(f"Loading model from {model_path}")
            self._model = tf.keras.models.load_model(model_path, compile=False)
            logger.info("Model loaded successfully")

        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise

    def set_image(self, image_path):
        """Set đường dẫn ảnh mới"""
        self.image_path = image_path

    def process_image(self):
        """Xử lý ảnh đầu vào"""
        if not self.image_path:
            raise ValueError("Image path not set")

        test_img = cv2.imread(self.image_path)
        test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
        original_size = test_img.shape[:2]

        if self.preprocess_func:
            test_img_input = self.preprocess_func(test_img)
        else:
            test_img_resized = cv2.resize(test_img, (256, 256))
            test_img_input = test_img_resized / 255.0
            test_img_input = np.expand_dims(test_img_input, axis=0)

        return test_img, test_img_input, original_size

    def predict_mask(self):
        """Dự đoán mask từ ảnh"""
        if not self._model:
            raise RuntimeError("Model not loaded")

        test_img, test_img_input, original_size = self.process_image()

        prediction = self._model.predict(test_img_input, verbose=0)
        predicted_img = np.argmax(prediction, axis=3)[0, :, :]
        predicted_img_resized = cv2.resize(
            predicted_img.astype(np.uint8), original_size[::-1])

        return test_img, predicted_img_resized, predicted_img

    def traffic_volume(self):
        """Tính traffic volume từ predicted mask"""
        try:
            mask = self.predict_mask()[2]
            area_a = np.sum(mask == 0)
            area_b = np.sum(mask == 1)

            if area_a == 0 or area_b == 0:
                logger.warning(
                    f"Invalid areas detected for image {self.image_path}")
                return 0

            ratio = area_a / area_b
            return ratio

        except Exception as e:
            logger.error(f"Error calculating traffic volume: {e}")
            return 0
