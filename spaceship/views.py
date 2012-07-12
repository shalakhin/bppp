#-*- coding: utf-8 -*-

from django.contrib.auth.views import logout
from django.shortcuts import redirect


def logout_me(request):
    logout(request)
    return redirect('/')

# TODO change password
# TODO upload avatars
# TODO set statuses
# TODO show statistics
# TODO display messages
# TODO moderators?
