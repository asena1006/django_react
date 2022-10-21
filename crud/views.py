from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from .models import Post
from django.views.generic import DetailView, ListView, ArchiveIndexView


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view(model=Post, paginate_by=10)
# def post_list(requset):
#     qs = Post.objects.all()
#     q = requset.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     return render(requset, 'crud/post_list.html',{
#         'post_list' : qs,
#         'q' : q,
#     })

post_detail = DetailView.as_view(model=Post)

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at')