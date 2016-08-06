from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from Piazza.models import post, Course

def welcome_teacher(request):
    temp=loader.get_template("welcome_teacher.html")
    result=temp.render()
    return HttpResponse(result)
def display_posts(request,c_name):
    try:
        p=post.objects.all().filter(course=Course.objects.get(course_name=c_name));
    except:
        p=None
    temp=loader.get_template("diplay_posts.html")
    result=temp.render(context={"posts":p,'cname':c_name})
    return HttpResponse(result)