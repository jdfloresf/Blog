"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

# SEO
from django.contrib.sitemaps.views import sitemap
from apps.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('apps.users.urls')),
    re_path('', include('apps.home.urls')),
    re_path('', include('apps.entrada.urls')),
    re_path('', include('apps.favoritos.urls')),

    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

sitemaps = {
    'site': Sitemap(
        [
            'home_app:index'
        ]
    ),
    'entradas': EntrySitemap
}

urlpatterns_sitemap = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, 
         name='jango.contrib.sitemaps.views.sitemap'),
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap