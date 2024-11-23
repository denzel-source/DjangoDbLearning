from django.shortcuts import render,get_object_or_404

from DbApp.models import Blogpost


# Create your views here.
def bloglist(request):
    posts=Blogpost.objects.all()
    return render(request,'blog_list.html',{'posts':posts})

def blog_detail(request,id):
    post=get_object_or_404 (Blogpost,id=id)
    return render(request,'blog_detail.html',{'post':post})
