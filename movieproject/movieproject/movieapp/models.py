from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    des=models.TextField()
    image=models.ImageField(upload_to='IMAGE')

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}"width="100"/>')