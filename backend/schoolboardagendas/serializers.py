from rest_framework import serializers 
from schoolboardagendas.models import *


class SchoolDistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchoolDistrict
		fields = ('name','mailing_city','mailing_state')

class SchoolBoardAgendasSerializer(serializers.ModelSerializer):
	school_district = SchoolDistrictSerializer(read_only=True)
	class Meta:
		model = SchoolBoardAgendas 
		fields = ('school_district','meeting_at','link_to_agenda','keyword_flag','keywords')

