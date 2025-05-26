from django.shortcuts import redirect

def payment_success_redirect(result):
    return redirect('store:track_order', order_reference=result["order_reference"])

def payment_failure_redirect(result):
    return redirect('store:create_order')
