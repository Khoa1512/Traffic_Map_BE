import logging

from flask import jsonify, request
from ..utils.astar import AStarGraph


class RouteController:
    def find_path(self):
        try:
            data = request.json
            start_id = data.get('start')
            end_id = data.get('end')

            if not start_id or not end_id:
                return jsonify({
                    'success': False,
                    'message': 'Thiếu điểm xuất phát hoặc điểm đến'
                }), 400

            # Tạo graph mới cho mỗi request để có traffic density mới nhất
            current_graph = AStarGraph()

            # Khởi tạo edges với chi phí cơ bản
            base_edges = [
                ('A', 'G', 4), ('A', 'H', 8), ('C', 'D', 5),
                ('C', 'Q', 11), ('E', 'M', 6), ('F', 'K', 6),
                ('G', 'F', 4), ('M', 'E', 6), ('N', 'S', 5),
                ('H', 'L', 5), ('H', 'P', 11), ('H', 'K', 4),
                ('K', 'L', 1), ('L', 'M', 1), ('M', 'N', 1),
                ('N', 'P', 3), ('P', 'Q', 3), ('Q', 'J', 1),
                ('J', 'U', 3), ('N', 'R', 2), ('J', 'R', 3),
                ('R', 'L', 3), ('R', 'O', 4), ('R', 'S', 4),
                ('R', 'I', 5), ('I', 'S', 5), ('K', 'I', 5),
                ('I', 'Z', 2), ('O', 'S', 4), ('H', 'Z', 4),
                ('H', 'G', 4), ('E', 'F', 1), ('E', 'D', 4)
            ]

            # Thêm edges vào graph
            for from_node, to_node, base_cost in base_edges:
                current_graph.add_edge(from_node, to_node, base_cost)

            # Tìm đường với traffic density hiện tại
            path, cost = current_graph.a_star(start_id, end_id)

            if path is None:
                return jsonify({
                    'success': False,
                    'message': 'Không tìm thấy đường đi'
                }), 404

            # Lấy chi tiết đường đi với traffic density
            path_details = current_graph.get_path_details(path)

            logging.debug(f"Đường đi: {path}")
            logging.debug(f"Chi tiết đường đi: {path_details}")

            return jsonify({
                'success': True,
                'path': path,
                'cost': cost,
                'details': path_details
            })

        except Exception as e:
            logging.error(f"Error in find_path: {str(e)}")
            return jsonify({
                'success': False,
                'message': 'Có lỗi xảy ra'
            }), 500
