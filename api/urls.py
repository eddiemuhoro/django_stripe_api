from django.urls import path
from .views import CreateCheckoutSessionView, GetStripePublishableKeyView

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('config/', GetStripePublishableKeyView.as_view(), name='get-stripe-publishable-key'),
]