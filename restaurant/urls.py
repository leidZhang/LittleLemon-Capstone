from . import views
from django.urls import path, include 
from rest_framework import routers 

router = routers.DefaultRouter() 
router.register(r'bookings', views.BookingViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', views.index, name='index'), 
    path('api/', include(router.urls)), 
    # path('menu/', views.MenuView.as_view(), name="menu-list"), 
    # path('menu/<int:pk>', views.SingleMenuView.as_view(), name="menu-item"), 
    # path('booking/', include(router.urls)) 
]