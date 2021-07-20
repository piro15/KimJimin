from django.urls import path
from . import views

app_name = 'devtools'

urlpatterns = [
    path('', views.tool_list, name='tool_list'),
    path('<int:pk>/', views.tool_detail, name='tool_detail'),
    path('create/', views.create_tool, name='create_tool'),
    path('<int:pk>/edit/', views.edit_tool, name='edit_tool'),
]
