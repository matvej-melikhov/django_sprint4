from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

MAX_LENTH_TITLE = 256


class BaseModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
        default=True,
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=256,
        help_text='Максимальная длина строки - 256 символов',
    )
    text = models.TextField(
        'Текст',
        help_text='Текст публикации',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации',
        help_text='Выберите автора публикации'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        verbose_name='Местоположение',
        help_text='Выберите местоположение'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        verbose_name='Категория',
        help_text='Выберите категорию публикации'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='media/',
        blank=True,
        help_text='Изображение к публикации'
    )

    @property
    def comment_count(self):
        return self.comments.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)


class Category(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=MAX_LENTH_TITLE,
        help_text='Максимальная длина 256 символов'
    )
    description = models.TextField(
        'Описание',
        help_text='Описание категории'
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(BaseModel):
    name = models.CharField(
        'Название места',
        max_length=MAX_LENTH_TITLE,
        help_text='Максимальная длина 256 символов'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(
        'Текст комментария',
        help_text='Введите текст комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация',
        help_text='Выберите публикацию'
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Выберите автора комментария'
    )

    class Meta:
        ordering = ('created_at',)
