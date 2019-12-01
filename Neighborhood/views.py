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
        all_posts = Post.objects.filter(hood_post=id)
    else:
        all_posts = ""       

    return render(request,'hood_app/index.html',{"all_posts":all_posts,"prof_info":profile,"hoodie":hoodie})

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


# Create your views here.
