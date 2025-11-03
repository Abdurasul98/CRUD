from django.urls import path
from app1.views import *


urlpatterns = [
    path('',index,name='index'),
    path('category/<int:id>',category,name='category'),
    path('product/<int:id>',product,name='product'),
    path('employee/',employee,name='employee'),
    path('order/',order,name='order'),
    path('orderdetail/',orderdetail,name='orderdetail'),

    # path('addcategory/',addcategory,name='addcategory'),
    # path('addproduct/',addproduct,name='addproduct'),
    # path('addsupplier/',addemployee,name='addemployee'),
    # path('addorder/',addorder,name='addorder'),
    # path('addorderdetail/',addorderdetail,name='addorderdetail'),

    # path('deleteproduct/<int:id>',deleteproduct,name='deleteproduct'),
    # path('deletecategory/<int:id>',deletecategory,name='deletecategory'),
    # path('deleteorder/<int:id>',deleteorder,name='deleteorder'),
    # path('deleteorderdetail/<int:id>/',deleteorderdetail,name='deleteorderdetail'),
    # path('deletesupplier/<int:id>/',deleteemployee,name='deleteemployee'),


    # path('updateorder/<int:id>',updateorder,name='updateorder'),
    # path('updateorderdetail/<int:id>',updateorderdetail,name='updateorderdetail'),
    # path('updateproduct/<int:id>',updateproduct,name='updateproduct'),
    # path('updatecategory/<int:id>',updatecategory,name='updatecategory'),
    # path('updateemployee/<int:id>',updatemployee,name='updateemployee'),


    path('addcategory/',AddCategory.as_view(),name = 'addcategory'),
    path('addproduct/',AddProduct.as_view(),name = 'addproduct'),
    path('addorder/',AddOrder.as_view(),name = 'addorder'),
    path('addorderdetail/',AddOrderDetail.as_view(),name = 'addorderdetail'),
    path('addemployee/',AddEmployee.as_view(),name = 'addemployee'),

    path('updatecategory/<int:pk>/',UpdateCategory.as_view(),name = 'updatecategory'),
    path('updateproduct/<int:pk>/',UpdateProduct.as_view(),name = 'updateproduct'),
    path('updateorder/<int:pk>/',UpdateOrder.as_view(),name = 'updateorder'),
    path('updateorderdetail/<int:pk>/',UpdateOrderDetail.as_view(),name = 'updateorderdetail'),
    path('updateemployee/<int:pk>/',UpdateEmployee.as_view(),name = 'updateemployee'),

    path('deleteproduct/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct'),
    path('deletecategory/<int:pk>/', DeleteCategory.as_view(), name='deletecategory'),
    path('deleteorder/<int:pk>/', DeleteOrder.as_view(), name='deleteorder'),
    path('deleteorderdetail/<int:pk>/', DeleteOrderDetail.as_view(), name='deleteorderdetail'),
    path('deleteemployee/<int:pk>/', DeleteEmployee.as_view(), name='deleteemployee'),

    path('readproduct/<int:pk>/',ReadProduct.as_view(),name = 'product' ),
]
