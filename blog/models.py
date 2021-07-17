from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    srno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,unique=True)
    content=models.TextField()
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=50,unique=True)
    timestamp=models.DateTimeField()
    def __str__(self):
        return self.title+ ' by ' + self.author
class Comments(models.Model):
    srno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self) -> str:
        return self.comment[0:13] + "..."+ "by "+self.user.username