from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task

class TaskListView(generic.ListView):
    model = Task
    template_name = "service/list_task.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("service/list_task.html")
    template_name = "service/task_create.html"
