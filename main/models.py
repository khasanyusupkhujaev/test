from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    picture = models.ImageField(upload_to="profilepic/", blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, raw=False, **kwargs):
        if created and not raw:
            Profile.objects.create(user=instance)
            print('Profile Created')

class Photos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ImageField(upload_to="posts/", blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True, default=None, related_name='likes1')

    def __str__(self):
        return str(self.user.username)

    @property
    def num_likes(self):
        return self.likes.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Photos, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post.user.username), self.post.id

class Comment(models.Model):
    post = models.ForeignKey(Photos, related_name='comments', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.post.id)