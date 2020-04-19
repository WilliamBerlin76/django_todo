from rest_framework import serializers

from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'passworkd'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']