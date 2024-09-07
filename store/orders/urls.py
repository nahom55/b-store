from django.urls import path

from .views import OrdersPageView, charge

urlpatterns = [

        path('charge/', charge, name='charge'),
        path('', OrdersPageView.as_view(), name='orders'),
        path('purchase/', OrdersPageView.as_view(), name='purchase'),
    ]
