from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid:
        nome = request.POST.get('name')
        sendTo = request.POST.get('email')
        message = request.POST.get('message')
        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {} <{}> Escreveu: \n \n {}".format(nome, sendTo, message),
            "no-replay@inbox.mailtrap.io",
            ["murilo.martinss@hotmail.com"],
            reply_to=[sendTo]
        )
        try:
            email.send()
            send = True
        except:
            send = False
    
    context = {
        'form': ContactForm,
        'success': send
    }

    return render(request, 'contact/contact.html', context)


