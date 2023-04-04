from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.


def index(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(desc) < 4:
            messages.error(request, 'please fill the form correctly')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=desc)
            contact.save()
            messages.success(request, 'Contact request has been sent')
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query) > 77 :
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains= query)
        allPostsContent  = Post.objects.filter(content__icontains = query )
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No search results found ')

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
