from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_view, name='upload_view'),
    # Add more URLs as needed
]
