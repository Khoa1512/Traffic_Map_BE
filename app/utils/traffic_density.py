# app/utils/traffic_density.py
import os
import logging
from datetime import datetime
from .image_segmentation import image_Segmentation
from ..models.camera import cameras

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TrafficDensityService:
    def __init__(self):
        self.captures_dir = os.path.join('app', 'data', 'captures')
        self.segmentation = image_Segmentation()

    def calculate(self):
        """Tính toán traffic density từ ảnh trong folder captures"""
        try:
            traffic_values = {}
            maxvolume = 1.8040083740908515

            # Tính traffic value cho mỗi camera
            for filename in os.listdir(self.captures_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        image_path = os.path.join(self.captures_dir, filename)
                        # Lấy camera ID từ tên file
                        camera_id = filename.split('_')[0]

                        # traffic_value = self.segmentation.traffic_volume(
                        #     image_path)
                        # Thiết lập đường dẫn ảnh
                        self.segmentation.set_image(image_path)
                        traffic_value = self.segmentation.traffic_volume()

                        traffic_values[camera_id] = traffic_value
                        # logger.info(
                        #     f"Calculated traffic value for camera {camera_id}: {traffic_value}")
                    except Exception as e:
                        logger.error(f"Error processing image {filename}: {e}")


            if maxvolume > 0:
                for camera_id, value in traffic_values.items():
                    if camera_id in cameras:
                        density_percentage = (value / maxvolume) * 100
                        camera = cameras[camera_id]  # Lấy camera object
                        camera.traffic_density = round(density_percentage, 2)
                        camera.last_update = datetime.now()
                        # logger.info(
                        #     f"Updated traffic density for camera {camera.name}: {camera.traffic_density}%"
                        # )

        except Exception as e:
            logger.error(f"Error calculating traffic density: {e}")


# Create service instance
traffic_density_service = TrafficDensityService()
