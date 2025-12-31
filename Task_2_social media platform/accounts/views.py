from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user_to_follow)

    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)

    return redirect('/')
