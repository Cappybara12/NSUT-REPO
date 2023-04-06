from rest_framework.response import Response
# from rest_flex_fields import FlexFieldsModelViewSet
from .serializers import UserViewSerializer
from rest_framework.viewsets import ModelViewSet
from asToken.authentication import MultiTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from signin.models import AsUser
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    serializer_class = UserViewSerializer
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    queryset = AsUser.objects.all()
    filterset_fields = ['id',]

    def get_queryset(self):
        if self.kwargs.get('pk') not in [None,'',0]:
            filteredUser = AsUser.objects.filter(id=self.kwargs.get('pk'))
            return filteredUser


