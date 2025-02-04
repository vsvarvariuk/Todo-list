from django.urls import path
from todo_service.views import (TaskListView,
                                TaskCreateView,
                                TaskUpdateView,
                                TaskDeleteView,
                                TagListView,
                                TagUpdateView,
                                TagDeleteView,
                                TagCreateView, toggle_task_status)

urlpatterns = [

    path("change-status/<int:task_id>/",toggle_task_status,name="toggle-task-status"),
    path("",TaskListView.as_view(),name="task-list"),
    path("create-task/",TaskCreateView.as_view(),name="task-create"),
    path("update-task/<int:pk>/",TaskUpdateView.as_view(),name="task-update"),
    path("delete-task/<int:pk>/",TaskDeleteView.as_view(),name="task-delete"),
    path("tag-list/",TagListView.as_view(),name="tag-list"),
    path("tag-update/<int:pk>/",TagUpdateView.as_view(),name="tag-update"),
    path("tag-delete/<int:pk>/",TagDeleteView.as_view(),name="tag-delete"),
    path("tag-create/",TagCreateView.as_view(),name="tag-create")
]
app_name = "Todo"