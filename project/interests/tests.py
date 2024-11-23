from rest_framework.test import APITestCase
from rest_framework import status
from .models import PointOfInterest

class PointOfInterestTests(APITestCase):

    def setUp(self):
        self.poi_data = {
            "name": "Test POI",
            "description": "A point of interest for testing",
            "latitude": 45.0,
            "longitude": 90.0,
            "category": "test_category",
        }
        self.poi = PointOfInterest.objects.create(**self.poi_data)

    def test_create_poi(self):
        data = {
            "name": "New POI",
            "description": "Another point of interest",
            "latitude": 50.0,
            "longitude": 80.0,
            "category": "new_category",
        }
        response = self.client.post("/api/poi/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_poi(self):
        response = self.client.get("/api/poi/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_poi_by_id(self):
        response = self.client.get(f"/api/poi/{self.poi.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.poi_data["name"])

    def test_update_poi(self):
        data = {
            "name": "Updated POI",
            "description": "Updated description",
            "latitude": 60.0,
            "longitude": 70.0,
            "category": "updated_category",
        }
        response = self.client.put(f"/api/poi/{self.poi.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.poi.refresh_from_db()
        self.assertEqual(self.poi.name, "Updated POI")

    def test_delete_poi(self):
        response = self.client.delete(f"/api/poi/{self.poi.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PointOfInterest.objects.count(), 0)
