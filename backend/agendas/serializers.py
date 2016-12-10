from rest_framework import serializers 
from agendas.models import Agendas


class AgendasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Agendas 
		fields = '__all__'
