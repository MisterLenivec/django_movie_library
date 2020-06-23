from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Contact
from .forms import ContactForm
from .service import send
from .tasks import send_spam_email


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    success_message = 'Вы успешно подписались на рассылку!'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
