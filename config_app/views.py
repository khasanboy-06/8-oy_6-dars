
from .serializers import HududSerializer, QurilishbinosiSerializer, Qurilish_tashkilotiSerializer
from .models import Hudud, Qurilish_binosi, Qurilish_tashkiloti
from .permissions import HududPermission, QurilishBinosiPermission, QurilishTashkilotiPermission

from rest_framework.viewsets import ModelViewSet



class HududAPIView(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [HududPermission]

class QurilishBinosiAPIView(ModelViewSet):
    queryset = Qurilish_binosi.objects.all()
    serializer_class = QurilishbinosiSerializer
    permission_classes = [QurilishBinosiPermission]


class QurilishTashkilotiAPIView(ModelViewSet):
    queryset = Qurilish_tashkiloti.objects.all()
    serializer_class = Qurilish_tashkilotiSerializer
    permission_classes = [QurilishTashkilotiPermission]