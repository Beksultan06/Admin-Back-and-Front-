from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from app.base.views import index
from core.yasg import urlpatterns_yasg
from django.views.generic import TemplateView


class ViteTemplateView(TemplateView):
    def get_template_names(self):
        return ["index.html"]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urlpatterns_yasg)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    re_path(r"^(?:.*)/?$", ViteTemplateView.as_view(), name="vite_react"),
    path('', index, name='index'),
    path('<path:path>', index),
    path("api/v1/base/", include("app.base.urls")),
    path("api/v1/passport/", include("app.passport.urls")),
    path("api/v1/news/", include("app.news.urls")),
    path("api/v1/managers/", include("app.managers.urls")),
    path("api/v1/gallery/", include("app.gallery.urls")),
    path("api/metrick/", include("app.metrick.urls")),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)