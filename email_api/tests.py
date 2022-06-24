from rest_framework import status
from rest_framework.test import APITestCase

from django.conf import settings

class SendEmailTests(APITestCase):
    def test_send_email(self):
        url = '/v1/api/send-email/'
        data = {
                'email': 'azizbekgafurov00963@gmail.com',
                "mess_title": "This is message title",
                "mess_body": "This is message body",
                "from_to": "MyTaxi <noreply@mytaxi.uz>"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        