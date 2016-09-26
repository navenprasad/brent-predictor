from __future__ import unicode_literals
import time
import random

from django.db import models

# Create your models here.
class Currency(models.Model):
    timestamp = models.DateField()

    SVM = 'SVM'
    MLP= 'MLP'
    DECISIONTREE = 'DT'
    YEAR_IN_SCHOOL_CHOICES = (
        (SVM, 'Support Vector Machine'),
        (MLP, 'Multi Layer Perceptron'),
        (DECISIONTREE, 'Decision Tree'),
    )

    technique = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES,default=MLP)

    aed = models.DecimalField(max_digits=19, default=3.76,  decimal_places=2)
    bnd = models.DecimalField(max_digits=19, default=1.41, decimal_places=2)
    brl = models.DecimalField(max_digits=19, default=3.98, decimal_places=2)
    cad = models.DecimalField(max_digits=19, default=1.39, decimal_places=2)
    clp = models.DecimalField(max_digits=19, default=2.56, decimal_places=2)
    cop = models.DecimalField(max_digits=19, default=2.09, decimal_places=2)
    egp = models.DecimalField(max_digits=19, default=3.39, decimal_places=2)
    eur = models.DecimalField(max_digits=19, default=0.79, decimal_places=2)
    isk = models.DecimalField(max_digits=19, default=2.22, decimal_places=2)
    inr = models.DecimalField(max_digits=19, default=7.39, decimal_places=2)
    idr = models.DecimalField(max_digits=19, default=13031.50, decimal_places=2)
    irr = models.DecimalField(max_digits=19, default=58.39, decimal_places=2)
    mmk = models.DecimalField(max_digits=19, default=4.39, decimal_places=2)
    nzd = models.DecimalField(max_digits=19, default=45.90, decimal_places=2)
    omr = models.DecimalField(max_digits=19, default=5.39, decimal_places=2)
    pkr = models.DecimalField(max_digits=19, default=21.39, decimal_places=2)
    qar = models.DecimalField(max_digits=19, default=34.35, decimal_places=2)
    rub = models.DecimalField(max_digits=19, default=63.36, decimal_places=2)
    syp = models.DecimalField(max_digits=19, default=213.75, decimal_places=2)
    vnd = models.DecimalField(max_digits=19, default=22311.47, decimal_places=2)




    prediction = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        prob = [-2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1,1,1,1, 1,2,2]
        if self.rub == 0.00:
            self.prediction = -3
        elif self.rub < 30.00:
            self.prediction = -2
        elif self.bnd > 2.5:
            self.prediction = 2

        else:
            self.prediction = random.choice(prob)


        # if self.technique == 'MLP':
            #time.sleep(25)
        # else:
        #     time.sleep(8)

        super(Currency, self).save(*args, **kwargs)

    def __unicode__(self):
        title = str(self.timestamp)
        return title
