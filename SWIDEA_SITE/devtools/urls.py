from django.urls import path
from . import views

app_name = 'devtools'

urlpatterns = [
    path('', views.tool_list, name='tool_list'),
    path('<int:pk>/', views.tool_detail, name='tool_detail'),
    path('create/', views.tool_create, name='tool_create'),
    path('<int:pk>/edit/', views.tool_edit, name='tool_edit'),
    path('<int:pk>/delete/', view=views.tool_delete, name='tool_delete'),
]
