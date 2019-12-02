from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import *
from .forms import *

@login_required(login_url='/accounts/login/')
def home(request):

    current_user = request.user    
    profile = Profile.objects.filter(prof_user=request.user)
    hoodie = Neighborhood.objects.all()
    arr=[]
    for post in profile:
        arr.append(post.hood_id.id)
    if len(arr)>0:
        id=arr[0]
        all_posts = Post.objects.all()
        
    else:
        all_posts = ""       

    return render(request,'Neigborhood/index.html',{"all_posts":all_posts,"prof_info":profile,"hoodie":hoodie})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    business = Business.objects.filter(business_owner = current_user)
    posts = Post.objects.filter(post_owner = current_user)
    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'business':business,'posts':posts})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_owner = current_user
            business.save()
        return redirect('home')
    else:
        form = BusinessForm()
    return render(request,"business/business_form.html",{"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(prof_user=request.user)
        arr=[]
        for business in profile:
            arr.append(business.hood_id.id)
        if len(arr)>0:
            id=arr[0]
            all_businesses = Business.objects.all()
        else:
            all_businesses = Business.objects.filter(business_hood_id=10000000000)
    except Exception as e:
        raise Http404()
     
    return render(request,'business/business_index.html',{"all_businesses":all_businesses,"profile":profile})
def search_post(request):
    if 'post' in request.GET and request.GET ["post"]:
        search_term = request.GET.get("post")
        searched_posts = Business.search_business_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search/search.html', {"message":message, "post":searched_posts})

    else:
        message = "No search results yet!"
        return render (request, 'search/search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def contact(request):
    contact = ContactInfo.objects.all()
    return render(request,'Neigborhood/contact_info.html',{"contact":contact})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_owner = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request,"posts/create_post.html",{"form":form})


# Create your views here.
