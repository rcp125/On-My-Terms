from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .parser import parse_script
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def fetch_info(request):
	url = "https://www.jetblue.com/legal/flights-terms"
	if request.method == "POST":
		split_list = (request.body).decode("utf-8").split("\n")
		#print(split_list[0])
		
		print("SPLIT LIST: ")
		print(str(split_list[0].replace('"', "")))
		
		url = str(split_list[0].replace('"', ""))
		#url = url
		
		#print(type(url))
		#print(url)
		#print(split_list)
		print(url)
		
	context = {
		#"data": parse_script.parse_url(url) 
		"data": parse_script.sample_info() 
	}
	
	print(context)
	
	response = JsonResponse(context)
	response['Access-Control-Allow-Origin'] = '*'
	response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
	
	return response