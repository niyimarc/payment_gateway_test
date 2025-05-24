from django.shortcuts import render, redirect, get_object_or_404
from django_pg.payment import verify_payment
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
    print(payment_method)
    return render(request, "store/checkout.html", context)

@login_required
def payment_verification(request, order_id, payment_method):
    if payment_method == "paystack":
        transaction_id = request.GET.get('reference')
    if payment_method == "flutterwave":
        transaction_id = request.GET.get('transaction_id')
    else:
        messages.error(request, "Unsupported payment method")
        return redirect('store:create_order')
    
    result = verify_payment(order_id, transaction_id, request.user, payment_method)

    if result.get("success"):
        # redirect to track order for example if payment is successful
        return redirect('store:track_order', order_reference=result["order_reference"])
    else:
        print("Payment verification failed")
        messages.error(request, result.get("message", "Payment verification failed"))
        return redirect('store:create_order')

@login_required
def track_order(request, order_reference):
    order = get_object_or_404(Order, order_reference=order_reference)
    context = {
        "order": order,
    }
    return render(request, "store/track.html", context)