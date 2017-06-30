from django.contrib import admin
from .models import Profile, Topic, Post

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Profile)


class TopicAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'topic_poster', None) is None:
            obj.topic_poster = Profile.objects.get(pk=request.my_id)
            #obj.topic_poster = request.user
        obj.save()
