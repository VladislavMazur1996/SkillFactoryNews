from celery import shared_task
from .models import Post, Category
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def daily_post():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(creating_dt__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscriber = set(Category.objects.filter(name__in=categories).values_list('subscriber__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': 'http://127.0.0.1:8000/',
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='Skillfactory1@yandex.ru',
        to=subscriber,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'http://127.0.0.1:8000/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body=preview,
        from_email='Skillfactory1@yandex.ru',
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
