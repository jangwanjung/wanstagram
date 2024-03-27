from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id')  #피드의 객체들의 모든걸 가져오겠다는 뜻이다 select * from content_feed; 와 같은기능을한다

        return render(request,'jinstagram/main.html',context=dict(feeds=feed_list)) #context는 feed_list의 있는값들을 딕셔너리형태로 main.html로 넘겨준다는 뜻이다
