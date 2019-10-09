from django.urls import include, path
from django.contrib import admin
from event import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('event.urls')),
    path('', views.EventList.as_view(), name='event_list'),
    path('new/', views.EventCreate.as_view(), name='event_new'),
    path('<int:pk>/edit/', views.EventUpdate.as_view(), name='event_edit'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]
