"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myblog import settings

from blog.views import root

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'blog.views.forbidden'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'




"""
127.0.0.1:8005/          = mysite.com/              ''
127.0.0.1:8005/blog/     = mysite.com/blog/         'blog/'
127.0.0.1:8005/blog/     = mysite.com/blog/about/
"""