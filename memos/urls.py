from django.urls import path
from . import views

urlpatterns = [
    path('memos/', views.memo_list, name='memo_list'),
    path('memos/<int:pk>/', views.memo_detail, name='memo_detail'),
]
