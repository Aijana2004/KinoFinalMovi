from django.db import models




class UserProfile(models.Model):
    nickname = models.CharField(max_length=40,unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    website = models.URLField(verbose_name=None)

    def __str__(self):
        return  self.nickname


class Follow(models.Model):
    follower_up = models.ForeignKey(UserProfile,related_name='person')
    following_up = models.ForeignKey(UserProfile,related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower_up}-{self.following_up}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='images',null=True,blank=True)
    video  = models.FileField(verbose_name='video',null=True,blank=True)
    caption =models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtag =models.CharField(max_length=30)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent =models.ForeignKey('self',related_name='replies',null=True,blank=True,on_delete=models.CASCADE)
    like =models.BooleanField(null=False,blank=True)

    def __str__(self):
        return f'{self.user}-{self.post}-{self.text}'


