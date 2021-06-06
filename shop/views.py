from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Product, Purchase
from .forms import BuyProductFrom


def show_product(request):
    product = Product.objects.all()
    context = {
        'products': product,
    }
    return render(request, 'shop/home.html', context)


@login_required()
def buy_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':

        form = BuyProductFrom(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            purchase = Purchase(user=request.user, product=product, quantity=quantity)
            purchase.save()
            return redirect('shop:payment_done')

    else:
        form = BuyProductFrom()
        context = {
            'form': form,
            'product': product
        }
    return render(request, 'shop/payment.html', context)


@login_required()
def make_payment(request):
    purchase = Purchase.objects.filter(user=request.user).order_by("-pay_money")[0]
    print(purchase)
    return render(request, 'shop/success.html', {'purchase': purchase})
