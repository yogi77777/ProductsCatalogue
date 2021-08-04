from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product,Order
from users.models import CustomUser
from .serializers import ProductSerializer,OrderSerializer
import json
from django.http import JsonResponse


# Create your views here.

class GetProducts(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        products_data = json.dumps(serializer.data)
        products_data = json.loads(products_data)
        return JsonResponse({"products":products_data})

class PlaceOrder(APIView):

    def post(self,request):
        user=CustomUser.objects.filter(email=request.data['email']).first()
        product = Product.objects.filter(id=request.data['product_id']).first()
        order = Order(user=user,product=product)
        order.save()
        return JsonResponse({"order_id":order.order_id,"message":"order placed successfully"})
        

class GetOrders(APIView):
    def get(self,request,email):
        user = CustomUser.objects.filter(email=email).first()
        orders = Order.objects.filter(user=user).order_by('-created_at')
        serializer = OrderSerializer(orders,many=True)
        orders_data = json.dumps(serializer.data)
        orders_data = json.loads(orders_data)
        return JsonResponse({"orders":orders_data})

        

