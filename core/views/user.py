from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Endpoint para listar, criar, editar e deletar usuários."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(RetrieveAPIView):
    """Endpoint para retornar o usuário autenticado."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
