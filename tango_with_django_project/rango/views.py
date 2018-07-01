from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

from rango.forms import UserForm, UserProfileForm

# Create your views here.


def index(request):
     # Query the database for a list of ALL categories currently stored. # Order the categories by no. likes in descending order. # Retrieve the top 5 only - or all if less than 5. # Place the list in our context_dict dictionary # that will be passed to the template engine.
     category_list = Category.objects.order_by('-likes')[:5]
     context_dict = {'categories': category_list}
     # Render the response and send it back! return render(request, 'rango/index.html', context_dict)
     return render(request, 'rango/index.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save() 
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors) 
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})













 



