from django.urls import path
from .views import create_checkout_session, ItemDetailView

urlpatterns = [
    path('buy/<int:pk>', create_checkout_session, name='checkout-session'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item-detail-page'),
]
