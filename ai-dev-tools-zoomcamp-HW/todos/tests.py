from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(title="Test Todo", description="Test Description")
        self.assertEqual(str(todo), "Test Todo")
        self.assertFalse(todo.resolved)

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="Test Todo", description="Test Description")

    def test_list_view(self):
        response = self.client.get(reverse("todos:todo_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_create_view(self):
        response = self.client.post(reverse("todos:todo_create"), {
            "title": "New Todo",
            "description": "New Description",
            "due_date": "2025-12-31",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Todo.objects.filter(title="New Todo").exists())

    def test_update_view(self):
        response = self.client.post(reverse("todos:todo_edit", args=[self.todo.id]), {
            "title": "Updated Todo",
            "description": "Updated Description",
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated Todo")

    def test_delete_view(self):
        response = self.client.post(reverse("todos:todo_delete", args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())

    def test_toggle_resolved(self):
        response = self.client.post(reverse("todos:todo_toggle", args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)

class TodoFormTest(TestCase):
    def test_valid_form(self):
        data = {
            "title": "Form Todo",
            "description": "Form Description",
            "due_date": "2025-12-31",
        }
        response = self.client.post(reverse("todos:todo_create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title="Form Todo").exists())