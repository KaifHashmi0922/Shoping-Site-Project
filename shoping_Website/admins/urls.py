from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from  .import views
urlpatterns = [
    # path('',views.home_view,name='home'),
    path('adminslogin/',views.admin_login,name='adminslogin'),
    path('',views.dashbord_view,name='dashbord'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('admins_viewproduct/',views.admin_viewproduct,name='admins_viewproduct'),
    path('addcategorys/',views.addcategory_view,name='addcategorys'),
    path('view_categorys/',views.category_view,name='view_categorys'),
    path('view_custmers/',views.view_custmer,name='view_custmers'),
    # path('question/',views.question,name='question'),
    path('category_edit/<id>',views.edit_category,name='category_edit'),
    path('category_delete/<id>',views.delete_category,name='category_delete'),
    path('product_edit/<id>',views.edit_product,name='product_edit'),
    path('product_delete/<id>',views.delete_product,name='product_delete'),
    path('addcompanys/',views.add_comp,name='addcompanys'),
    path('view_companys/',views.company_view,name='view_companys'),
    path('company_edit/<id>',views.edit_company,name='company_edit'),
    path('company_delete/<id>',views.delete_company,name='company_delete'),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    
    