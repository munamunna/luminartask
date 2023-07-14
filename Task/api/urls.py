from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import UserView

router=DefaultRouter()
router.register("users",UserView,basename="users")

urlpatterns =[
    
]+router.urls