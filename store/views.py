from django.shortcuts import render, redirect, get_object_or_404
from django_pg.payment import verify_payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order
from django.conf import settings

@login_required
def create_order(request):
    order = Order.objects.create(user=request.user, total_price=5000, payment_method="paystack")
    payment_method = order.payment_method
    context = {
        "order": order,
        "payment_method": payment_method,
        "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
    }
    return render(request, "store/checkout.html", context)

@login_required
def payment_verification(request, order_id, payment_method):
    reference = request.GET.get('reference')
    result = verify_payment(order_id, reference, request.user, payment_method)

    if result.get("success"):
        # redirect to track order for example if payment is successful
        return redirect('store:track_order', order_reference=result["order_reference"])
    else:
        messages.error(request, result["message"])
        return redirect('store:shop')

@login_required
def track_order(request, order_reference):
    order = get_object_or_404(Order, order_reference=order_reference)
    context = {
        "order": order,
    }
    return render(request, "store/track.html", context)