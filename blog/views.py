from django.shortcuts import render
#models에 있는 파일을 가져와 준다.
from django.utils import timezone
from .models import Post



# Create your views here.
def post_list(request):
	#published_date 기준으로 정리해준다.
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
                                                  #템플릿을 추가하기 위해 매개변수를 추가


