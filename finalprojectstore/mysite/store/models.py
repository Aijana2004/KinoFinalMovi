from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField (max_length=32)
    age = models.PositiveIntegerField(default=0)
    date_registered = models.DateField(auto_now=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    STATUS_CHOICES = (
        ('gold','Gold'),
        ('silver','Silver'),
        ('bronze','Bronze'),
        ('simple','Simple'),
    )
    status= models.CharField(max_length=10, choices=STATUS_CHOICES,default='Simple')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=16,unique=True)


    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    product_video = models.FileField(verbose_name='video',null=True,blank=True)


    def __str__(self):
        return self.product_name


class ProductPhotos(models.Model):
    product = models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')



class Rating(models.Model):
    product = models.ForeignKey(Product,related_name='ratings',on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i,str(i))for i in range (1,6)],verbose_name='РЕЙТИНГ')


    def __str__(self):
        return f'{self.product}-{self.user}-{self.stars}'



class Review( models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self',related_name='replies',null=True,blank=True,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.author}-{self.product}'