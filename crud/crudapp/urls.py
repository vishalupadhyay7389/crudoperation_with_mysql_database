from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/',views.show,name="show"),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
]