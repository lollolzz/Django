# from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# def index(request):
#
#     posts = Post.objects.all().order_by('-pk')
#     # all() 데이터 가져오기
#
#     return render(
#         # render 랜더링 하는 거
#         # html, css, javascrtipt 등 개발자가 작성한 문서를 브라우저에서 그래픽 형태로
#         # 출력하는 과정
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.object.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )
