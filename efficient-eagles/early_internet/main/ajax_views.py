from django.http import JsonResponse

from main.models import Post, Comment


def helper_vote(obj, user, vote):
    # Adds/Removes user from field upvoted_by/downvoted_by from models Post/Comment
    # upvoted = user didn't upvote yet
    # downvoted = user didn't downvote yet
    upvoted = user not in obj.upvoted_by.all()
    downvoted = user not in obj.downvoted_by.all()

    if not upvoted and vote:
        obj.upvoted_by.remove(user)
    elif not downvoted and not vote:
        obj.downvoted_by.remove(user)
    elif vote:
        obj.upvoted_by.add(user)
        obj.downvoted_by.remove(user)
    elif not vote:
        obj.upvoted_by.remove(user)
        obj.downvoted_by.add(user)

    obj.save()
    return JsonResponse({"upvotes": obj.upvotes, "downvotes": obj.downvotes})


def ajax_vote_post(request, post_id, vote):
    user = request.user
    post = Post.objects.get(id=post_id)

    return helper_vote(post, user, vote)


def ajax_vote_comment(request, comment_id, vote):
    user = request.user
    comment = Comment.objects.get(id=comment_id)

    return helper_vote(comment, user, vote)
