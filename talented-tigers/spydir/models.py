from django.db import models


class BlogPost(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=50, blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.title


class PageImage(models.Model):
    image = models.TextField(blank=True)


class GeneratedPage(models.Model):
    page_title = models.CharField(max_length=50, blank=True)
    is_generated = models.BooleanField(default=False)
    css_seed = models.IntegerField()
    page_author = models.CharField(max_length=20, blank=True)
    page_type_choices = [
        ("BLOG", "Blog"),
        ("INFO", "Information"),
        ("BIZ", "Business"),
    ]
    page_type = models.CharField(max_length=4, choices=page_type_choices, blank=True)
    page_images = models.ManyToManyField(PageImage, blank=True)

    # Blog Fields
    blog_posts = models.ManyToManyField(BlogPost, blank=True)
    blogger_age = models.IntegerField(blank=True, null=True)
    blogger_location = models.CharField(max_length=20, blank=True)

    # Information Fields
    page_content = models.TextField(blank=True)
    page_source_url = models.URLField(blank=True)

    # Business Fields
    business_phone_num = models.CharField(max_length=10, blank=True)
    business_email = models.EmailField(blank=True)
    business_about = models.TextField(blank=True)
    business_mission = models.TextField(blank=True)

    def __str__(self):
        return self.page_title
