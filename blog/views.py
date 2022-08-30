# blog.views.py

from django.urls import reverse
from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    paginate_by = 15
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"
    template_name = "blog/post_list.html"


post_list_view = PostListView.as_view(
    extra_context={"page_title": "blog"}
)


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = f"{self.object.title}"
        return super().get_context_data(**kwargs)


post_detail_view = PostDetailView.as_view()


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__contains=tag).published()
    context = {"tag": tag, "posts": posts}
    return render(request, "blog/post_by_tags.html", context)


blog_tag = blog_tag
