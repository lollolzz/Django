from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()

    # 시간 자동 설정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후 작석 예정

    # title제목 설정하는 것
    def __str__(self):
        return f'[{self.pk}] {self.title}'
        # {}만 의미를 가지고 [], () 들은 그대로 출력된다.

# Create your models here.
