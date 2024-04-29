from django.urls import path
from config import settings
from testrestapi.apps import TestrestapiConfig
# from testrestapi.views import CustomLoginView, home, cutter_file, signup_without_confirmation, upload
from django.conf.urls.static import static
from testrestapi.views import history, ping, query#, receive#, result home,


app_name = TestrestapiConfig.name

urlpatterns = [
   
    path('', query, name='query'),
    # path('result/<int:pk1>/<int:pk2>/<int:pk3>', result, name='result'),
    path('ping', ping, name='ping'),
    path('history', history, name='history'),
    # path('emulate_server', home, name='home'),
    # path('receive', receive, name='receive'),
    
#     “/result" - для отправки результата
# "/ping" - проверка, что  сервер запустился
# “/history” - для получения истории запросов

  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

