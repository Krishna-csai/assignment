from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from .models import Post
from .serializers import PostsSerializer

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/base.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/deatil.html', {'post': post})

def post_list(request):
    post = Post.objects.all()
    serializer = PostsSerializer(post, many=True)
    return JsonResponse(serializer.data, safe=False)