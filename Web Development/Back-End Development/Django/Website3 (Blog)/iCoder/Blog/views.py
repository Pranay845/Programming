from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, BlogComment
from .templatetags import Extras

# Create your views here.


def bloghome(request):
    AllPosts = Post.objects.all()
    Context = {'AllPosts': AllPosts}
    return render(request, "Blog/BlogHome.html", Context)

def blogpost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views+=1
    post.save()
    Comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.postSerialNumber not in replyDict.keys():
            replyDict[reply.parent.postSerialNumber]=[reply]
        else:
            replyDict[reply.parent.postSerialNumber].append(reply)

    Context={'Post':post, 'Comments': Comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "Blog/BlogPost.html", Context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSerialNumber=request.POST.get('postSno')

        post= Post.objects.get(SerialNumber=postSerialNumber)
        parentSerialNumber= request.POST.get('parentSno')
        if parentSerialNumber=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(postSerialNumber=parentSerialNumber)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/Blog/{post.slug}")