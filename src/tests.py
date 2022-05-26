from django.test import TestCase
from .models import employeeDetail, employeeRegistratoin

# Create your tests here.
class SignInViewTest(TestCase):

    def setUp(self):
        employeeRegistratoin.objects.create(first_name='test', 
                                                            last_name='12test12', 
                                                            email='test@example.com',
                                                            password='asdasd',
                                                            phone='8798435454',)
        

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('/employeelogin/', {'email': 'vamtore@gmail.com', 'password': 'vamtore@1234'})
        self.assertTrue(response.data['authenticated'])

    def test_wrong_username(self):
        response = self.client.post('/employeelogin/', {'email': 'wrong', 'password': '12test12'})
        self.assertFalse(response.data['authenticated'])

    def test_wrong_pssword(self):
        response = self.client.post('/employeelogin/', {'email': 'test', 'password': 'wrong'})
        self.assertFalse(response.data['authenticated'])
