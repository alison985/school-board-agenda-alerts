from schoolboardagendas.models import SchoolBoardAgendas
from schoolboardagendas.serializers import SchoolBoardAgendasSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from datetime import datetime 


now = datetime.now()

class SchoolBoardAgendasList(generics.ListCreateAPIView):
	queryset = SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	serializer_class = SchoolBoardAgendasSerializer
	model = SchoolBoardAgendas 
	permission_class = (AllowAny,)
	order_by = ('meeting_at')
def get_queryset(self,request):
	keyword_flag = request.query_params.get('keyword_flag',"True")
	if keyword_flag == "All":
		return SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	elif keyword_flag == "True":
		return SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day),keyword_flag=True)
	elif keyword_flag == "False":
		return SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day),keyword_flag=False)


class SchoolBoardAgendasLocationList(generics.ListCreateAPIView):
	queryset = SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	serializer_class = SchoolBoardAgendasSerializer
	model = SchoolBoardAgendas 
	permission_class = (AllowAny,)
	order_by = ('meeting_at')
def get_queryset(self,request,city,state):
	keyword_flag = request.query_params.get('keyword_flag',"True")
	queryset = SchoolBoardAgendas.objects.filter(meeting_at__gte=datetime(now.year,now.month,now.day))
	if keyword_flag == "All":
		queryset = queryset
	elif keyword_flag == "True":
		queryset = queryset.filter(keyword_flag=True)
	elif keyword_flag == "False":
		queryset = queryset.filter(keyword_flag=False)
	return queryset.filter(school_district__mailing_city__icontains=city,school_district__mailing_state__icontains=state)






class SchoolBoardAgendasDetail(generics.RetrieveAPIView):
	queryset = SchoolBoardAgendas.objects.all()
	serializer_class = SchoolBoardAgendasSerializer
	model = SchoolBoardAgendas 
	permission_class = (AllowAny,)