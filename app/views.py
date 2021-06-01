from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView

from app.models import *


class Home(View):
    def get(self,request):
        return render(request,'app/home.html')


class SchoolListView(ListView):
    model=School
    #queryset=School.objects.filter(name='Java')
    context_object_name='schools'
    #template_name='app/school_list.html'
    ordering=['name']


#standard html file names for each View class is mentioned below

    #applicationName/modelclassname_list.html--->ListView-->app/school_list.html
    #applicationName/modelclassname_detail.html--->DetailView-->app/school_detail.html
    #applicationName/modelclassname_form.html--->CreateView-->app/school_form.html
    #applicationName/modelclassname_form.html--->UpdateView-->app/school_form.html
    #applicationName/modelclassname_confirm_delete.html--->DeleteView-->app/school_confirm_delete.html


