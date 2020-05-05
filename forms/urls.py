from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base, name ='base'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
    path('view/<str:pk>/',views.view, name ='view')
]