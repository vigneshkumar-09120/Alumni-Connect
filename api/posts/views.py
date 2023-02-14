from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Post
from alumni.models import Alumni
from .forms import PostCreationForm
from .models import Post
from comments.forms import CommentForm
from django.shortcuts import render, get_object_or_404

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    ordering = ['-time_posted']

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'posts/new.html'

    def form_valid(self, form):
        form.instance.author = Alumni.objects.get(user = self.request.user)
        return super().form_valid(form)

def post_detail(request, pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.posted_by = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
