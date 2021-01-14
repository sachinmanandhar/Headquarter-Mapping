"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from formback import views 

from municipality.views import MunPostTemp,MunGet,update,MunGetAll,MunGetDist
from rest_framework.urlpatterns import format_suffix_patterns 
#from signup.views import  signupformAPI, UserLogin
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views
from formback.views import updateW

router = routers.DefaultRouter()                      # add this
#router.register(r'form', views.FormView, 'Form')
router.register(r'tryform', views.TryFormView, 'TryForm')



urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include(router.urls)),
	url(r'^getward/', views.formAPI.as_view()),
	url(r'^postward/', views.postFormAPI.as_view()),
	url(r'^getwardAll/', views.WardFormAll.as_view()),
	url(r'^getwardMun/', views.WardFormMun.as_view()),
	url(r'^MunPost/', MunPostTemp.as_view()),
	url(r'^MunData/', MunGet.as_view()),
	url(r'^MunAll/', MunGetAll.as_view()),
	url(r'^MunDist/', MunGetDist.as_view()),
	#url(r'^signup/',signupformAPI.as_view()),
	url(r'^api-auth',include('rest_framework.urls')),
	#url(r'^api/token/', TokenObtainPairView.as_view()),
	#url(r'^api/token/refresh/', TokenRefreshView.as_view()),
	#url(r'^login/',UserLogin.as_view()),
	url(r'^updateMun/',update),
	url(r'^updateWard/',updateW),
	path('api/v1/', include('api.urls')),	
]

