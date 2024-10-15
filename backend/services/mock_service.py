from services.base_service import CoordsService
class MockService(CoordsService):
    def get_coords(self, ciudad, pais):
        return {'lat': 35.6897, 'lng': 139.6922}
