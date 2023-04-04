from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.

# superuse name - coder ,pass - man9 , email - rapx


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    print(post)
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)

    