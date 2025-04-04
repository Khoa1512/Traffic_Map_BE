import heapq
from ..models.camera import cameras


class AStarGraph:
    def __init__(self):
        # Lưu đồ thị theo định dạng {node: [(neighbor, base_cost)]}
        self.edges = {}
        self.base_costs = {}  # Lưu trữ chi phí gốc của các cạnh

    def add_edge(self, from_node, to_node, cost):
        """Thêm cạnh vào đồ thị với chi phí gốc"""
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []

        # Lưu cạnh với chi phí gốc
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))

        # Lưu chi phí gốc
        edge_key = tuple(sorted([from_node, to_node]))
        self.base_costs[edge_key] = cost

    def get_dynamic_edge_cost(self, from_node, to_node, base_cost):
        """Tính chi phí cạnh dựa trên traffic density của cả hai node"""
        from_density = cameras[from_node].traffic_density if from_node in cameras else 0
        to_density = cameras[to_node].traffic_density if to_node in cameras else 0

        # Lấy mật độ trung bình của hai điểm
        avg_density = (from_density + to_density) / 2

        # Tăng chi phí theo mật độ giao thông
        # Ví dụ: density 100% sẽ làm tăng chi phí lên gấp đôi
        return base_cost * (1 + avg_density / 100)

    def get_current_heuristic(self, node):
        """Lấy giá trị heuristic hiện tại dựa trên traffic density"""
        if node in cameras:
            return cameras[node].traffic_density
        return 0

    def a_star(self, start, goal):
        """
        Thuật toán A* với chi phí động dựa trên traffic density.
        Trả về đường đi và chi phí (path, cost).
        """
        if start not in self.edges or goal not in self.edges:
            return None, float('inf')

        pq = []  # Priority queue
        # Initial cost dựa trên traffic density hiện tại
        initial_heuristic = self.get_current_heuristic(start)
        heapq.heappush(pq, (initial_heuristic, 0, start, [start]))

        visited = set()

        while pq:
            _, cost_so_far, current_node, path = heapq.heappop(pq)

            if current_node == goal:
                return path, cost_so_far

            if current_node in visited:
                continue

            visited.add(current_node)

            # Xét các node kề
            for neighbor, base_cost in self.edges[current_node]:
                if neighbor not in visited:
                    # Tính chi phí động cho cạnh hiện tại
                    dynamic_cost = self.get_dynamic_edge_cost(
                        current_node, neighbor, base_cost)
                    new_cost = cost_so_far + dynamic_cost

                    # Tính heuristic dựa trên traffic density hiện tại
                    current_heuristic = self.get_current_heuristic(neighbor)
                    estimated_total = new_cost + current_heuristic

                    heapq.heappush(
                        pq, (estimated_total, new_cost, neighbor, path + [neighbor]))

        return None, float('inf')

    def get_path_details(self, path):
        """
        Trả về chi tiết về đường đi bao gồm:
        - Tổng chi phí
        - Chi phí từng đoạn
        - Traffic density của từng node
        """
        if not path or len(path) < 2:
            return None

        details = {
            'total_cost': 0,
            'segments': [],
            'densities': {}
        }

        for i in range(len(path) - 1):
            from_node = path[i]
            to_node = path[i + 1]

            # Lấy chi phí gốc
            edge_key = tuple(sorted([from_node, to_node]))
            base_cost = self.base_costs[edge_key]

            # Tính chi phí thực tế với traffic density
            actual_cost = self.get_dynamic_edge_cost(
                from_node, to_node, base_cost)

            segment = {
                'from': from_node,
                'to': to_node,
                'base_cost': base_cost,
                'actual_cost': actual_cost,
                'traffic_density': {
                    'from': cameras[from_node].traffic_density if from_node in cameras else 0,
                    'to': cameras[to_node].traffic_density if to_node in cameras else 0
                }
            }

            details['segments'].append(segment)
            details['total_cost'] += actual_cost

        # Thêm traffic density của tất cả các node trong đường đi
        for node in path:
            details['densities'][node] = cameras[node].traffic_density if node in cameras else 0

        return details
