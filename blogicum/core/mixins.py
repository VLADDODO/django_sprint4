from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class PostMixin(LoginRequiredMixin):
    """Миксин для CBV работы с публикациями.

    Содержит общие настройки: модель, форму, шаблон и ключ URL.
    Проверяет, что редактировать/удалять пост может только его автор.
    """

    # Импорты внутри методов, чтобы избежать циклических зависимостей
    template_name = 'blog/create.html'
    pk_url_kwarg = 'post_id'

    def get_model(self):
        from blog.models import Post
        return Post

    def get_form_class(self):
        from blog.forms import PostForm
        return PostForm

    @property
    def model(self):
        from blog.models import Post
        return Post

    @property
    def form_class(self):
        from blog.forms import PostForm
        return PostForm

    def dispatch(self, request, *args, **kwargs):
        """Перенаправляет не-автора на страницу поста без сообщения об ошибке."""
        post = self.get_object()
        if post.author != request.user:
            return redirect(
                'blog:post_detail',
                post_id=self.kwargs[self.pk_url_kwarg],
            )
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('blog:index')


class CommentMixin(LoginRequiredMixin):
    """Миксин для CBV работы с комментариями.

    Содержит общие настройки: модель, форму, шаблон и ключ URL.
    """

    template_name = 'blog/comment.html'
    pk_url_kwarg = 'comment_id'

    @property
    def model(self):
        from blog.models import Comment
        return Comment

    @property
    def form_class(self):
        from blog.forms import CommentForm
        return CommentForm

    def get_success_url(self):
        return reverse_lazy(
            'blog:post_detail',
            kwargs={'post_id': self.kwargs['post_id']},
        )


class IsAuthorMixin:
    """Миксин проверки авторства.

    Перенаправляет не-автора на страницу поста.
    Должен стоять ПОСЛЕ LoginRequiredMixin и ПЕРЕД UpdateView/DeleteView.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return redirect(
                'blog:post_detail',
                post_id=self.kwargs['post_id'],
            )
        return super().dispatch(request, *args, **kwargs)
