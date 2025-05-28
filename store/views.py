from django.shortcuts import render, redirect, get_object_or_404
from django_pg.views import payment_verification
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from django.conf import settings

@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = form.cleaned_data["total_price"]
            payment_method = form.cleaned_data["payment_method"]

            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                payment_method=payment_method
            )

            context = {
                "order": order,
                "payment_method": payment_method,
                "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
                "FLUTTERWAVE_PUBLIC_KEY": settings.FLUTTERWAVE_PUBLIC_KEY,
                "INTERSWITCH_MERCHANT_CODE": settings.INTERSWITCH_MERCHANT_CODE,
                "INTERSWITCH_PAY_ITEM_ID": settings.INTERSWITCH_PAY_ITEM_ID,
            }
            return render(request, "store/checkout.html", context)
    else:
        form = OrderForm()

    return render(request, "store/create_order.html", {"form": form})

@login_required
def track_order(request, order_reference):
    order = get_object_or_404(Order, order_reference=order_reference)
    context = {
        "order": order,
    }
    return render(request, "store/track.html", context)