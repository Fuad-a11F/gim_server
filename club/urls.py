from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.api.urls')),
    path('api/auth_2/', include('reg.api.urls')),
    path('api/music/', include('music.api.urls')),
    path('api/gim/', include('gim.api.urls')),
    path('api/friend/', include('friend.api.urls')),
    path('api/note/', include('note.api.urls')),
    path('api/user/', include('users.api.urls')),
    path('api/food/', include('food.api.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)