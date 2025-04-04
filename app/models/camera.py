class Camera:
    def __init__(self, id, name, latitude, longitude, stream_url, snap_url, district):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.stream_url = stream_url
        self.snap_url = snap_url
        self.district = district
        self.traffic_density = 0
        self.last_update = None


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'streamUrl': self.stream_url,
            'snapUrl': self.snap_url,
            'district': self.district,
            'trafficDensity': self.traffic_density,
            'lastUpdate': self.last_update
        }


cameras = {
    'A': Camera(
        'A',
        'Lý Thường Kiệt - Bắc Hải',
        10.777868,
        106.656145,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7d29bfd3d90017e8f437&camLocation=L%C3%BD%20Th%C6%B0%E1%BB%9Dng%20Ki%E1%BB%87t%20-%20B%E1%BA%AFc%20H%E1%BA%A3i&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7d29bfd3d90017e8f437',
        'Quận 10'
    ),
    'C': Camera(
        'C',
        'Cách mạng tháng 8 - Bắc Hải',
        10.786879,
        106.664586,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer?camId=63ae798abfd3d90017e8f255&camLocation=C%C3%A1ch%20M%E1%BA%A1ng%20Th%C3%A1ng%20T%C3%A1m%20-%20B%E1%BA%AFc%20H%E1%BA%A3i&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae798abfd3d90017e8f255',
        'Quận 10'
    ),
    'D': Camera(
        'D',
        'Cách mạng tháng 8 - Tô Hiến Thành',
        10.782844,
        106.672083,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7966bfd3d90017e8f240&camLocation=C%C3%A1ch%20M%E1%BA%A1ng%20Th%C3%A1ng%20T%C3%A1m%20-%20T%C3%B4%20Hi%E1%BA%BFn%20Th%C3%A0nh&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7966bfd3d90017e8f240',
        'Quận 10'
    ),
    'E': Camera(
        'E',
        'Tô Hiến Thành - Sư Vạn Hạnh',
        10.777894,
        106.665414,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7a74bfd3d90017e8f2c7&camLocation=T%C3%B4%20Hi%E1%BA%BFn%20Th%C3%A0nh%20%E2%80%93%20S%C6%B0%20V%E1%BA%A1n%20H%E1%BA%A1nh&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a74bfd3d90017e8f2c7',
        'Quận 10'
    ),
    'F': Camera(
        'F',
        'Thành Thái - Bắc Hải',
        10.780737,
        106.658844,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7c73bfd3d90017e8f3ed&camLocation=L%C3%BD%20Th%C6%B0%E1%BB%9Dng%20Ki%E1%BB%87t%20-%20T%C3%B4%20Hi%E1%BA%BFn%20Th%C3%A0nh%202&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7c73bfd3d90017e8f3ed',
        'Quận 10'
    ),
    'G': Camera(
        'G',
        'Lý Thường Kiệt - Tô Hiến Thành',
        10.770474,
        106.658336,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7c53bfd3d90017e8f3d8&camLocation=L%C3%BD%20Th%C6%B0%E1%BB%9Dng%20Ki%E1%BB%87t%20-%20T%C3%B4%20Hi%E1%BA%BFn%20Th%C3%A0nh%201&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7c53bfd3d90017e8f3d8',
        'Quận 10'
    ),
    'H': Camera(
        'H',
        '3/2 - Lý Thường Kiệt',
        10.763762,
        106.660012,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=5deb576d1dc17d7c5515ad23&camLocation=Ba%20Th%C3%A1ng%20Hai%20-%20L%C3%BD%20Th%C6%B0%E1%BB%9Dng%20Ki%E1%BB%87t&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/5deb576d1dc17d7c5515ad23',
        'Quận 10'
    ),
    'I': Camera(
        'I',
        'Nguyễn Chí Thanh - Nguyễn Tri Phương',
        10.759991,
        106.668812,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=649da419a6068200171a6c90&camLocation=Nguy%E1%BB%85n%20Ch%C3%AD%20Thanh%20-%20Ng%C3%B4%20Quy%E1%BB%81n&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/649da419a6068200171a6c90',
        'Quận 10'
    ),
    'J': Camera(
        'J',
        'Điện Biên Phủ - Nguyễn Thượng Hiền',
        10.775945,
        106.682875,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=66f1266f538c780017c93579&camLocation=H%C3%B9ng%20V%C6%B0%C6%A1ng%20-%20Nguy%E1%BB%85n%20Ch%C3%AD%20Thanh&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/66f1266f538c780017c93579',
        'Quận 10'
    ),
    'K': Camera(
        'K',
        '3/2 - Nguyễn Tri Phương',
        10.767623,
        106.667172,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7a26bfd3d90017e8f29a&camLocation=Ba%20Th%C3%A1ng%20Hai%20-%20L%C3%AA%20H%E1%BB%93ng%20Phong%202&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a26bfd3d90017e8f29a',
        'Quận 10'
    ),
    'L': Camera(
        'L',
        '3/2 - Lý Thái Tổ',
        10.768008,
        106.667963,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae763bbfd3d90017e8f0c4&camLocation=L%C3%BD%20Th%C3%A1i%20T%E1%BB%95%20-%20Nguy%E1%BB%85n%20%C4%90%C3%ACnh%20Chi%E1%BB%83u&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae763bbfd3d90017e8f0c4',
        'Quận 10'
    ),
    'M': Camera(
        'M',
        '3/2 - Sư Vạn Hạnh',
        10.769752,
        106.67078,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7a50bfd3d90017e8f2b2&camLocation=Ba%20Th%C3%A1ng%20Hai%20%E2%80%93%20S%C6%B0%20V%E1%BA%A1n%20H%E1%BA%A1nh&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a50bfd3d90017e8f2b2',
        'Quận 10'
    ),
    'N': Camera(
        'N',
        '3/2 - Lê Hồng Phong',
        10.771078,
        106.673169,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7a08bfd3d90017e8f285&camLocation=Ba%20Th%C3%A1ng%20Hai%20-%20L%C3%AA%20H%E1%BB%93ng%20Phong%201&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a08bfd3d90017e8f285',
        'Quận 10'
    ),
    'P': Camera(
        'P',
        'Điện Biên Phủ - Cao Thắng',
        10.772608,
        106.679147,
        'http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae7a9cbfd3d90017e8f303&camLocation=%C4%90i%E1%BB%87n%20Bi%C3%AAn%20Ph%E1%BB%A7%20%E2%80%93%20Cao%20Th%E1%BA%AFng&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae7a9cbfd3d90017e8f303',
        'Quận 10'
    ),
    'Q': Camera(
        'Q',
        '3/2 - Cách mạng tháng 8',
        10.777878,
        106.681257,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=63ae73cebfd3d90017e8f00d&camLocation=Nguy%E1%BB%85n%20Th%E1%BB%8B%20Minh%20Khai%20-%20C%E1%BB%91ng%20Qu%E1%BB%B3nh&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/63ae73cebfd3d90017e8f00d',
        'Quận 10'
    ),
    'R': Camera(
        'R',
        'Ngã bả Lý Thái Tổ',
        10.767627,
        106.674608,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=5deb576d1dc17d7c5515acf6&camLocation=N%C3%BAt%20giao%20Ng%C3%A3%20s%C3%A1u%20C%E1%BB%99ng%20H%C3%B2a&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/5deb576d1dc17d7c5515acf6',
        'Quận 10'
    ),
    'O': Camera(
        'O',
        'Nút giao Ngã Sáu Cộng Hoà',
        10.765358,
        106.681179,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=5deb576d1dc17d7c5515acf7&camLocation=N%C3%BAt%20giao%20Ng%C3%A3%20s%C3%A1u%20C%E1%BB%99ng%20H%C3%B2a&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/5deb576d1dc17d7c5515acf7',
        'Quận 10'
    ),
    'S': Camera(
        'S',
        'Hùng Vương - Lê Hồng Phong',
        10.762156,
        106.676384,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=5d8cd3b7766c880017188942&camLocation=L%C3%AA%20H%E1%BB%93ng%20Phong%20-%20Nguy%E1%BB%85n%20Tr%C3%A3i&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8',
        'http://camera.thongtingiaothong.vn/api/snapshot/5d8cd3b7766c880017188942',
        'Quận 10'
    ),
    'Z': Camera(
        'Z',
        'Lý Thường Kiệt - Nguyễn Chí Thanh',
        10.758456,
        106.661515,
        'https://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=66f126e8538c780017c9362f&camLocation=Nguy%E1%BB%85n%20Ch%C3%AD%20Thanh%20-%20Nguy%E1%BB%85n%20Kim&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3',
        'http://camera.thongtingiaothong.vn/api/snapshot/66f126e8538c780017c9362f',
        'Quận 10'
    ),
}
