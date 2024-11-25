from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Task, AdminInvite

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

@admin.register(AdminInvite)
class AdminInviteAdmin(admin.ModelAdmin):
    list_display = ('email', 'sent_at')
    actions = ['send_invitation_email']

    def send_invitation_email(self, request, queryset):
        for invite in queryset:
            subject = "You're Invited to Join the Task Manager App!"
            message = (
                f"Hi,\n\n"
                f"You have been invited to join the Task Manager App. "
                f"Click the link below to sign up:\n\n"
                f"http://localhost:8000/accounts/signup/"
            )
            send_mail(subject, message, settings.EMAIL_HOST_USER, [invite.email])
        self.message_user(request, f"{queryset.count()} invitation(s) sent!")

    send_invitation_email.short_description = "Send Invitation Email"
