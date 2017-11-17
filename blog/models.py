#djangogirls tutorial
from django.db import models
from django.utils import timezone
#다른 파일에 있는것을 추가하라

class Post(models.Model):
	#모델을 정의하는 코드 모델은 객체(object)
	#class는 특별한 키워드로, 객체를 정의한다는 것을 알려줍니다.
    #Post는 모델의 이름입니다. (특수문자와 공백 제외한다면) 
    	#다른 이름을 붙일 수도 있습니다. 
    	#항상 클래스 이름의 첫 글자는 대문자로 써야 합니다.
	#models은 Post가 장고 모델임을 의미합니다. 
	#이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
	author = models.ForeignKey('auth.User')
	#다른 모델에 대한 링크
	title = models.CharField(max_length=200)
	#글자수가 제한된 텍스트를 정의할때 사용한다.
	text = models.TextField()
	#글자수에 제한이 없는 긴 텍스트를 위한 속성
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		#publish 라는 메서드 
		self.published_data = timezone.now()
		self.save()

	def __str__(self):
		return self.title
