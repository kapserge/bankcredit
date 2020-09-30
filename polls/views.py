from django.http import HttpResponse
from django.template import loader

import pandas as pd 
import json


def index(request):
    
    df = pd.read_csv("polls/random_forest_baseline.csv",nrows=10)
    template = loader.get_template('polls/index.html')
    
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data} 
    return HttpResponse(template.render(context, request))