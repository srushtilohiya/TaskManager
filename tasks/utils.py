# tasks/utils.py
from django.core.mail import send_mail
from django.conf import settings
from tasks.models import AdminInvite

def send_invitations():
    invites = AdminInvite.objects.all()  # Get all invites
    for invite in invites:
        subject = "You're Invited to Join the Task Manager App!"
        message = "Click the link to join: http://localhost:8000/accounts/signup/"  # Replace with your signup link
        recipient = invite.email
        
        # Send the email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

    return f"Invitations sent to {len(invites)} users."
