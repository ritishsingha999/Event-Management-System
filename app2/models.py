from django.db import models

# Create your models here.
def sign_up(request):
    pass
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    # if password == confirm_password:
    #     user = User.objects.create_user(username=username, email=email, password=password)
    #     user.save()
    #     return redirect('login')
    # else:
    #     return render(request, 'signup.html', {'error': 'Passwords do not match'})
        