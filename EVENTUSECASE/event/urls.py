from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('new/', views.EventCreate.as_view(), name='event_new'),
    path('<int:pk>/edit/', views.EventUpdate.as_view(), name='event_edit'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]
