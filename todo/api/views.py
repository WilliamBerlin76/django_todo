from rest_framework import viewsets
from .serializers import UserTodoSerializer
from todo.models import UserTodo

class UserTodoViewset(viewsets.ModelViewSet):
    serializer_class = UserTodoSerializer
    queryset = UserTodo.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return UserTodo.objects.none()

        else:
            return UserTodo.objects.filter(user=user)

class TodoByIdViewset(viewsets.ModelViewSet):
    serializer_class = UserTodoSerializer
    queryset = UserTodo.objects.none()

    def get_queryset(self):
        user = self.request.user
        todo_id = self.kwargs['todo_id']
        if user.is_anonymous:
            return UserTodo.objects.none()
        else:
            return UserTodo.objects.filter(id=todo_id)