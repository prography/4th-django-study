# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views as menu_views
from order import views as order_views
from kakao import views as kakao_views
from kakao import kakaopay as kakaopay
from rest_auth.views import LogoutView


router = DefaultRouter()
router.register(r'menu', menu_views.MenuViewSet)
router.register(r'order', order_views.OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/kakao/', kakao_views.KakaoLogin.as_view(), name='kakao_login'),
    # path('accounts/kakao/login/', order_views.oauthCode),
    # path('accounts/kakao/login/callback/', order_views.oauthCodeCallback),
    # path('accounts/kakao/logout/', order_views.oauthLogOut),
    # path('accounts/kakao/check/', order_views.oauthLogOut),
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('pay/', kakaopay.Pay, name='kakao_pay'),
    path('check/', kakaopay.Check, name='kakao_check'),
]

