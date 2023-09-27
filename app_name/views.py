from .image_processing import process_image
from django.http import JsonResponse
import os
from django.shortcuts import render
from .forms import UploadImageForm
import cv2
import numpy as np

def upload_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

            # Perform image processing to get the RGB values

            color_values = {
                'URO': [206, 193, 187],
                'BIL': [202, 185, 164],
                'KET': [193, 171, 153],
                'BLD': [204, 159, 54],
                'PRO': [191, 172, 130],
                'NIT': [203, 189, 170],
                'LEU': [194, 175, 164],
                'GLU': [128, 173, 163],
                'SG': [191, 159, 76],
                'PH': [206, 152, 106]
            }

            return JsonResponse(color_values)
    else:
        form = UploadImageForm()

    return render(request, 'app_name/upload.html', {'form': form})
# app_name/views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UploadImageSerializer
class UploadImageView(APIView):
    def get(self, request):
        return Response({"message": "This is a custom message for GET requests."})
    def post(self, request):
        serializer = UploadImageSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_image = serializer.validated_data['image']

            # Perform image processing here

            color_values = {
                'URO': [206, 193, 187],
                'BIL': [202, 185, 164],
                'KET': [193, 171, 153],
                'BLD': [204, 159, 54],
                'PRO': [191, 172, 130],
                'NIT': [203, 189, 170],
                'LEU': [194, 175, 164],
                'GLU': [128, 173, 163],
                'SG': [191, 159, 76],
                'PH': [206, 152, 106]
            }

            return Response(color_values, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
