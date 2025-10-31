from django.urls import path
from app1.views import *


urlpatterns = [
    path('',index,name='index'),
    path('category/<int:id>',category,name='category'),
    path('product/<int:id>',product,name='product'),
    path('employee/',employee,name='employee'),
    path('order/',order,name='order'),
    path('orderdetail/',orderdetail,name='orderdetail'),

    path('addcategory/',addcategory,name='addcategory'),
    path('addproduct/',addproduct,name='addproduct'),
    path('addsupplier/',addemployee,name='addemployee'),
    path('addorder/',addorder,name='addorder'),
    path('addorderdetail/',addorderdetail,name='addorderdetail'),

    path('deleteproduct/<int:id>',deleteproduct,name='deleteproduct'),
    path('deletecategory/<int:id>',deletecategory,name='deletecategory'),
    path('deleteorder/<int:id>',deleteorder,name='deleteorder'),
    path('deleteorderdetail/<int:id>/',deleteorderdetail,name='deleteorderdetail'),
    path('deletesupplier/<int:id>/',deleteemployee,name='deleteemployee'),


    path('updateorder/<int:id>',updateorder,name='updateorder'),
    path('updateorderdetail/<int:id>',updateorderdetail,name='updateorderdetail'),
    path('updateproduct/<int:id>',updateproduct,name='updateproduct'),
    path('updatecategory/<int:id>',updatecategory,name='updatecategory'),
    path('updateemployee/<int:id>',updatemployee,name='updateemployee'),
]
