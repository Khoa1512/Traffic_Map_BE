import os
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from ..models.camera import cameras

from .traffic_density import traffic_density_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CaptureService:
    def __init__(self):
        self.scheduler = None
        self.captures_dir = os.path.join('app', 'data', 'captures')
        os.makedirs(self.captures_dir, exist_ok=True)

    def capture_images(self):
        """Chỉ chụp ảnh và lưu vào folder"""
        try:
            # Xóa ảnh cũ
            for filename in os.listdir(self.captures_dir):
                file_path = os.path.join(self.captures_dir, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        # logger.info(f"Deleted old image: {filename}")
                except Exception as e:
                    logger.error(f"Error deleting {file_path}: {e}")

            # Chụp ảnh mới
            for cam_id, camera in cameras.items():
                try:
                    # logger.info(f"Capturing from camera {cam_id}")
                    response = requests.get(camera.snap_url, stream=True)
                    if response.status_code == 200:
                        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                        filename = f'{cam_id}_{timestamp}.jpg'
                        filepath = os.path.join(self.captures_dir, filename)

                        with open(filepath, 'wb') as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                        # logger.info(f"Saved image for camera {cam_id}")
                    else:
                        logger.error(
                            f"Failed to capture camera {cam_id}: HTTP {response.status_code}")
                except Exception as e:
                    logger.error(f"Error capturing camera {cam_id}: {e}")

            # Sau khi có ảnh mới, gọi service tính traffic density
            traffic_density_service.calculate()

        except Exception as e:
            logger.error(f"Error in capture_images: {e}")

    def start(self):
        if self.scheduler is None or not self.scheduler.running:
            self.scheduler = BackgroundScheduler()
            self.scheduler.add_job(
                func=self.capture_images,
                trigger="interval",
                seconds=12
            )
            self.scheduler.start()
            # Chụp ảnh lần đầu
            self.capture_images()
            logger.info(
                "Capture service started - will capture every 30 seconds")
            return True
        return False

    def stop(self):
        if self.scheduler and self.scheduler.running:
            self.scheduler.shutdown()
            self.scheduler = None
            logger.info("Capture service stopped")
            return True
        return False




# Create service instance
capture_service = CaptureService()
