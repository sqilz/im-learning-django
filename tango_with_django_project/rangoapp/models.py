from django.template.defaultfilters import slugify
from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # can be blank=True, slugifies/populates the category slug field of a
    # category as you type, specified in rangoapp/admin.py CategoryAdmin
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        # Fix typo 'Categorys' to Categories in admin page
        verbose_name_plural = 'categories'

    def __str__(self):  # For Python 2, use __unicode __too
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
