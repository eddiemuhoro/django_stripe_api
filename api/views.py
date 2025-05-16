from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateCheckoutSessionSerializer
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
class CreateCheckoutSessionView(APIView):
    def post(self, request):
        serializer = CreateCheckoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[{
                        'price_data': {
                            'currency': serializer.validated_data['currency'],
                            'product_data': {
                                'name': 'Sample Product',
                            },
                            'unit_amount': serializer.validated_data['amount'],
                        },
                        'quantity': 1,
                    }],
                    mode='payment',
                    success_url=serializer.validated_data['success_url'],
                    cancel_url=serializer.validated_data['cancel_url'],
                )
                return Response({'sessionId': checkout_session.id})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#config route to get stripe publishable key
class GetStripePublishableKeyView(APIView):
    def get(self, request):
        return Response({'publishableKey': settings.STRIPE_PUBLISHABLE_KEY})
