from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("create-order/", views.create_order, name="create_order"),
    path("checkout/", views.create_order, name="checkout"),
    path("verify/<int:order_id>/<str:payment_method>/", views.payment_verification, name="payment_verification"),
    path("track_order/<str:order_reference>/", views.track_order, name="track_order")
]
