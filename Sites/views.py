from .                  import models
from .forms             import SayHelloForm
from django.conf        import settings
from django.contrib     import messages
from django.core.mail   import send_mail
from django.shortcuts   import render, redirect

def all(request):
    # Data for the view in all circumstances
    sites = models.Site.objects.all()
    last_site_is_loner = (models.Site.objects.count() % 2 != 0)
    view_data = {
        'last_site_is_loner': last_site_is_loner,
        'sites': sites
    }
    if request.method == 'POST':
        f = SayHelloForm(request.POST)
        if f.is_valid():
            # Email their comment to Alexander
            visitors_name = request.POST.get('name')
            visitors_email = request.POST.get('email')
            visitors_message = request.POST.get('message') + '\n\nFrom %(visitors_email)s.' % locals()
            message_subject = 'Message from %(visitors_name)s at iAlexander.io' % locals()
            sent = send_mail(message_subject, visitors_message, visitors_email, [settings.EMAIL_HOST_USER])
            if sent:
                # The message was sent
                view_data['hello_message_sent'] = True
                return render(request, 'all.html', view_data)
        else:
            # Form validation has failed
            view_data['say_hello_form'] = f
            view_data['say_hello_form_needs_display'] = 1
            return render(request, 'all.html', view_data)
    else:
        # Return the sites page
        return render(request, 'all.html', view_data)
