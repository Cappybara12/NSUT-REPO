from django.conf import settings
from django.db import models
import binascii
import os
from django.utils.translation import gettext_lazy as _


# Create your models here.


class MultiToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, null=True)
    user = models.ForeignKey(  # changed from OneToOne to ForeignKey
        settings.AUTH_USER_MODEL, related_name='tokens',
        on_delete=models.CASCADE, verbose_name=_("User")
    )

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
