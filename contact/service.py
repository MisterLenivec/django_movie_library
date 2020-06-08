from django.core.mail import send_mail
from django_movie_library.settings import EMAIL_HOST_USER


def send(user_email):
    send_mail(
        'Вы подписались на рассылку Django Movie Library.',
        'Мы будем присылать вам новости.',
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
