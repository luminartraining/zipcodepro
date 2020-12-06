from django.shortcuts import render
# Create your views here.
import pandas as pd
# BASE_DIR = Path(__file__).resolve().parent.parent

from rest_framework.response import Response
from django.http import JsonResponse

def get_data_frame():
    df = pd.read_csv("api/static/uszips.csv")
    return df
     # all zip code in json format




from rest_framework.views import APIView
from rest_framework.response import Response

class ZipCodes(APIView):
    def get(self, request, format=None):
        df=get_data_frame()
        zipcodes = df['zip']
        zip_data = zipcodes.to_json()

        return JsonResponse(zip_data,safe=False)

#
class ZipCodeDetails(APIView):

    def get(self, request, pk, format=None):
        df=get_data_frame()
        zip_code_row = df.loc[df['zip'] == 601]
        zip_code_row_data = zip_code_row.to_json()
        return JsonResponse(zip_code_row_data, safe=False)


