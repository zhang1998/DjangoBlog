'''
作为 项目中为了抄pdf时候 的临时文件 记录

'''



def search(query, fields, terms):
    """ Performs a search based on a list of search terms. Returns a new
            query filtered with the search. """

    if len(terms) > 0:

        search_list = []

        for term in terms:
            field_list = []
            for field in fields:
                field_list.append(Q(**{field + '__icontains':term}))
            search_list.append(reduce(operator.or_, field_list))#逐个进行operator

        return query.filter(reduce(operator.and_, search_list))

    else:
        return query


'''
抄写 输入框部分的内容

'''

#model
class (models.Model):
    body=models.TextField()

    def __str__(self):
        return self.body


admin.site.register()

'''
自定义的 编辑器部分

'''
#model
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="article1")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE,related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ("title",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])




#form
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model=ArticlePost
        fields=("title","body")
#view
def article_post(request):
     if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()

                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
     else:
         article_post_form = ArticlePostForm()
         article_columns = request.user.article_column.all()
         return render(request, "article/column/article_post.html", {"article_post_form":article_post_form, "article_columns":article_columns})
# html
{% extends "article/base.html" %}
{% load static %}
{% block title %}article column{% endblock %}
{% block content %}
<link rel="stylesheet" href="{% static 'editor/css/style.css' %}">
<link rel="stylesheet" href="{% static 'editor/css/editormd.css' %}">

<div style="margin-left:10px">
    <form class="form-horizontal" action="." method="post">{% csrf_token %}
        <div class="row" style="margin-top: 10px;">
            <div class="col-md-2 text-right"><span>标题:</span></div>
            <div class="col-md-10 text-left">{{article_post_form.title}}</div>
        </div>
        <div class="row" style="margin-top: 10px;">
            <div class="col-md-2 text-right"><span>栏目:</span></div>
            <div class="col-md-10 text-left">
                <select id="which_column">
                    {% for column in article_columns %}
                    <option value="{{column.id}}">{{column.column}}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="row" style="margin-top: 10px;">
                <div class="col-md-2 text-right"><span>内容:</span></div>
                <!--div class="col-md-10 text-left">{{article_post_form.body}}</div-->
                <div id="editormd" class="col-md-10 text-left">
                  <textarea style="display:none;" id="id_body"></textarea>
                </div>

        </div>
        <div class="row">
          <input type="button" class="btn btn-primary btn-lg" value="发布" onclick="publish_article()">
        </div>
    </form>
</div>
<script type="text/javascript" src='{% static "js/jquery.js" %}'></script>
<script type="text/javascript" src="{% static 'js/layer.js'%}"></script>
<script type="text/javascript" src='{% static "editor/editormd.min.js" %}'></script>

<script type="text/javascript">
function publish_article(){
    var title = $("#id_title").val();
    var column_id = $("#which_column").val();
    var body = $("#id_body").val();
    $.ajax({
        url: "{% url 'article:article_post' %}",
        type: "POST",
        data: {"title":title, "body":body, "column_id":column_id},
        success: function(e){
            if(e=="1"){
                layer.msg("successful");
                location.href="{% url 'article:article_list' %}";
            }else if(e=="2"){
                layer.msg("sorry.") ;
            }else{
                layer.msg("是不是有没有填写的项目？都必须写，不能空。");
            }
        },
    });
}


$(function() {
    var editor = editormd("editormd", {
        width   : "100%",
        height  : 640,
        syncScrolling : "single",
        path    : "{% static 'editor/lib/' %}"
    });
});

</script>
{% endblock %}



post:
    if .isvalid():
        return HttpResponse("wel")
    else:
        return HttpResponse("now")
