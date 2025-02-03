from django.urls import path
from Todoservice.views import (TaskListView,
                               TaskCreateView,
                               TaskUpdateView,
                               TaskDeleteView)

urlpatterns = [

    path("",TaskListView.as_view(),name="task-list"),
    path("create-task/",TaskCreateView.as_view(),name="task-create"),
    path("update-task/<int:pk>/",TaskUpdateView.as_view(),name="task-update"),
    path("delete-task/<int:pk>/",TaskDeleteView.as_view(),name="task-delete")
]
app_name = "Todo"