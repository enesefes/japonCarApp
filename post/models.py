from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Yazar', related_name='posts')
    image = models.ImageField(null=True, blank=True, verbose_name='Resim')
    title = models.CharField(max_length=200, verbose_name='Başlık')
    content = models.TextField(verbose_name='içerik')
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True)
    postTitleSlug  = models.SlugField(unique=True, editable=False, max_length=130)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'postTitleSlug':self.postTitleSlug})
        #return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create')
        #return "/post/{}".format(self.id)

    def get_update_url(self):
        return reverse('post:update', kwargs={'postTitleSlug':self.postTitleSlug})
        #return "/post/{}".format(self.id)
    
    def get_delete_url(self):
        return reverse('post:delete', kwargs={'postTitleSlug':self.postTitleSlug})
        #return "/post/{}".format(self.id)

    def get_unique_slug(self):
        postTitleSlug = slugify(self.title.replace('ı','i'))
        uniques_slug= postTitleSlug
        counter = 1
        while Post.objects.filter(postTitleSlug=uniques_slug).exists():
            uniques_slug = '{}-{}'.format(postTitleSlug, counter)
            counter +=1
        return uniques_slug


    def save(self, *args, **kwargs):
        self.postTitleSlug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering=['-publishing_date', 'id']


class Comment(models.Model):

    post = models.ForeignKey('post.Post', related_name='comments', on_delete = models.CASCADE)
    name= models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True)