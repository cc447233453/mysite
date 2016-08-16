from django.shortcuts import render
from blog.models import Article
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  

# Create your views here.
def index(request):
	page_no = request.GET.get('page_no',1)
	article_list = Article.objects.all()
	p = Paginator(article_list,10)
	article_list = p.page(page_no)

	context = { 'article_list': article_list }
	return render(request, 'index.html', context)

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'detail.html', {'article': article})

@login_required
def uploadlist(request):
	return render(request, 'uploadlist.html')
