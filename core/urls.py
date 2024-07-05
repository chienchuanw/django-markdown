from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/<slug:slug>/", views.display_post, name="detail"),
]
