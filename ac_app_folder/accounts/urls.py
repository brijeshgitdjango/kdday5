from django.conf.urls import url
from .views import func, LoginView, LogoutView

urlpatterns = [
    
    url(r'^$', func, name="home"),
    url(r'^login/$', LoginView, name="login"),
    url(r'^logout/$', LogoutView, name="logout"),
]
