from django.db import models

# asm imports
from assets_register.models import Assets, currency


class Disposal(models.Model):

    modes_of_disposal = (
        ('sl', 'Sale'),
        ('dn', 'Donation'),
        ('ls', 'Loss'),
    )

    disposal_status = (
        ('dsp', 'Disposed'),
        ('emk', 'Earmarked'),
    )

    asset = models.OneToOneField(Assets, null=False, blank=False, db_index=True)
    mode_of_disposal = models.CharField(max_length=2, null=True, blank=True, choices=modes_of_disposal)
    reason = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=3, null=False, blank=False, choices=disposal_status, default='emk')
    disposal_value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)
    disposal_currency = models.CharField(max_length=5, null=False, blank=True, default='KES', choices=currency)
    disposal_age = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    date_disposed = models.DateField(null=True)

    def __str__(self):
        return self.asset
