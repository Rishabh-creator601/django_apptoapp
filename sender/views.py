from django.shortcuts import render
from .models import Profile
from django.contrib import messages



# Create your views here.
# cd web && python manage.py runserver
def index(request):
	
	if request.method == 'POST':
		name = request.POST.get('name')
		age = request.POST.get('age')
		prof = request.POST.get('prof')
		gender= request.POST.get('gender')
		profile = Profile(name=name,age=age,proffession=prof)
		profile.save()
		
		messages.success(request, 'Profile details Added.')
	
	
	return render(request,'form.html')
	
