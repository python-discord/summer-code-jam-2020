from django.db import models


class BlogPost(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=50, blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.title


class PageImage(models.Model):
    image = models.ImageField()


# These 2 following classes are for the food recipies
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=35)


class Step(models.Model):
    step = models.TextField()


class GeneratedPage(models.Model):
    page_title = models.CharField(max_length=50, blank=True)
    page_author = models.CharField(max_length=20, blank=True)
    page_type_choices = [
        ("BLOG", "Blog"),
        ("INFO", "Information"),
        ("BIZ", "Business"),
        ("FOOD", "Food Recipe"),
        ("SCAM", "Scam"),
    ]
    page_type = models.CharField(max_length=4, choices=page_type_choices, blank=True)
    page_content = models.TextField(blank=True)
    page_images = models.ManyToManyField(PageImage, blank=True)
    # The tab description will be based on the page type (this is the little text that appears on the tab, not the url)
    tab_description = models.CharField(max_length=10, blank=True)

    # Blog Fields
    blog_posts = models.ManyToManyField(BlogPost, blank=True)
    blog_introduction = models.TextField(default="Welcome to my blog!", blank=True)

    # Information Fields

    # Business Fields

    # Food Recipe Fields
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    steps = models.ManyToManyField(Step, blank=True)

    # Scam Fields
