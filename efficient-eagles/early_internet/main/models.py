from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to="profile_imgs/", null=True, blank=True)
    bio = models.TextField(
        max_length=100, default="Hi, I am a HoneyFeed User", null=True, blank=True
    )

    def __str__(self):
        return self.username


class Topic(TimeStampedModel):
    name = models.CharField(max_length=20, default="", blank=False, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=255, default="", blank=True)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    body = models.TextField(default="", blank=True)

    slug = models.SlugField(max_length=255, default="", blank=True, unique=True)

    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    upvoted_by = models.ManyToManyField(CustomUser, related_name="upvoted_by")
    downvoted_by = models.ManyToManyField(CustomUser, related_name="downvoted_by")
    comments = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return f"title={self.title} author={self.author} upvotes={self.upvotes} downvotes={self.downvotes}"

    @property
    def url(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse("topic", slug=self.slug)

    @property
    def comment_url(self):
        return "{}/comments/".format(self.slug)

    def __str__(self):
        return f"title={self.title} author={self.author} upvotes={self.upvotes} downvotes={self.downvotes}"

    def save(self, *args, **kwargs):
        if self.pk:
            self.upvotes = len(self.upvoted_by.all())
            self.downvotes = len(self.downvoted_by.all())
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            slug = slugify(self.title)
            try:
                slug += "-" + str(self.id)
            except Post.DoesNotExist:
                pass
            self.slug = slug
            self.save()


class Comment(TimeStampedModel):
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    upvoted_by = models.ManyToManyField(CustomUser, related_name="comment_upvoted_by")
    downvoted_by = models.ManyToManyField(
        CustomUser, related_name="comment_downvoted_by"
    )

    body = models.CharField(max_length=10000, default="")

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_thread = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    thread_level = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return f"author={self.author} body={self.body} thread_level={self.thread_level}"

    def save(self, *args, **kwargs):
        if self.pk:
            self.upvotes = len(self.upvoted_by.all())
            self.downvotes = len(self.downvoted_by.all())
        super(Comment, self).save(*args, **kwargs)

    @classmethod
    def preorder(cls, comment, ordered_comments):
        """
        Depth-first search of binary tree - Pre-order.

            Parameters:
                post (Post): Post object
                ordered_comments (list): List of Comment objects

            Returns:
                None
        """
        comments = comment.comment_set.order_by("created")
        if not comments:
            return None

        for thread_comment in comments:
            ordered_comments.append(thread_comment)
            cls.preorder(thread_comment, ordered_comments)

    @classmethod
    def sort_comment_section(cls, post):
        """
        Create ordered list of comments.

            Parameters:
                post (Post): Post object

            Returns:
                ordered_comments (list): List of Comment objects
        """
        ordered_comments = []
        comments = Comment.objects.filter(post=post, thread_level__in=[0, 1, 2, 3, 4])
        ordered_root_comments = comments.filter(thread_level=0).order_by("-created")

        for comment in ordered_root_comments:
            ordered_comments.append(comment)
            cls.preorder(comment, ordered_comments)

        return ordered_comments
