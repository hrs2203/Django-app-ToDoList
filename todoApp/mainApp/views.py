from django.shortcuts import render, redirect
import random
from django.http import JsonResponse

def homepage(request):
    return render(
        request = request,
        template_name = 'mainApp/home_page.html',
        context = {}
    )

def send_testGraphData(request):
	l = random.randint(1,30)
	x = []
	y = []
	for i in range(l):
		x.append(random.randint(1,5))
		y.append(x[-1]**2)
	return JsonResponse({
		"x_axis" : x,
		"y_axis" : y
	})