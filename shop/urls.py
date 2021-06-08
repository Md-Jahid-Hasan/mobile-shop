from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.show_product, name='product_show'),
    path('<int:product_id>/payment/', views.buy_product, name='payment'),
    path('success/', views.make_payment, name='payment_done'),
]