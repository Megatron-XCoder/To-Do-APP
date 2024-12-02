from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.shortcuts import render

# API to create a new todo item
class TodoItemCreate(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

# API to read a single todo item
class TodoItemDetail(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

# API to read all todo items
class TodoItemList(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

# API to update an existing todo item
class TodoItemUpdate(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

# API to delete a todo item
class TodoItemDelete(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    permission_classes = [IsAuthenticated]

def homepage(request):
    return render(request, 'index.html')  # Make sure the template is in the correct directory