from app.controllers.camera_controller import CameraController
from app.controllers.route_controller import RouteController
from flask import Blueprint
import logging

logging.basicConfig(level=logging.DEBUG)
api_bp = Blueprint('api', __name__)

camera_controller = CameraController()
route_controller = RouteController()


api_bp.route('/cameras', methods=['GET'])(camera_controller.get_all_cameras)
api_bp.route('/find-path', methods=['POST'])(route_controller.find_path)
api_bp.route('/capture/start', methods=['POST'])(camera_controller.start_capture)





