from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
	path('getUser',views.getUser.as_view())
]