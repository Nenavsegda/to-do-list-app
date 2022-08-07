import sys

from django.contrib import auth, messages
from django.contrib.auth import logout as out
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(reverse('login') + '?token=' + str(token.uid))
    message_body = f'Use this link to log in:\n\n{url}'
    from_email = 'noreply@superlists'
    send_mail(
        f'Your login link for Superlists - {from_email}',
        message_body,
        from_email,
        recipient_list=[email],
    )
    messages.success(
        request, "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')


def logout(request):
    out(request)
    return redirect('/')
