from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 字节类型，长度200
    pub_date = models.DateTimeField('date publish')  # 时间类型

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键
    choice_text = models.CharField(max_length=200)  # 字符类型
    votes = models.IntegerField(default=0)  # 整型
# Create your models here.
