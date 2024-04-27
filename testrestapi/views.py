import time
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
            print('----------------------------------------------------------------------------------')
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
        return redirect(reverse('testrestapi:result', kwargs={'pk1':instance.cad_num, 'pk2':instance.shirota, 'pk3':instance.dolgota}))
    else:
       
        form = RealEstForm()

    return render(request, 'testrestapi/templates/testrestapi/query.html', context) 

def result(request, **kwargs):
    cad_num=kwargs['pk1']
    shirota=kwargs['pk2']
    dolgota=kwargs['pk3']

    result = False
    try:
        reobject=RealEstateObject.objects.all().get(cad_num=cad_num, shirota=shirota, dolgota=dolgota)
        context = {
                'result':True
        }
        time.sleep(2)# Не обязательно все 60 сек ждать, достаточно 2
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
    except :
        print('----------------------------------------------------------------------------------')
        context = {
                'result':result
        }
    return render(request, 'testrestapi/templates/testrestapi/result.html', context)

def ping(request):
    
    page = requests.get(BASE_URL,'/emulate_server')
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