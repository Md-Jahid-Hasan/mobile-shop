from django.views.decorators import gzip
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Product, Purchase
from .forms import BuyProductFrom
from users.models import Machine


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# @gzip.gzip_page
# def camera_feed(request):
#     try:
#         camera = VideoCamera()
#         return StreamingHttpResponse(gen(camera), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         return StreamingHttpResponse(np.zeros((300, 300, 3), np.uint8))


def show_product(request):
    product = Product.objects.all()

    if request.method == 'POST':
        machine_id = request.POST['machineID']
        try:
            machine = Machine.objects.get(machine_code=machine_id)
            print(machine.product.id)
            return redirect('shop:payment', machine.product.id)
        except:
            messages.error(request, "This code is not valid")

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
