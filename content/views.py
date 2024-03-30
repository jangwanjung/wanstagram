from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed


import os
from jinstagram.settings import MEDIA_ROOT


# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id')  #피드의 객체들의 모든걸 가져오겠다는 뜻이다 select * from content_feed; 와 같은기능을한다

        return render(request,'jinstagram/main.html',context=dict(feeds=feed_list)) #context는 feed_list의 있는값들을 딕셔너리형태로 main.html로 넘겨준다는 뜻이다

class UploadFeed(APIView):
    def post(self,request):

        file = request.FILES['file']
        uuid_name=uuid4().hex
        save_path = os.path.join(MEDIA_ROOT,uuid_name)

        with open(save_path,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image= uuid_name
        content=request.data.get('content')
        user_id=request.data.get('user_id')
        profile_image=request.data.get('profile_image')

        Feed.objects.create(image=image,content=content,user_id=user_id, profile_image=profile_image ,like_count=0)

        return Response(status=200)