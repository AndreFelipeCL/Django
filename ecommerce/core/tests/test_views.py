from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def tearDown(self):
        pass

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_invalid(self):
        data = {
            'name': '',
            'email': '',
            'message': '',
        }
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_form_valid(self):
        data = {
            'name': 'André Felipe C. Leite',
            'email': 'andre@email.com.br',
            'message': 'asdasdasdasdasd.',
        }
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertTrue(response.context['form'].is_valid())
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato Django E-commerce')
