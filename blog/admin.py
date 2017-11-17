#11/17 자 드장고걸스 듀토리얼 진행
from django.contrib import admin
from .models import Post
#post 모델을 가져오고 있다.

admin.site.register(Post)
#관리자 페이지에서 만든 모델을 보기위해 등록하는 과정이다.

# Register your models here.
