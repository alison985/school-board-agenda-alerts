from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from datetime import datetime
from urlparse import urljoin
import requests
import re

from schoolboardagendas.models import SchoolBoardAgendas
from schoolboardagendas.models import SchoolDistrict


url = 'https://meeting.nasbonline.org/public/Agency.aspx?PublicAgencyID=4397&agencytypeid=1'
header = {'User-Agent': 'Mozilla/5.0'}
words = ['bathroom', 'bathrooms', 'trans', 'transgender', 'locker room', 'locker rooms', 'shower', 'showers', 'gender',
         'restroom', 'restrooms']


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(url, headers=header)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        agenda_links = soup.find_all('a')

        for link in agenda_links:
            link_text = link.text
            date_match = re.search('(\d{2})[/.-](\d{2})[/.-](\d{4})', link_text)
            if date_match:
                time = re.search('(\d{1,2})[:](\d{2}) (AM|PM|am|pm)', link_text).group(0)

                words_in_match = []
                agenda_full_url = urljoin(url, link['href'])
                agenda_request = requests.get(agenda_full_url, headers=header)
                agenda_content = agenda_request.content.lower()

                for word in words:
                    match = re.search(r'\b{}\b'.format(word), agenda_content)
                    if match:
                        words_in_match.append(word)

                words_in_match_str = ','.join(words_in_match)
                date = date_match.group(0)
                agenda_datetime = datetime.strptime('{} {}'.format(date, time), '%m/%d/%Y %I:%M %p')

                school_district, created = SchoolDistrict.objects.get_or_create(
                    name='Omaha Public Schools Board',
                    defaults={
                        'url_to_scrape': url,
                        'mailing_city': 'Omaha',
                        'mailing_state': 'NE',
                        'can_parse': True,
                    }
                )

                SchoolBoardAgendas.objects.create(
                    school_district=school_district,
                    meeting_at=agenda_datetime,
                    link_to_agenda=agenda_full_url,
                    keyword_flag=True if words_in_match_str else False,
                    keywords=words_in_match
                    )
