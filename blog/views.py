from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog


class BlogHome(View):
    def get(self, request):
        #  <view logic>
        posts = Blog.objects
        print(posts)
        return render(request, 'blog/blog.html', {'posts':posts})

class Detail(View):
    def get(self, request, blog_id):
        #  <view logic>
        detail_post = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'blog/detail.html', {'detail_post': detail_post })
