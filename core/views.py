from django.shortcuts import render, get_object_or_404
from .models import Leadz_Reup, Contact_Form_Submission
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    leadz_reup = get_object_or_404(Leadz_Reup, pk=1)
    return render(request, 'index.html', {'leadz_reup': leadz_reup})


def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        services = request.POST.getlist('services')

        contact_form = Contact_Form_Submission(
            name = name,
            email = email,
            phone_number = phone_number,
            message = message,
            services = services,
        )
       
        contact_form.save()
        
        leadz_reup = get_object_or_404(Leadz_Reup, pk=1)

        email_subject = 'Contact Form Submission'
        email_body = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'message': message,
            'leadz_reup_phone_number' : leadz_reup.phone_number,
            'services': services,
        })

        # Send the email
        msg = EmailMessage(email_subject, email_body, to=[email, 'lynkslocal@gmail.com'])
        msg.content_subtype = 'html'
        msg.send()

        return render(request, 'index.html', {'leadz_reup': leadz_reup})






