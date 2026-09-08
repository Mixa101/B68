from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    text = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, upload_to="posts")
    views = models.IntegerField(default=0)
