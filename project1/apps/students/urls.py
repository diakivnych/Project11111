from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_users, name = 'all_users'),
    path('new_user', views.add_user, name = 'add_user'),
    path('author', views.author, name = 'author'),
    path('leave_comment/<int:user_id>', views.leave_comment, name = 'leave_comment')
]