from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
]
