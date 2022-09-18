from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    # path('blog/', BlogList.as_view()),
    # path('blog/<int:pk>/', BlogDetail.as_view()),
]