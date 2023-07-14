
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.models import Useraccount
from api.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=Useraccount.objects.all()
    model=Useraccount
    
