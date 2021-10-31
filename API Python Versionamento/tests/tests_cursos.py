from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso Teste 1', nivel='B'
        )

        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso Teste 2', nivel='C'
        )

    def test_get_listar_cursos(self):
        """Testando o get de cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_criar_curso(self):
        """Testando o post de cursos"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_nao_pode_delete(self):
        """Teste para validar a impossibilidade de usar o delete"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_curso(self):
        """Valida que está podendo atualizar o curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 Atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)