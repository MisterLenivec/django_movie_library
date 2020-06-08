from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Contact
from .forms import ContactForm
from .service import send


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    success_message = 'Вы успешно подписались на рассылку!'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
