from rest_framework import serializers 
from schoolboardagendas.models import SchoolBoardAgendas


class SchoolBoardAgendasSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchoolBoardAgendas 
		fields = '__all__'
