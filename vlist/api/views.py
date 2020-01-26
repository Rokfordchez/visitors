from rest_framework import viewsets
from .serializers import UListSerializer
from vlist.models import UList


class UListViewSet(viewsets.ModelViewSet):
    queryset = UList.objects.all()
    serializer_class = UListSerializer
