from django.urls import path
from . import views
from .views import*

urlpatterns = [
    path('',views.upload_view, name='upload_image'),
    path('api/upload/', UploadImageView.as_view(), name='upload_image_api'),
    # Add more URLs as needed
]
