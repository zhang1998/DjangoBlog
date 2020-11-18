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
    #图片的位置
    imageLoca=models.CharField(max_length=300) #建立的时候直接使用其groups 组 绑定文件夹
    # 图片的显示顺序
    showOrder=models.IntegerField("显示顺序id")
    textContent=models.CharField(max_length=300)
    created = models.DateField(auto_now_add=True)
    groups=models.ForeignKey(Groups, on_delete=models.CASCADE,)

'''
这个是 每个 上传的原始图片组 对应的内容
当然 其实
1. 原始作品的信息
2. 以及 新建的group的 信息 都在这里
新上传的图片 其存储 和显示 是分开的  显示是 显示组的事情 用代码解决
'''
class ImageSt(models.Model):
    #图片的唯一标志


    # 图片的显示顺序
    created = models.DateField(auto_now_add=True)
    #描述
    description=models.CharField(max_length=300)
    #存储位置
    storepa=models.CharField(max_length=300) #直接放的就是文件名字
    frontCover=models.CharField(max_length=300) #封面的位置
    #作品名字 用来自己识别的
    name=models.CharField(max_length=300)
    #作者 author
    author=models.CharField(max_length=300)
    #页数 page
    #上架日期
    #更新日期


#测试 编辑器部分的功能
class editorTest(models.Model):
    body=models.TextField()
    content = models.TextField()
    def __str__(self):
        return self.body
