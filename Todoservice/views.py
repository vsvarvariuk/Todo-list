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


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "service/task_update.html"
    success_url = reverse_lazy("service/list_task.html")



class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "service/task_delete.html"
    success_url = reverse_lazy("service/list_task.html")