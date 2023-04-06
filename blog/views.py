from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.

# superuse name - coder ,pass - man9 , email - rapx


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post': post, 'comments': comments,'user':request.user}
    return render(request, 'blog/blogPost.html', context)


def postComment(request):
    if request.method == "POST":
        # comment = request.POST.get('comments')
        # user = request.user
        # postSno = request.POST.get('postSno')
        # post = Post.objects.get(sno=postSno)

        comment = request.POST['comment']
        postSno = request.POST['postSno']
        user = request.user
        post = Post.objects.get(sno=postSno)

        print(comment, user, postSno, post)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blog/{post.slug}")
