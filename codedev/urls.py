from django.contrib import admin
from django.urls import path
from .import views
from django.urls import re_path as url
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^about/$',views.about),
    url(r'^$',article_views.article_list, name="home"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)