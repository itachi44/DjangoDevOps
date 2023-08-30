from django.test import TestCase
from django.urls import reverse
from users.models import *


class UserListViewTest(TestCase):
    def setUp(self):
        # Créez quelques utilisateurs pour le test
        Account.objects.create(username='user1', email='user1@example.com', first_name='John', last_name='Doe')
        Account.objects.create(username='user2', email='user2@example.com', first_name='Jane', last_name='Smith')

    def test_user_list_view(self):
        url = reverse('users_list')  # Remplacez 'user-list' par le nom de l'URL de votre vue
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)  # Vérifiez si la page se charge correctement
        self.assertContains(response, 'user1')
        self.assertContains(response, 'user2')
        # Assurez-vous d'ajouter d'autres assertions pour vérifier les détails des utilisateurs