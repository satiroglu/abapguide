from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Taslak"),
    (1, "Yayında")
)


# Category Model
class Category(models.Model):
    # Category
    name = models.CharField(verbose_name="Kategori Adı", max_length=200, unique=True, )
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    description = models.TextField(verbose_name="Kısa Açıklama", blank=True, max_length=200,
                                   help_text="Maksimum 200 karakter")

    # SEO
    seoTitle = models.CharField(verbose_name="SEO Başlığı", max_length=70, blank=True,
                                help_text="Maksimum 70 karakter")
    seoKeywords = models.CharField(verbose_name="Anahtar Kelimeler", blank=True, max_length=300,
                                   help_text="Anahtar kelimeleri virgül ile ayırın")
    seoDescription = models.CharField(verbose_name="SEO Açıklama", blank=True, max_length=150,
                                      help_text="Maksimum 160 karakter")

    # Other
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar", )

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name



class Post(models.Model):
    # Post
    title = models.CharField(verbose_name="Yazı Başlığı", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    content = models.TextField(verbose_name="Yazı")

    # SEO
    seoTitle = models.CharField(verbose_name="SEO Başlığı", max_length=70, blank=True,
                                help_text="Maksimum 70 karakter")
    seoKeywords = models.CharField(verbose_name="Anahtar Kelimeler", blank=True, max_length=300,
                                   help_text="Anahtar kelimeleri virgül ile ayırın")
    seoDescription = models.CharField(verbose_name="SEO Açıklama", blank=True, max_length=150,
                                      help_text="Maksimum 160 karakter")

    # Other
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=1)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', verbose_name="Yazar",)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazılar'

    def __str__(self):
        return self.title