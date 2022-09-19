from django.urls import path
from .views import *

urlpatterns = [
    # path('user/', UserList.as_view()),
    # path('user/<int:pk>/', UserDetail.as_view()),
    # path('blog/', BlogList.as_view()),
    # path('blog/<int:pk>/', BlogDetail.as_view()),
    path('reg_user', reg_user, name="reg_user"),
    path('reg_blog', reg_blog, name="reg_blog"),
    # path('user_login', user_login, name="user_login"),
]