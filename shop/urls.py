from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customer', CustomerAPIView, basename='customer')
router.register(r'category', CategoryAPIView, basename='category')
router.register(r'product', ProductAPIView, basename='product')
router.register(r'shopCard', ShopCardAPIView, basename='shopCard')
router.register(r'item', ItemAPIView, basename='item')
router.register(r'admin', AdminAPIView, basename='admin')
router.register(r'purchase', PurchaseAPIView, basename='purchase')

urlpatterns = [
    path('purchase-history/<int:user_id>/', PurchaseHistoryView.as_view(), name='purchase-history'),
    path('check-purchase-amount/<int:customer_id>/', CheckPurchaseAmountView.as_view(), name='check-purchase-amount'),
    path('total-product-quantity/', TotalProductQuantityView.as_view(), name='total-product-quantity'),
    path('expired-products/', ExpiredProductsView.as_view(), name='expired-products'),
    path('best-selling-product/', BestSellingProductView.as_view(), name='best-selling-product'),
    path('auth/',HelloView.as_view(), name='auth'),
    path('get-token/', obtain_auth_token, name='get-token'),  # <-- And here
] + router.urls 
