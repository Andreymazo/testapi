import json
import os
import re
import time
import django
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.settings import BASE_URL
from testrestapi2.forms import RealEstForm
from django.shortcuts import render
import requests
from testrestapi2.models import HistoryApi
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt   
def query(request):
    form = RealEstForm(request.POST)
  
    context = {
        'form':form
    }
    if request.method == "POST":   
        if form.is_valid():
            instance = form.save(commit=False)
            print('jjjjjjjjjjjjjjjjjjjjjjjjj')
            cad_num_form_value = form.cleaned_data['cad_num']
            shirota_form_value = form.cleaned_data['shirota']
            dolgota_form_value = form.cleaned_data['dolgota']
            # instance = HistoryApi.objects.create(cad_num=cad_num_form_value, shirota=shirota_form_value, dolgota=dolgota_form_value)
            result = False
            url = 'http://localhost:8002'
            data = {
            "cad_num": cad_num_form_value,
            "shirota": shirota_form_value,
            "dolgota": dolgota_form_value,
            }
            response = requests.post(url, params=data)#, headers={ 'X-CSRFToken': clear_token})
          

            time.sleep(2)
            print('response.text', response.text)
            if response.text=='false':
                result=False
            if response.text=='true':
                result=True
            context = {
        'form':form,
        'result':response.text
    }
            instance = HistoryApi.objects.create(cad_num=cad_num_form_value, shirota=shirota_form_value, dolgota=dolgota_form_value, result=result)
            instance.save()
           
        return render(request, 'testrestapi/templates/testrestapi/query.html', context) 
    else:
       
        form = RealEstForm()

    return render(request, 'testrestapi/templates/testrestapi/query.html', context) 

def ping(request):
    # url = f'{BASE_URL}/emulate_server'
    url = 'http://127.0.0.1:8002/'
    page = requests.get(url)
    context = {
        'status_code':page.status_code
    }
    return render(request, 'testrestapi/templates/testrestapi/ping.html', context)

def history(request):
    queryset = HistoryApi.objects.all()
    context = {
        'queryset': queryset
    }
    return render (request, 'testrestapi/templates/testrestapi/history.html', context)

def values_to_param(filter_query, param):
    
    param = re.compile(f"{param}=(.*)")
    param = param.findall(filter_query)
    return param[0]
