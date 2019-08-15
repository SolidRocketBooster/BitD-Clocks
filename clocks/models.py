from django.db import models


class Clock(models.Model):
        types = [(8, '8-hours'), (6, '6-hours'), (4, '4-hours')]
        
        title = models.CharField(max_length=100)
        clock_type = models.PositiveSmallIntegerField(choices=types)
        compleation = models.PositiveSmallIntegerField(default = 0)
        description = models.TextField(max_length=600)
        following_clock = models.ManyToManyField('Clock', blank=True)

        def display(self):
                return "clocks\\images\\" + "Progress Clock " + str(self.clock_type) + "-" + str(self.compleation) + ".png"

        def __str__(self):
                return self.title

