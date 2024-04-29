import os
from django.core.management import BaseCommand
import requests

from config.settings import BASE_URL
from rest_framework.authtoken.models import Token

class Command(BaseCommand):

    def handle(self, *args, **options):
        

        # token = Token.objects.create(user=request.user)
        # print(token.key)
        print(os.path.join(BASE_URL,'/emulate_server'))
        print(f'{BASE_URL}/emulate_server')

        
        # response = requests.get(f"{BASE_URL}?cad_num=23&shirota=25&dolgota=55")
        # print(response.json())
        # print(BASE_URL)
     