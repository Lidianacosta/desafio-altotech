from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("usuarios.urls")),
    path("", include("produtos.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("carrinho/", include("carrinho.urls")),
    path('', include("landing_pages.urls")),

    path("admin/", admin.site.urls),

    path('summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
