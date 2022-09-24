from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from petstagram import settings
from petstagram.accounts.models import Profile


@receiver(pre_save, sender=Profile)
def send_greeting_email(instance, *args, **kwargs):
    if Profile.objects.filter(user_id=instance.user_id):
        return

    subject = "Registration greetings"
    html_message = render_to_string('common/email-greeting.html', {'profile': instance})
    plain_message = strip_tags(html_message)
    to = instance.email
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [to], html_message=html_message)
