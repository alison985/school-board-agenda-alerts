from agendas.models import Agendas
from agendas.serializers import AgendasSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from datetime import datetime 


now = datetime.now()

class AgendasList(generics.ListCreateAPIView):
	queryset = Agendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	serializer_class = AgendasSerializer
	model = Agendas 
	permission_class = (AllowAny,)
	order_by = ('meeting_at')
	
def get_queryset(self,request):
	keyword_flag = request.query_params.get('keyword_flag',"True")
	if keyword_flag == "All":
		return Agendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	elif keyword_flag == "True":
		return Agendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day),keyword_flag=True)
	elif keyword_flag == "False":
		return Agendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day),keyword_flag=False)



class AgendasDetail(generics.RetrieveAPIView):
	queryset = Agendas.objects.all()
	serializer_class = AgendasSerializer
	model = Agendas 
	permission_class = (AllowAny,)