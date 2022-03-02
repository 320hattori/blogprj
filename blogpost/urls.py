from django.urls import path, include
from .views import BlogList,BlogDetail,BlogCreate

urlpatterns = [
    path('list/', BlogList.as_view(),name='list'),
    path('detail/<int:pk>', BlogDetail.as_view(),name='detail'),
    path('create/',BlogCreate.as_view(),name='create'),
]
