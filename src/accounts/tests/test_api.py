import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import CustomUser

from accounts.serializers import CustomUserSelializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin')

        self.custom_user_1 = CustomUser.objects.create(username='Ari', password='1234', first_name='Ari',                                                 last_name='Bray',email='ar@g.com', phone='3492234',                                                     birdthday='1979-09-23', age='41',is_active='True',
                                                  is_staff='False', language='fr', status='RENTER',
                                                  created_at='08:22:50', updated_at='08:22:50')
        self.custom_user_2 = CustomUser.objects.create(username='Bari', password='1234', first_name='Bari',
                                                  last_name='Arays', email='ba@r.com', phone='304841999',
                                                  birdthday='1991-01-15', age='30', is_active='True',
                                                  is_staff='False', language='ru', status='OWNER',
                                                  created_at='08:28:50', updated_at='08:28:50')

    def test_get(self):
        url = reverse('customuser-list')
        self.client.force_login(self.user)
        response = self.client.get(url)
        serializer_data = CustomUserSelializer([self.custom_user_1, self.custom_user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('customuser-list')
        self.client.force_login(self.user)
        response = self.client.get(url, data={'search':'304841999'})
        serializer_data = CustomUserSelializer([self.custom_user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, CustomUser.objects.all().count())
        url = reverse('customuser-list')
        data = {
            "username": 'Ara',
            "password": '1234',
            "first_name": 'Ari',
            "last_name": 'Brai',
            "email": 'ara@g.com',
            "phone": '3492236',
            "birdthday": '1978-09-23',
            "age": '42',
            "is_active": 'True',
            "is_staff": 'False',
            "language": 'fr',
            "status": 'RENTER',
            "created_at": '08:22:50',
            "updated_at": '08:22:50'
       }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, CustomUser.objects.all().count())

    def test_update(self):
        url = reverse('customuser-detail', args=(self.custom_user_1.id,))
        data = {
            "username": self.custom_user_1.username,
            "password": '1234',
            "first_name": 'Ari',
            "last_name": self.custom_user_1.last_name,
            "email": 'ara@g.com',
            "phone": '95455322',
            "birdthday": '1978-09-23',
            "age": '42',
            "is_active": 'True',
            "is_staff": 'False',
            "language": 'fr',
            "status": 'RENTER',
            "created_at": '08:22:50',
            "updated_at": '08:22:50'
       }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.custom_user_1.refresh_from_db()
        self.assertEqual('95455322', self.custom_user_1.phone)
