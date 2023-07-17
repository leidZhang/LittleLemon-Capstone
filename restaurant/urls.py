from . import views
from django.urls import path, include 
from rest_framework import routers 

router = routers.DefaultRouter() 
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'), 
    path('menu/', views.MenuView.as_view(), name="menu-list"), 
    path('menu/<int:pk>', views.SingleMenuView.as_view(), name="menu-detail"), 
    path('booking/', include(router.urls)) 
]