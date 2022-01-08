from django.urls import path
from webapp.views import (main_view,
                          create_guest_view,
                          update_guest_view,
                          delete_guest_view)

urlpatterns = [
    path('', main_view, name="main_page"),
    path('create_guest/', create_guest_view, name="guest_add"),
    path('<int:pk>/update/', update_guest_view, name="guest_update"),
    path('<int:pk>/delete/', delete_guest_view, name="guest_delete"),
    ]