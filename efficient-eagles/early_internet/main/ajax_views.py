from django.shortcuts import render, redirect

from main.models import CustomUser, Post, Comment


def ajax_vote_post(request, post_id, vote):
    user = request.user
    post = Post.objects.get(id=post_id)
    upvoted = user not in post.upvoted_by.all()
    downvoted = user not in post.downvoted_by.all()

    # if true = user didn't voted before
    if upvoted and downvoted:
        if vote:
            post.upvotes = post.upvotes + 1 
            post.upvoted_by.add(user)
        else:
            post.downvotes = post.downvotes + 1 
            post.downvoted_by.add(user)
    else:
        if not upvoted and vote:
            post.upvotes = post.upvotes - 1 
            post.upvoted_by.remove(user)
        elif not downvoted and not vote:
            post.downvotes = post.downvotes - 1 
            post.downvoted_by.remove(user)

    post.save()

    return redirect('home')

def ajax_vote_comment(request, comment_id, vote):
    user = request.user
    comment = Comment.objects.get(id=comment_id)
    upvoted = user not in comment.upvoted_by.all()
    downvoted = user not in comment.downvoted_by.all()

    # if true = user didn't voted before
    if upvoted and downvoted:
        if vote:
            comment.upvotes = comment.upvotes + 1 
            comment.upvoted_by.add(user)
        else:
            comment.downvotes = comment.downvotes + 1 
            comment.downvoted_by.add(user)
    else:
        if not upvoted and vote:
            comment.upvotes = comment.upvotes - 1 
            comment.upvoted_by.remove(user)
        elif not downvoted and not vote:
            comment.downvotes = comment.downvotes - 1 
            comment.downvoted_by.remove(user)

    comment.save()

    return redirect('home')
