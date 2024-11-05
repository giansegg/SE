from services.base_service import CoordsService
class MockService(CoordsService):
    def get_coords(self, ciudad, pais):
        return {'lat': 0, 'lng':0}
