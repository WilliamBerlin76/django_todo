from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_by_id(request, pk):
    
    try:
        todo = UserTodo.objects.get(pk=request.kwargs['todo_id'])
    except UserTodo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = UserTodoSerializer(todo, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
