from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from store.models import *
from django.contrib.auth import update_session_auth_hash

def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        connect_data(request)
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        return redirect('store:home')
    return render(request, 'sign_in.html', {'form': form})
    # valid_user = True
    # if request.method == 'POST':
    #     form = LoginForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         return redirect('store:home')
    #     valid_user = False
    # form = LoginForm()
    # return render(request, 'log_in.html', {'form': form, 'valid_user': valid_user})

def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('users:sign_in')

def connect_data(request):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)
    cart_items = CartItem.objects.filter(guest=guest[0]) if guest else []

    for item in cart_items:
        item.customer=request.user
        item.guest=None
        item.save()

def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('store:home')
    return render(request, 'edit_profile.html', {'form': form})


def reset_password(request):
    form = ResetPasswordForm(request.user, request.POST or None)

    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('users:sign_in')
    return render(request, 'reset_password.html', {'form': form})
