from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        # Check if the passwords match
        if password != confirm_password:
            messages.error(request,'Password is not matching')
            return redirect('/auth/signup')
        
         # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')
        
        # Create the new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('/')

        # Show success message and redirect to login page
        messages.success(request, 'Sign-up successful! You can now log in.')
        return redirect('/auth/login/')
    
    return render(request, 'signup.html')

def handleLogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password = request.POST.get('pass1')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('/')  # Redirect to the home page or any page you want after login
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid credentials, please try again.')

    return render(request, 'login.html')

    

def handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request,'login.html')
    