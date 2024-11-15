from django.contrib import admin
from django.urls import path, include, re_path  # Include re_path for regex patterns
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from users.views import *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mun_dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/', include('api.urls')),
    re_path(r'^dj_rest-auth/', include('dj_rest_auth.urls')),  # Use re_path instead of url
    re_path(r'^dj_rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Use re_path instead of url
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
