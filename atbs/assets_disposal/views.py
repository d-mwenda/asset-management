from django.shortcuts import render
from django.core.mail import EmailMessage

email = EmailMessage('Subject', 'Body', to=['dmurithi@christian-aid.org'])
email.send()
