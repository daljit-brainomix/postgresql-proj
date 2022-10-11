from django.urls import path

from .views import (
    DogCreate,
    ContactView,
    JSONListView,
    JSONDetailView,
    JSONUpdate,
    JSONDelete,
)

urlpatterns = [
    path("", JSONListView.as_view(), name="doglist"),
    path("dogDetail/<int:pk>/", JSONDetailView.as_view(), name="dog-detail"),
    path("dogUpdate/<int:pk>/", JSONUpdate.as_view(), name="dog-update"),
    path("dogDelete/<int:pk>/", JSONDelete.as_view(), name="dog-delete"),
    path("dog/", ContactView.as_view(), name="dogform"),
    path("newdog/", DogCreate.as_view(), name="dognew"),
]
