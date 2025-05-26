from django.shortcuts import render, redirect, get_object_or_404
from django_pg.views import payment_verification
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order
from django.conf import settings

@login_required
def create_order(request):
    order = Order.objects.create(user=request.user, total_price=5000.00, payment_method="flutterwave")
    payment_method = order.payment_method
    context = {
        "order": order,
        "payment_method": payment_method,
        "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
        "FLUTTERWAVE_PUBLIC_KEY": settings.FLUTTERWAVE_PUBLIC_KEY,
    }
    return render(request, "store/checkout.html", context)

@login_required
def track_order(request, order_reference):
    order = get_object_or_404(Order, order_reference=order_reference)
    context = {
        "order": order,
    }
    return render(request, "store/track.html", context)