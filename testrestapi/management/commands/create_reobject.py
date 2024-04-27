from django.core.management import BaseCommand

from testrestapi.models import RealEstateObject


class Command(BaseCommand):

    def handle(self, *args, **options):
        RealEstateObject
        dict_for_fillin = [{'cad_num': 23, 'shirota': 25, 'dolgota': 55}, {'cad_num': 123, 'shirota': 125, 'dolgota': 155}]
        for i in dict_for_fillin:
        
            ff = RealEstateObject.objects.create(cad_num=i['cad_num'], shirota=i['shirota'], dolgota=i['dolgota'])
            ff.save()
  

