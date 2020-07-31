from django.db import models


class BlogPost(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=50, blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.title

class GeneratedPage(models.Model):
    page_title = models.CharField(max_length=50, blank=True)
    page_type_choices = [
    ('BLOG', 'Blog'),
    ('INFO', 'Information'),
    ('BIZ', 'Buisness'),
    ('FOOD', 'Food Recipe'),
    ('SCAM', 'Scam'),
    ]
    page_type = models.CharField(max_length=4, choices=page_type_choices, blank=True)

    ##Blog Fields
    blog_posts = models.ManyToManyField(BlogPost)
    blog_introduction = models.TextField(default="Welcome to my blog!", blank = True)

    ##Information Fields
    
    ##Buisness Fields

    ##Food Recipe Fields

    ##Scam Fields