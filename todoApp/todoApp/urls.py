from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('todo/', include('todo.urls')),
    path('', include('mainApp.urls')),
    path('sendMail/', include('sendMail.urls')), 
]
