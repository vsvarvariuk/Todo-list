from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from todo_service.models import Task, Tag


def toggle_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))

class TaskListView(generic.ListView):
    model = Task
    template_name = "service/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("service/task_list.html")
    template_name = "service/task_create.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "service/task_update.html"
    success_url = reverse_lazy("service/task_list.html")



class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "service/task_delete.html"
    success_url = reverse_lazy("service/task_list.html")


class TagListView(generic.ListView):
    model = Tag
    template_name = "service/tag_list.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "service/tag_update.html"
    success_url = reverse_lazy("service/tag_list.html")


class TagDeleteView(generic.DeleteView):
    model = Task
    template_name = "service/tag_delete.html"
    success_url = reverse_lazy("service/tag_list.html")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("service/tag_list.html")
    template_name = "service/tag_create.html"