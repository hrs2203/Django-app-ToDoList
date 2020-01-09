from django.urls import path , include
from todo import views

urlpatterns = [
    path('' , views.homepage),
    path('login/', views.login_request ),
    path('logout/' , views.logout_request),
    path('register/' , views.register_request),
    path("account/" , views.account_details),
    path('add_task/', views.add_new_task),
    path('add_task_type/', views.add_new_task_type),
    path('delete_task/',views.delete_task),
    path('edit_task/', views.edit_task)
]
