"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='homepage'),
    path('admin/', admin.site.urls),
    path('api/todo/', views.TodoItemList.as_view(), name='todo-list'),  # Read all todo items
    path('api/todo/create/', views.TodoItemCreate.as_view(), name='todo-create'),  # Create a todo item
    path('api/todo/<int:pk>/', views.TodoItemDetail.as_view(), name='todo-detail'),  # Read one todo item
    path('api/todo/<int:pk>/update/', views.TodoItemUpdate.as_view(), name='todo-update'),  # Update a todo item
    path('api/todo/<int:pk>/delete/', views.TodoItemDelete.as_view(), name='todo-delete'),  # Delete a todo item
]