from http.client import responses
from django.test import TestCase
from .models import employeeDetail, employeeRegistratoin

# Create your tests here.
class SignInViewTest(TestCase):
    """this is used to test employee functionalty and save 
    with dummy and correct data in the database.
    """
    def setUp(self):
        user=employeeRegistratoin.objects.create(first_name='test', 
                                                            last_name='12test12', 
                                                            email='test@example.com',
                                                            password='asdasd',
                                                            phone='8798435454',)
        user.save()
        self.assertEqual(responses.data['authenticated'])

    def test_correct(self):
        response = self.client.post('/employeelogin/', {'email': 'vamtore@gmail.com', 'password': 'vamtore@1234'})
        self.assertEqual(response.data['authenticated'])

    def test_wrong_username(self):
        response = self.client.post('/employeelogin/', {'email': 'wrong', 'password': '12test12'})
        self.assertFalse(response.data['authenticated'])

    def test_wrong_pssword(self):
        response = self.client.post('/employeelogin/', {'email': 'test', 'password': 'wrong'})
        self.assertFalse(response.data['authenticated'])
