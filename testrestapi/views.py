import json
import os
import time
import django
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


def home(request, cad_num, shirota, dolgota):# Этот ендпоинт просто существует
        
        reobject = 'Nothing'
        try:
            reobject=RealEstateObject.objects.all().get(cad_num=cad_num, shirota=shirota, dolgota=dolgota)
            context = {
                'reobject':reobject
        
        }
            time.sleep(7)# Не обязательно все 60 сек ждать, достаточно 7
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
        except :
            print('--------------------------------------------iiii--------------------------------------')
            context = {
                'reobject':reobject
        }
          
        return render(request, 'testrestapi/templates/testrestapi/home.html', context) 
       
    
def query(request):
    form = RealEstForm(request.POST)
  
    context = {
        'form':form
    }
    if request.method == "POST":   
        if form.is_valid():
            print('jjjjjjjjjjjjjjjjjjjjjjjjj')
            cad_num_form_value = form.cleaned_data['cad_num']
            shirota_form_value = form.cleaned_data['shirota']
            dolgota_form_value = form.cleaned_data['dolgota']
            instance = HistoryApi.objects.create(cad_num=cad_num_form_value, shirota=shirota_form_value, dolgota=dolgota_form_value)
            instance.save()
             #<a class="btn.btn-default" href="{% url 'musiclib:cutter_file' object.pk request_user_id %}" >Обрезка трека</a>
             #path('cutter_file/<int:pk1>/<int:pk2>', cutter_file, name='cutter_file'),

            print('cad_num', instance.cad_num, 'shirota', instance.shirota, 'dolgota', instance.dolgota)
            ## Здесь нельзя редиректом, надо апи реквестом запрашивать
        return redirect(reverse('testrestapi:result', kwargs={'pk1':instance.cad_num, 'pk2':instance.shirota, 'pk3':instance.dolgota}))
    else:
       
        form = RealEstForm()

    return render(request, 'testrestapi/templates/testrestapi/query.html', context) 

def result(request, **kwargs):
    cad_num=kwargs['pk1']
    shirota=kwargs['pk2']
    dolgota=kwargs['pk3']
    
    result = False
    print('request.content1', request.META['CONTENT_TYPE'])#<class 'django.core.handlers.wsgi.WSGIRequest'>##equest.META['CONTENT_TYPE'] text/plain
    # url = os.path.join(BASE_URL,'/emulate_server')
    url = 'http://localhost:8002'
    # response = requests.get(url)
    data = {
    "cad_num": cad_num,
    "shirota": shirota,
    "dolgota": dolgota,
}   
    # response = requests.get(url)
    # my_csrf_token = request.META['HTTP_COOKIE']
    # clear_token = re.compile("=(.*)")
    # clear_token = clear_token.findall(my_csrf_token)[0]
    response = requests.post(url, params=data)#, headers={ 'X-CSRFToken': clear_token})
    # print('response.headers', response_get.headers)
    print('request.META', request.META['HTTP_COOKIE'])
    # print(clear_token)
    print(response)

    # print(request.COOKIES.get('XSRF-TOKEN'))
    # print(django.middleware.csrf.get_token(request)
    
    # print(response_get.cookies['HTTP_COOKIE'])
    # headers = {'X-CSRFToken': csrf_token}
    # print('response.headers', response.headers)# response.headers {'Date': 'Mon, 29 Apr 2024 03:27:48 GMT', 'Server': 'WSGIServer/0.2 CPython/3.10.5', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Vary': 'Cookie', 'Content-Length': '1455', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 'same-origin', 'Set-Cookie': 'csrftoken=eqFVnpaPL9hU1CyHQEVwOqcSKmvuhx10; expires=Mon, 28 Apr 2025 03:27:48 GMT; Max-Age=31449600; Path=/; SameSite=Lax'}

    # headers = {'Content-type': 'application/json'}
    # r = requests.get(url, headers=headers)

    # print('type(response)', type(response))
    
    context = {
                'result':result
        }
    return render(request, 'testrestapi/templates/testrestapi/result.html', context)

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