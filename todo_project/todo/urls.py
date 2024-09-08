from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/update/<int:id>/', views.update_todo, name='update_todo'),
    path('todos/delete/<int:id>/', views.delete_todo, name='delete_todo'),
]
