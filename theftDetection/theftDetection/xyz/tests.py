from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse


class ApiRoutesTest(SimpleTestCase):
    def test_api_root_lists_endpoints(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('suspects', response.json()['endpoints'])
        self.assertIn('victims', response.json()['endpoints'])
        self.assertIn('police_officers', response.json()['endpoints'])
        self.assertIn('theftCases', response.json()['endpoints'])
        self.assertIn('stolenItems', response.json()['endpoints'])
        self.assertIn('policeCenter', response.json()['endpoints'])
        self.assertIn('history', response.json()['endpoints'])  
        self.assertIn('witness', response.json()['endpoints'])
        self.assertIn('evidences', response.json()['endpoints'])
        self.assertIn('investigationReports', response.json()['endpoints'])
        self.assertIn('notifications', response.json()['endpoints'])


# Create your tests here.
