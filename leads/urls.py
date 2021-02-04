from django.urls import path
from .views import (
    home_view, 
    detail_lead, 
    create_lead, 
    update_lead,
    delete_lead,
    item_create, 
    item_list, 
    item_detail, 
    item_delete,


    InstanceDetail,
    InstanceItemDetail,
    InstanceListperUser,
)

urlpatterns = [
    path('', home_view, name="index"),
    path('create/', create_lead, name="create_leads"),
    path('<int:pk>/', detail_lead, name="detail_lead"),
    path('<int:pk>/update/', update_lead, name="update_lead"),
    path('<int:pk>/delete/', delete_lead, name="delete_lead"),
    path('items/', item_list, name="item_list"),


    path('instances/<int:pk>/', InstanceDetail.as_view(), name="instance_detail"),
    path('instances/<int:pk>/', InstanceItemDetail.as_view(), name="instance_detail2"),
    path('<int:user_id>/instances/',
         InstanceListperUser.as_view(), name="instance_list"),

]
