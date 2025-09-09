from django.test import TestCase, Client

class MainViewTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_context_data(self):
        response = Client().get('')
        self.assertContains(response, "SweetBall Shop")
        self.assertContains(response, "2406437533")  
        self.assertContains(response, "Qoriana Syahwa Maharani")   
        self.assertContains(response, "PBP-B")
