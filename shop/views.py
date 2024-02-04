from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import*
import datetime
from rest_framework.permissions import IsAuthenticated  # <-- Here

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class CustomerAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShopCardAPIView(viewsets.ModelViewSet):
    queryset = ShopCard.objects.all()
    serializer_class = ShopCardSerializer

class ItemAPIView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AdminAPIView(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
  

class PurchaseAPIView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseHistoryView(APIView):  #Foydalanuvchi id bo'yicha xaridlar tarixini olish
    def get(self, request, user_id):
        purchases = Purchase.objects.filter(client_id=user_id)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

class CheckPurchaseAmountView(APIView): #Xaridorning umumiy xaridi 1 000 000 so'mdan ortiq yoki yo'qligini tekshirish
    def get(self, request, customer_id):
        total_purchase = Purchase.objects.filter(client_id=customer_id).aggregate(total_amount=models.Sum('total_amount'))
        if total_purchase['total_amount'] > 1000000:
            return Response({'message': "Mijozning xaridi 1 000 000 so'mdan ortiq"})
        else:
            return Response({'message': "Mijozning xaridi 1 000 000 so'mdan oshmaydi"})
        

class TotalProductQuantityView(APIView): #Barcha mahsulotlarning umumiy miqdorini olish
    def get(self, request):
        total_price = Product.objects.aggregate(total_price=models.Sum('price'))
        return Response({'total_price': total_price['total_price']})
    
class ExpiredProductsView(APIView): #Barcha muddati o'tgan mahsulotlar ro'yxatini olish
    def get(self, request):
        # expired_products = Product.objects.filter(expiration_date__lt=datetime.date.today())
        # serializer = ProductSerializer(expired_products, many=True)
        # return Response(serializer.data)
        expired_goods = Product.objects.filter(expiration_date__lt=datetime.date.today())
        return Response({'muddati otgan tovarlar': list(expired_goods.values())})
    
class BestSellingProductView(APIView): #Eng ko'p sotiladigan mahsulotni olish
    def get(self, request):
        best_selling_product = Product.objects.first()
        serializer = ProductSerializer(best_selling_product)
        return Response({'eng kop sotilgan mahsulot': best_selling_product.name})

