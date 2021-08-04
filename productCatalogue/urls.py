"""productCatalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from product.views import PlaceOrder,GetProducts,GetOrders



urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/order',PlaceOrder.as_view(),name="place-order"),
    path("get/orders/<str:email>",GetOrders.as_view(),name="get-orders"),
    path('get/products',GetProducts.as_view(),name="get-products"),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),

   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
