from django.urls import path
from .views import *

urlpatterns = [
    path('', CNCIndex.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('cnc/<slug:cnc_slug>/', ShowCNC.as_view(), name='cnc'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='category'),
    path('add_cnc/', AddCNC.as_view(), name='add_cnc'),
    path('register/', Register.as_view(), name='register')
]