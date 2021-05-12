from django.shortcuts import render
from sender.models import Profile

def home(request):
	objects = Profile.objects.all()
	params = {'objects':objects}
	return render(request,'main.html',params)

# Create your views here.
