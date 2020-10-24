from django.db import models

# Create your models here.
# 展示 所有的 图片组
class Groups(models.Model):

    # 组的名称
    title=models.CharField(max_length=300)
    # 组的链接
    def __str__(self):
        return self.title

# 修改 每张图片对应的内容
class Group(models.Model):

    #图片的唯一标志
    imageId=models.IntegerField("图片的id")
    # 图片的显示顺序
    showOrder=models.IntegerField("显示顺序id")
    textContent=models.CharField(max_length=300)
    created = models.DateField(auto_now_add=True)
    groups=models.ForeignKey(Groups, on_delete=models.CASCADE,)
