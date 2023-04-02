from django.contrib import admin
from django.urls import path, include
from .views import homeview
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from accounts.views import contact_view
from store.views import delete_product, my_listings,  addproducts, ProductUpdateView
admin.site.site_header = "ADEYEMI-Ecommerce Admin"
admin.site.site_title = "ADEYEMI=Ecommerce Admin Panel"
admin.site.index_title = "Welcome to ADEYEMI Admin Panel"

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('elijahlogin/', admin.site.urls),
    path('home', homeview, name='home'),
    path('', RedirectView.as_view(url='/home')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('account/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('add/', addproducts, name='addProducts'),
    path('mylistings/', my_listings,name='mylistings'),
    path('delete/<int:id>/', delete_product,name='delete_product'),
    path('update/<int:pk>/',ProductUpdateView.as_view(),name='update_product'),
    path('contact/', contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
