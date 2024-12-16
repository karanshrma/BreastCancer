
from django.shortcuts import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm
from django.db.models import Q
from django.contrib.auth.models import User


def index(request):
	profile = 'k'
	context={
	'profile':profile
	}
	try:
		profile = Profile.objects.get(username1 = request.user.username )
		context={
		'profile':profile
		}
	except :
		pass

	return render(request, 'index.html' , context)

def about(request):
    profile = 'k'
    context={
    'profile':profile
    }
    try:
        profile = Profile.objects.get(username1 = request.user.username )
        context={
        'profile':profile
        }
    except :
        pass

    return render(request, 'about.html' , context)


def allusers(request):
    profile_data = Profile.objects.all()
    context={
    'data': profile_data
    }
    profile = 'k'
    context={
    'profile':profile
    }
    try:
        profile = Profile.objects.get(username1 = request.user.username )
        context={
        'profile':profile,
                'data': profile_data

        }
    except :
        pass
    if request.method == 'POST' :
        if 'user123' in request.POST  :
            iduser = request.POST['user123']
            # pw = Profile.objects.get(username1=iduser)
            ppp = User.objects.get(username=iduser)
            ppp.delete()
            # pw.delete()
            try:
                 pq = Register.objects.filter(User=iduser)
                 for n in pq:
                    n.status='Cancel'
                    n.save()
            except:
                pass
        if 'check' in request.POST:
            checkcategory = request.POST["check"]
            print(checkcategory)
            Data_get = Profile.objects.all().filter( Q(username1__icontains=checkcategory) | Q(Ocuupation__icontains=checkcategory) | Q(Gender__icontains=checkcategory)| Q(email__icontains=checkcategory) )
            context={'data':Data_get , 'profile':profile}

        else:
            pass
    else:
        pass

    return render(request, 'allusers.html' , context)

def allpatients(request):
    profile_data = Profile.objects.all().filter(Ocuupation='Patient')
    profile = 'k'
    context={
    'data': profile_data
    }
    try:
        profile = Profile.objects.get(username1 = request.user.username )
        context={
        'profile':profile,
        'data': profile_data
        }
    except :
        pass
    if request.method == 'POST' :
        if 'user123' in request.POST  :
            iduser = request.POST['user123']
            # pw = Profile.objects.get(username1=iduser)
            ppp = User.objects.get(username=iduser)
            ppp.delete()
            # pw.delete()
            try:
                 pq = Register.objects.filter(User=iduser)
                 for n in pq:
                    n.status='Cancel'
                    n.save()
            except:
                pass

        if 'check' in request.POST:
            checkcategory = request.POST["check"]
            print(checkcategory)
            Data_get = Profile.objects.all().filter( Q(username1__icontains=checkcategory) | Q(Ocuupation__icontains=checkcategory) | Q(Gender__icontains=checkcategory)| Q(email__icontains=checkcategory) )
            data2 = Data_get.filter(Ocuupation='Patient')
            context={'data':data2 , 'profile':profile}            
        else:
            pass
    else:
        pass

    return render(request, 'allpatients.html' , context)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.Ocuupation = form.cleaned_data.get('Occupation')
        user.profile.Gender = form.cleaned_data.get('Gender')
        user.profile.Contact_Number = form.cleaned_data.get('Contact_Number')
        user.profile.Address = form.cleaned_data.get('Address')
        user.profile.username1 = form.cleaned_data.get('username')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})