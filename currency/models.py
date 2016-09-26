from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Currencies(models.Model):
    timestamp = models.DateTimeField()
    aed = models.DecimalField(..., max_digits=19, decimal_places=10)
    bnd= models.DecimalField(..., max_digits=19, decimal_places=10)
    brl = models.DecimalField(..., max_digits=19, decimal_places=10)
    cad = models.DecimalField(..., max_digits=19, decimal_places=10)
    clp = models.DecimalField(..., max_digits=19, decimal_places=10)
    cop = models.DecimalField(..., max_digits=19, decimal_places=10)
    egp = models.DecimalField(..., max_digits=19, decimal_places=10)
    irr = models.DecimalField(..., max_digits=19, decimal_places=10)
    jpy = models.DecimalField(..., max_digits=19, decimal_places=10)
    krw = models.DecimalField(..., max_digits=19, decimal_places=10)
    mmk = models.DecimalField(..., max_digits=19, decimal_places=10)
    nzd = models.DecimalField(..., max_digits=19, decimal_places=10)
    pkr = models.DecimalField(..., max_digits=19, decimal_places=10)
    qar = models.DecimalField(..., max_digits=19, decimal_places=10)
    rub = models.DecimalField(..., max_digits=19, decimal_places=10)
    sar = models.DecimalField(..., max_digits=19, decimal_places=10)
    sgd = models.DecimalField(..., max_digits=19, decimal_places=10)
    syp = models.DecimalField(..., max_digits=19, decimal_places=10)
    ttd = models.DecimalField(..., max_digits=19, decimal_places=10)

    def __str__(self):
        return self.email
