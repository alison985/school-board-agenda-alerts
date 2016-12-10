from agendas.models import Agendas
from agendas.serializers import AgendasSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
import datetime 


class AgendasList(generics.ListCreateAPIView):
	queryset = Agendas.objects.filter(meeting_at__gte=datetime.date.now)
	serializer_class = AgendasSerializer
	model = Agendas 
	permission_class = (AllowAny,)
	order_by = ('meeting_at')

class AgendasDetail(generics.RetrieveAPIView):
	queryset = Agendas.objects.all()
	serializer_class = AgendasSerializer
	model = Agendas 
	permission_class = (AllowAny,)