from __future__ import unicode_literals

from django.db import models


class SchoolDistrict(models.Model):
	name = models.CharField(max_length=255)
	url_to_scrape = models.TextField()
	grade_levels = models.CharField(max_length=50, null=True)
	mailing_city = models.CharField(max_length=60)
	mailing_state = models.CharField(max_length=2)
	district_number = models.CharField(max_length=4, null=True)
	can_parse = models.BooleanField(default=False)
	ever_matched_keywords = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add =True)
	modified_at = models.DateTimeField(auto_now=True)

class Agendas(models.Model):
	school_district = models.ForeignKey(SchoolDistrict)
	meeting_at = models.DateTimeField()
	link_to_agenda = models.TextField()
	keyword_flag = models.BooleanField()
	keywords = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)




