from djoser import email
from django.contrib.auth.tokens import default_token_generator

from djoser import utils
from djoser.conf import settings

class ActivationEmailCustomized(email.ActivationEmail):

    template_name = "emails/activation.html"

class ConfirmationEmailCustomized(email.ConfirmationEmail):

    template_name = "emails/confirmation.html"

class PasswordResetEmailCustomized(email.PasswordResetEmail):

    template_name = "emails/passwordReset.html"

class PasswordResetConfirmationEmailCustomized(email.PasswordChangedConfirmationEmail):

    template_name = "emails/passwordResetConfirmation.html"