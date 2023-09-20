from django.contrib import admin
from apps.resources import models


# Register your models here.
class CustomResources(admin.ModelAdmin):
    list_display = (
        "get_username",
        "title",
        "get_category",
        "link",
        "get_all_tags",
        "description",
    )

    @admin.display(description="Username")
    def get_username(self, obj):
        return obj.user_id.username

    @admin.display(description="Category")
    def get_category(self, obj):
        return obj.cat_id.cat

    @admin.display(description="Tags")
    def get_tags(self, obj):
        return obj.tags


class CustomResourcesTag(admin.ModelAdmin):
    list_display = ("get_resource_name", "get_tag_name")


class CustomRatingAdmin(admin.ModelAdmin):
    list_display = ("user_name", "resource_title", "rate")


admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.ResourcesTag, CustomResourcesTag)
admin.site.register(models.Review)
admin.site.register(models.Rating, CustomRatingAdmin)
