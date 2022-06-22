from itertools import product
import profile
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('order/',views.ordering,name="ordering"),
    
    path('product/',views.producting,name="producting"),
    path('profile/<int:id>',views.profiling,name="profiling"),
    path('staff/',views.staffing,name="staffing"),
    path('staff_index/',views.staff_index,name="staff_index"),
    path('delete/<int:id>',views.delete, name="delete")
]