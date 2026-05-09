from django.db.models import Count
from django.utils import timezone


def filter_publication(queryset):
    """Фильтрует queryset по признаку опубликованности.

    Учитывает:
    - флаг is_published самого поста;
    - флаг is_published категории;
    - дату публикации (pub_date) не позднее текущего времени.
    """
    return queryset.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    )


def annotation_posts_number_comments(queryset):
    """Аннотирует queryset количеством комментариев к каждому посту.

    После annotate() обязательно задаём сортировку явно, так как
    порядок по умолчанию из Meta может конфликтовать с GROUP BY.
    """
    return queryset.annotate(
        comment_count=Count('comments')
    ).order_by('-pub_date')
