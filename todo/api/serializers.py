from rest_framework import serializers

from todo.models import UserTodo

class UserTodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserTodo
        fields = ('name', 'description', 'priority')

    def create(self, validated_data):
        user = self.context['request'].user
        todo = UserTodo.objects.create(user=user, **validated_data)
        return todo