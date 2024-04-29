import json
import os
import re
import time
import django
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.settings import BASE_URL
from testrestapi2.forms import RealEstForm
from testrestapi.models import RealEstateObject
from testrestapi.serializers import RealEstateObject, RealEstateObjectSerilizer
from django.shortcuts import redirect, render, reverse
import requests
from testrestapi2.models import HistoryApi
from django.views.decorators.csrf import csrf_exempt


# def home(request, cad_num, shirota, dolgota):# Этот ендпоинт просто существует
        
#         reobject = 'Nothing'
#         try:
#             reobject=RealEstateObject.objects.all().get(cad_num=cad_num, shirota=shirota, dolgota=dolgota)
#             context = {
#                 'reobject':reobject
        
#         }
#             time.sleep(7)# Не обязательно все 60 сек ждать, достаточно 7
#             print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
#         except :
#             print('--------------------------------------------iiii--------------------------------------')
#             context = {
#                 'reobject':reobject
#         }
          
#         return render(request, 'testrestapi/templates/testrestapi/home.html', context) 
       
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
            # print('response.headers', response_get.headers)
            # print("==========================request", result,request.META)
            # print('response.text==============================8888', response.text)
            # print('response', response) 

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

# def result(request, **kwargs):
#     cad_num=kwargs['pk1']
#     shirota=kwargs['pk2']
#     dolgota=kwargs['pk3']
    
#     result = False
#     # print('request.content1', request.META['CONTENT_TYPE'])#<class 'django.core.handlers.wsgi.WSGIRequest'>##equest.META['CONTENT_TYPE'] text/plain
#     # url = os.path.join(BASE_URL,'/emulate_server')
#     url = 'http://localhost:8002'
#     # response = requests.get(url)
#     data = {
#     "cad_num": cad_num,
#     "shirota": shirota,
#     "dolgota": dolgota,
# }   
#     # response = requests.get(url)
#     # my_csrf_token = request.META['HTTP_COOKIE']
#     # clear_token = re.compile("=(.*)")
#     # clear_token = clear_token.findall(my_csrf_token)[0]
#     response = requests.post(url, params=data)#, headers={ 'X-CSRFToken': clear_token})
#     # print('response.headers', response_get.headers)
#     print('request.META', request.META['HTTP_COOKIE'])
#     # print(clear_token)
#     print(response)

#     # print(request.COOKIES.get('XSRF-TOKEN'))
#     # print(django.middleware.csrf.get_token(request)
    
#     # print(response_get.cookies['HTTP_COOKIE'])
#     # headers = {'X-CSRFToken': csrf_token}
#     # print('response.headers', response.headers)# response.headers {'Date': 'Mon, 29 Apr 2024 03:27:48 GMT', 'Server': 'WSGIServer/0.2 CPython/3.10.5', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Vary': 'Cookie', 'Content-Length': '1455', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 'same-origin', 'Set-Cookie': 'csrftoken=eqFVnpaPL9hU1CyHQEVwOqcSKmvuhx10; expires=Mon, 28 Apr 2025 03:27:48 GMT; Max-Age=31449600; Path=/; SameSite=Lax'}

#     # headers = {'Content-type': 'application/json'}
#     # r = requests.get(url, headers=headers)

#     # print('type(response)', type(response))
    
#     context = {
#                 'result':result
#         }
#     time.sleep(10)
#     return render(request, 'testrestapi/templates/testrestapi/result.html', context)

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

from django.views.decorators.csrf import csrf_exempt
import requests

def values_to_param(filter_query, param):
    
    param = re.compile(f"{param}=(.*)")
    param = param.findall(filter_query)
    return param[0]
    
# @csrf_exempt
# def receive(request, **kwargs):
#     # cad_num=kwargs['pk1']
#     # shirota=kwargs['pk2']
#     # dolgota=kwargs['pk3']
#     print('request.content1', request.META)
#     result = 'Прошли черерз receive'
#     context = {
#                 'result':result
#         }
    
#     # response = requests.post(url, params=data)#, headers={ 'X-CSRFToken': clear_token})
#     # print('response.headers', response_get.headers)
#     # print('request.META', request.META['HTTP_COOKIE'])
#     # data = json.dumps(result)
#     # print('filter_query_all', filter_query_all, 'filter_lst', filter_lst)
#     # print('result', result)
#     print('request.__dict__', request.__dict__)
#     print("request.META['QUERY_STRING']", request.META['QUERY_STRING'])
#     filter_query = request.META['QUERY_STRING']
#     result='result'
#     result = values_to_param(filter_query,result)
#     print(filter_query)
#     print('result==========', result)
#     return render(request, 'testrestapi/templates/testrestapi/result.html', context)
    # return redirect(reverse('testrestapi:result/<int:pk1>/<int:pk2>/<int:pk3>'), kwargs={'result':result})
    # return HttpResponse(data, content_type='json')
    # return render(request, 'testrestapi/templates/testrestapi/result.html', context)
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
