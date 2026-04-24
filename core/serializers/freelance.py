from rest_framework.serializers import ModelSerializer

from core.models import Freelance


class FreelanceSerializer(ModelSerializer):
    class Meta:
        model = Freelance
        fields = '__all__'