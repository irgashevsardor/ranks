import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.conf import settings
from django.http import JsonResponse
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

DOMAIN = 'http://127.0.0.1:8000/'


@csrf_exempt
def create_checkout_session(request, pk):
    if request.method == 'GET':
        try:
            item = Item.objects.get(id=pk)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': item.name,
                            },
                            'unit_amount': int(item.price * 100),
                        },
                        'quantity': 1,
                    }],
                mode='payment',

                success_url=DOMAIN + '/success',
                cancel_url=DOMAIN + '/cancel',
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemDetailView(DetailView):
    model = Item
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
