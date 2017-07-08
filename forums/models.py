from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.utils.translation import ugettext_lazy as _

#replaced manytomany wiht foreign
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Topic(models.Model):
    topic_title = models.CharField(max_length=60)
    topic_poster = models.ForeignKey(User, null=True)

    def get_absolute_url(self):
        return reverse('forums:topic', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.topic_title) + ' -  ' + str(self.topic_poster)


class Post(models.Model):
    topic = models.ForeignKey(Topic)
    poster = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(validators=[MaxLengthValidator(200000)], null=True)
    parent = models.ForeignKey("self", blank=True, null=True)



    def __str__(self):
        return str(self.topic) + ' - ' + str(self.poster) + ' - ' + str(self.content) + ' - ' + str(self.parent)

