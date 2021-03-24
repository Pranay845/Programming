from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from .models import Contact
from Blog.models import Post


# Create your views here.
def home(request):
    return render(request, "Home/Home.html")


def about(request):
    return render(request, "Home/About.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phoneNumber=phoneNumber, content=content)

        if len(name) < 2 or len(email) < 3 or len(phoneNumber) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phoneNumber=phoneNumber, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "Home/Contact.html")


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        AllPosts = Post.objects.none()
    else:
        AllPostsTitle = Post.objects.filter(title__icontains=query)
        AllPostsAuthor = Post.objects.filter(author__icontains=query)
        AllPostsContent = Post.objects.filter(content__icontains=query)
        AllPosts = AllPostsTitle.union(AllPostsContent, AllPostsAuthor)
    if AllPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    Parameters = {'AllPosts': AllPosts, 'query': query}
    return render(request, 'Home/Search.html', Parameters)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # Check for errorneous input
        if len(username)>10:
            messages.error(request, " Your User name must be under 10 characters")
            return redirect('Home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('Home')
        if pass1!= pass2:
             messages.error(request, " Passwords do not match")
             return redirect('Home')
         
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('Home')

    else:
        raise Http404()

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("Home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("Home")

    raise Http404()

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Home')

