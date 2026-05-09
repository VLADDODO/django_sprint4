from django.db import models


class CreatedModel(models.Model):
    """Абстрактная модель с датой создания."""

    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('created_at',)


class PublishedCreatedModel(CreatedModel):
    """Абстрактная модель с флагом публикации и датой создания."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )

    class Meta(CreatedModel.Meta):
        abstract = True


class TitleModel(models.Model):
    """Абстрактная модель с заголовком."""

    title = models.CharField(
        'Заголовок',
        max_length=256,
    )

    class Meta:
        abstract = True
