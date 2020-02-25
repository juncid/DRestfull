from django.utils.http import urlencode
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import DroneCategory
from . import views


class DroneCategoryTests(APITestCase):

    def post_drone_category(self, name):
        url = reverse(views.DroneCategoryList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_drone_category(self):
        """
        Ensure we can create a new DroneCategory and then retrieve it
        """
        new_drone_category_name = 'Hexacopter'
        response = self.post_drone_category(new_drone_category_name)
        drone_category_id = DroneCategory.objects.get().pk
        print("PK {0}".format(drone_category_id))
        assert response.status_code == status.HTTP_201_CREATED
        assert DroneCategory.objects.count() == 1
        assert DroneCategory.objects.get().name == new_drone_category_name

