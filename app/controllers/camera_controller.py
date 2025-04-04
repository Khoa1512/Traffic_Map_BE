from flask import jsonify
from ..utils.camera_capture import capture_service
from ..models.camera import cameras
import logging

logging.basicConfig(level=logging.DEBUG)

class CameraController:


    def get_all_cameras(self):
        try:
            camera_list = [camera.to_dict() for camera in cameras.values()]
            return jsonify(camera_list)
        except Exception as e:
            logging.error(f"Error in get_cameras: {str(e)}")
            return jsonify({'error': str(e)}), 500

    def start_capture(self):
        try:
            if capture_service.start():
                # Khi bắt đầu capture service, cũng bắt đầu tính traffic density
                return jsonify({
                    'status': 'success',
                    'message': 'Capture service started'
                })
            return jsonify({
                'status': 'warning',
                'message': 'Capture service already running'
            })
        except Exception as e:
            logging.error(f"Error starting capture: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500


