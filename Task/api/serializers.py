from rest_framework import serializers
from accounts.models import Useraccount

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Useraccount
        fields="__all__"
