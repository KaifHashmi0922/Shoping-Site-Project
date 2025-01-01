
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from  .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/',views.cart_view,name='cart'),
    path('profile/',views.profile_view,name='profile'),
    # path('viewproduct/',views.view_product,name='viewproduct'),
    # path('password_change/<id>',views.edit_password,name='password_change'),
    path('guest/',views.login,name='login'),
    path('shoping/<id>',views.shop,name='shoping'),
    path('toggle/',views.toggle_view,name='toggle'),
    path('check/',views.show,name='check')  ,
    path('update_cust/<id>',views.Cust_update,name='update_cust'),
     path('delete_img/<id>',views.image_delete,name='delete_img'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

