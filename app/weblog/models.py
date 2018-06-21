from django.db import models


class Blog(models.Model):
    # id = primary_key
    name = models.CharField(max_length=100)
    tagline = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ThemeBlog(Blog):
    # blog_ptr_id = primary_key
    theme = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.theme}'


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(blank=True)
    pub_date = models.DateField(blank=True, null=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
