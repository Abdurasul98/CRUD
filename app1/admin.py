from django.contrib import admin
from app1.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    list_display_links = ['category_name']
    search_fields = ['category_name']
    last_editable = []


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','unit_price']
    list_display_links = ['unit_price']
    search_fields = ['product_name']
    last_editable = []


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date','required_date','shipped_date']
    list_display_links = ['required_date','shipped_date']
    search_fields = ['order_date']
    last_editable = []


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['unit_price','quantity']
    list_display_links = []
    search_fields = ['unit_price']
    last_editable = []


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name','title','title_of_courtesy','birth_date','hire_date','address','city','region','postal_code','country','home_phone','extension','notes','reports_to','phone_path']
    list_display_links = ['last_name','address']
    search_fields = ['first_name']
    last_editable = []


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(Employee,EmployeeAdmin)