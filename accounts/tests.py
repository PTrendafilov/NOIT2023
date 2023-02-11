from django.test import TestCase, Client
from accounts.models import Profile as User

class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@test.com')

    def test_index(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_page(self):
        self.client.login(email='test@test.com', password='testpassword')
        response = self.client.get('/accounts/logout/')
        self.assertRedirects(response, '/accounts/')

    def test_choose_role(self):
        response = self.client.get('/accounts/choose_role')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'choose-role-form.html')
        
    

