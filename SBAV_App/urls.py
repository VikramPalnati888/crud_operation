from django.urls import path
from SBAV_App.views import *

urlpatterns = [
    path('itemspost/', ItemsPost,name='items_post'),
    path('itemsget/', itemsGet,name='items_get'),
    path('itemsedit/<int:pk>/', itemsEdit,name='items_edit'),
    path('itemsdelete/<int:pk>/', itemsDelete,name='items_delete'),
]

