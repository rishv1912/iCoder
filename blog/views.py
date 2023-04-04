from django.shortcuts import render,HttpResponse
# Create your views here.

# superuse name - coder ,pass - man9 , email - rapx 

def blogHome(request):
    return render(request,'blog/blogHome.html')
def blogPost(request,slug):
    return render(request,'blog/blogPost.html',slug)
    