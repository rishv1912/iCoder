from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from blog.models import Post
# Create your views here.

# HTML pages
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
    if len(query) > 77:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No search results found ')

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authentication APIs

def handleSignUp(request):
    if request.method == 'POST':
        # get the parameters
        username = request.POST['username']
        fName = request.POST['fName']
        lName = request.POST['lName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/')

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return redirect('/')

        # passwords should match
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('/')
 
        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fName
        myuser.last_name = lName
        myuser.save()
        messages.success(
            request, 'Your iCoder account has been created successfully')
        return redirect('/')
    else:
        return HttpResponse('404 Error')

def handleLogin(request):
    if request.method == 'POST':
        # get the parameters
        loginusername = request.POST['loginUser']
        loginpass = request.POST['loginPass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/')
        else:
            messages.error(request, 'Login Credentials didn\'t match')
            return redirect('/')

    return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged out ')
    return redirect('/')
