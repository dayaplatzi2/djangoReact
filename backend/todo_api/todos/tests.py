from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='primer registro')
        Todo.objects.create(description='es la primera descripcion')
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'primer registro')

    def test_descripcion_content(self):
        todo = Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'es la primera descripcion')


