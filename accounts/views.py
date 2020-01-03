from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """
    This views drop the user on their homepage. This will display a
    birdseye view of the users entire manager account.
    """
    return render(request, 'accounts/home.html')

def login(request):
    """ This view handles all login activity """

    if request.method == 'POST': #  check for valid user on sign-in in post data
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            content = {'error_red': 'Username or Password are incorrect'}
            return render(request, 'accounts/login.html', content)
    else: # only allow access to site if authenticated
        return render(request, 'accounts/login.html')

def logout(request):
    """ This view handles the logout procedure. """

    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


def signup(request):
    """This view allows a user to signup an account."""

    if request.method == 'POST': # check matching passwords and create user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                content = {'error_red': 'Username already taken.'}
                return render(request, 'accounts/signup.html', content)
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            content = {'error_red': 'Passwords do not match'}
            return render(request, 'accounts/signup.html', content)
    else:
        return render(request, 'accounts/signup.html')
