"""
URL configuration for tradingDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

from . import views 
app_name = 'plan'


router = DefaultRouter()
router.register(r'info', views.InfoFormViewSet)
router.register(r'actual-returns', views.ActualReturnsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.homepag, name='homepag'),
    path('index', views.index, name='homepage'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.registerUser, name='register'),
    path('pricing.html', views.pricing, name='pricing'),
    path('stock-markets.html', views.stockMarkets, name='stock-markets'),
    path('trading-view.html', views.tradindViwe, name='trading-view'),
    path('journal-trades.html', views.journals, name='journal-trades'),
   # path('insert', views.insertData, name='insertData'),
   # path('delete/<id>/', views.delete_data, name="delete" ),
   # path('update/<id>/', views.update_data, name="update" ),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password" ),    
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_confirm.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   # path('adddata', views.addand, name='adddata'),
   # path('updatee', views.uppddaattee, name='updatte'),
    path('trading-business-plan.html', views.trading_business_plan, name='rading-business-plan'),
    #path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate,name="activate")
    
]

