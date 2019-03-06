from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
#     return render(request,"basic_app/index.html")

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('Class based views are cool!')

class IndexView(TemplateView):
    template_name = "basic_app/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #school_list automatically created by django if not specified and sent to templates(lower cases the model name and adds _list)

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.Student
    template_name = "basic_app/school_detail.html"
    #detail view just lowercases the model name and returns the context
