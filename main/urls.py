from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # region
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    # category
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/category/list', views.categories, name='categories'),
    path('dashboard/category/update/<int:id>', views.update_category, name='update_category'),
    path('dashboard/category/delete/<int:id>', views.delete_category, name='delete_category'),
    # item 
    path('dashboard/items/create', views.create_item, name = 'create_item'),
    path('dashboard/items/list', views.items, name = 'items'),
    path('dashboard/items/update/<int:id>', views.update_item, name = 'update_item'),
    path('dashboard/items/delete/<int:id>', views.delete_item, name = 'delete_item'),
    # applications
    path('dashboard/applications/list', views.applications, name = 'applications'),
    path('dashboard/applications/details/<int:id>', views.update_checked, name = 'update_checked')


]