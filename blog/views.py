from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from .models import Post,Comments
from blog.templatetags import extras
# Create your views here.
def bloghome(request):
    allpost= Post.objects.all();
    context={"allpost":allpost}
    return render(request,'blog/bloghome.html',context)
def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=Comments.objects.filter(post=post,parent=None)
    replies=Comments.objects.filter(post=post).exclude(parent=None)
    reptdict={}
    for reply in replies:
        if reply.parent.srno not in reptdict.keys():
            reptdict[reply.parent.srno]=[reply]
        else:
            reptdict[reply.parent.srno].append(reply)
    context={'post':post,'comments':comments,'reptdict':reptdict}
    return render(request,'blog/blogpost.html',context)
def postcomment(request):
    if request.method=="POST":
        comment=request.POST.get('comments')
        user=request.user
        srno=request.POST.get('srno')
        parentsrno=request.POST.get('parentsrno')
        post=Post.objects.get(srno=srno)
        if parentsrno == "":
            comments=Comments(comment=comment,user=user,post=post)
            comments.save()
            messages.success(request,"Your comment has been posted succesfully")
        else:
            parent=Comments.objects.get(srno=parentsrno)
            comments=Comments(comment=comment,user=user,post=post,parent=parent)
            comments.save()
            messages.success(request,"Your reply has been posted succesfully")
    else:
        messages.error(request,"cannot add comment")
    return redirect(f"/blog/{post.slug}")