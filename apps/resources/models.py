from django.db import models
from django.contrib import auth

# from django.contrib.postgres.fields import ArrayField

from apps.core.models import CreatedModifiedDateTimeBase
from apps.resources import validators

# Create your models here.


class Tag(CreatedModifiedDateTimeBase):
    # id=None # If you don't want the default id to be created
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat


class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        auth.get_user_model(), null=True, on_delete=models.SET_NULL
    )
    cat_id = models.ForeignKey(
        "resources.Category", default=1, on_delete=models.SET_DEFAULT
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    # rate = ArrayField(base_field=models.IntegerField())  # INT ARRAY

    class Meta:
        verbose_name_plural = "Resources"
        ordering = ("title",)
        # ordering = ("user_id__username",)

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"

    def get_all_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])


class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.resources_id.title} - {self.tag_id.name}"

    def get_resource_name(self):
        return self.resources_id.title

    def get_tag_name(self):
        return self.tag_id.name


class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        auth.get_user_model(), null=True, on_delete=models.SET_NULL
    )
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.user_id.username} - {self.resources_id.title}"


class Rating(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validators.check_rating_range])

    def user_name(self):
        return self.user_id.username

    def resource_title(self):
        return self.resources_id.title
