from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoatSerializer
from .models import Boat
from django.http import HttpResponse
from django.http import JsonResponse


class BoatView(viewsets.ModelViewSet):
    serializer_class = BoatSerializer
    queryset = Boat.objects.all()


def search_by_city(request, parameter):
    status = "success"
    error = None
    
    data = {
        "status": status,
        "boats": [
            {
                "link": "https://blabla",
                "title": parameter,
                "price": "123€",
            },
        ],
        "error": error
    }

    return JsonResponse(data)
