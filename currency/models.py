from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Currency(models.Model):
    timestamp = models.DateField()
    aed = models.DecimalField(max_digits=19, default=3.76,  decimal_places=2)
    bnd = models.DecimalField(max_digits=19, default=1.41, decimal_places=2)
    brl = models.DecimalField(max_digits=19, default=3.98, decimal_places=2)
    prediction = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.prediction = self.aed - self.bnd - self.brl
        super(Currency, self).save(*args, **kwargs)

    def __unicode__(self):
        title = str(self.timestamp)
        return title
