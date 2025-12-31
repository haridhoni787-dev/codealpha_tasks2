from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Follow

@login_required
def feed(request):
    posts = Post.objects.all()
    following = []

    if request.user.is_authenticated:
        following = Follow.objects.filter(
            follower=request.user
        ).values_list('following_id', flat=True)

    return render(request, 'feed.html', {
        'posts': posts,
        'following': following
    })


@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes.add(request.user)
    return redirect('feed')


@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if not created:
        follow.delete()

    return redirect('feed')
