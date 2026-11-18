from django.urls import path
from Employee import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("employee",views.Create_or_List.as_view()),
    path("employee/<int:id>",views.RetrieveUpdateDelete.as_view()),
   
]