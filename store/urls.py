from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('product/', views.product, name="product"),

	path('update_item/', views.updateItem, name="update_item"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)