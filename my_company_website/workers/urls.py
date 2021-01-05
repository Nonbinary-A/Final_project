from django.urls import path, include
from . import views
from rest_framework import routers
app_name = 'workers' \
           ''
router = routers.DefaultRouter()
router.register('workers', views.WorkersView)

urlpatterns = [
    path('', views.workers_list, name='list'),
    path('json', include(router.urls)),
    path('<slug:slug>/', views.worker_detail, name='detail')
]
