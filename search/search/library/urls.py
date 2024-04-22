from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
#path('', views.home, name="home"),
#path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Set login page as default
path('home/', views.home, name='home'),
path('logout/', LogoutView.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)