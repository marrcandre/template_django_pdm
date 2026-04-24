from rest_framework.viewsets import ModelViewSet

from core.models import Freelance
from core.serializers import FreelanceSerializer


class FreelanceViewSet(ModelViewSet):
    queryset = Freelance.objects.all()
    serializer_class = FreelanceSerializer