from django.urls import path
from .views import create_checkout_session, stripe_webhook, get_stripe_public_key

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('config/', get_stripe_public_key, name='get-stripe-public-key'),
]