from django.db import models


class Asset(models.Model):

    asset_no = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.asset_no