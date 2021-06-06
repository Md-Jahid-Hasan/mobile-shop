from django.shortcuts import render, redirect
from .forms import LogInForm
from django.contrib.auth import login, logout, authenticate


def login_user(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            next_url = form.cleaned_data['next_url']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                print(request.GET.get('next', '/'))
                return redirect(next_url)

    form = LogInForm(initial={'next_url': request.GET.get('next', '/')})
    print(request.GET.get('next', '/'))
    context = {'form': form}
    return render(request, 'user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('shop:product_show')
