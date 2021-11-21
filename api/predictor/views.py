from django.shortcuts import redirect, render
from django.http import HttpResponse
from .apps import PredictorConfig
from .models import approvals

def home(request):
                 
                                      if request.method == 'GET':
                                           return render (request,'predictor/home.html')      
                                      if request.method == 'POST':
                                             post=approvals()
                                             if request.POST.get('case_id') and request.POST.get('equipment_id'):
                                                post=approvals()
                                                post.case_id=request.POST.get('case_id')
                                                post.equipment_id=request.POST.get('equipment_id')
                                                post.completion_date=request.POST.get('completion_date')
                                                post.action_recommendation_id=request.POST.get('action_recommendation_id')
                                                post.action_recommendation_type=request.POST.get('action_recommendation_type')
                                                post.action_recommendation_category=request.POST.get('action_recommendation_category')
                                                post.equipment_area=request.POST.get('equipment_area')
                                                post.usage_type=request.POST.get('usage_type')
                                                post.speed_category=request.POST.get('speed_category')
                                                post.completion_date=request.POST.get('completion_date')
                                                post.load_category=request.POST.get('load_category')
                                                post.floors_categorye=request.POST.get('floors_category')
                                                post.save()
                                                return render(request,'predictor/Result.html')  
                                             
                      
                      
                             
  

                                          
                                        
                                         
                                             

def result(request):
	                return render(request,'predictor/Result.html')


