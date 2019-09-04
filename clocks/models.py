from django.db import models

class Note(models.Model):
        header = models.CharField(max_length=200)
        body = models.TextField(max_length=2000)

class Clock(models.Model):
        lengths = [(8, '8-hours'), (6, '6-hours'), (4, '4-hours')]
        types = [('project', 'Projects Clock'), ('campain', 'Campain Clock'), ('heal', 'Healing Clock'), ('faction', 'Faction Clock'), ('other', 'Other')]
        
        title = models.CharField(max_length=100, blank=True)
        clock_type = models.CharField(max_length=10, choices=types, default='other')
        clock_length = models.PositiveSmallIntegerField(choices=lengths, default=4)
        compleation = models.PositiveSmallIntegerField(default=0)
        description = models.TextField(max_length=600, blank=True)
        following_clock = models.ManyToManyField('Clock', blank=True)

        def increase(self):
                if self.compleation < self.clock_length:
                        self.compleation += 1
                        self.save()

        def decrease(self):
                if self.compleation > 0:
                        self.compleation -= 1
                        self.save()

        def display(self):
                return "clocks\\images\\" + "Progress Clock " + str(self.clock_length) + "-" + str(self.compleation) + ".png"

        def __str__(self):
                return self.title

class Ability(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(max_length=600)

class Action(models.Model):
        attributes = [('insight', 'Insight'), ('prowess', 'Prowess'), ('resolve', 'Resolve')]
        attribute = models.CharField(max_length=10, choices=attributes)
        name = models.CharField(max_length=100)
        score = models.PositiveSmallIntegerField(default=0)

class Character(models.Model):
        playbooks = [('cutter', 'Cutter'), ('hound', 'Hound'), ('leech', 'Leech'), ('lurk', 'Lurk'), ('slide', 'Slide'), ('spider', 'Spider'), ('whisper', 'Whisper'), ('ghost', 'Ghost'), ('vampire', 'Vampire'), ('hull', 'Hull')]
        heritages = [('ako', 'Akoros'), ('dag', 'Dagger Isles'), ('irv', 'Iruvia'), ('sev', 'Severos'), ('sko', 'Skovlan'), ('tyc', 'Tycheros')]
        backgrounds = [('aca', 'Academic'), ('lab', 'Labor'), ('law', 'Law'), ('tra', 'Trade'), ('mil', 'Military'), ('nob', 'Noble'), ('und', 'Underworld')]
        vices = [('fai', 'Faith'), ('gam', 'Gambling'), ('obl', 'Obligation'), ('ple', 'Pleasure'), ('stu', 'Stupor'), ('wei', 'Weird')]
        states = [('alive', 'Alive'), ('away', 'Away'), ('incar', 'Incarcerated'), ('dead', 'Dead')]

        playbook = models.CharField(max_length=10, choices=playbooks)
        heritage = models.CharField(max_length=3, choices=heritages)
        background = models.CharField(max_length=3, choices=backgrounds)
        vice = models.CharField(max_length=3, choices=vices)
        
        name = models.CharField(max_length=100)
        alias = models.CharField(max_length=100)
        look = models.TextField(max_length=600)
        healing_clock = models.OneToOneField(Clock, blank=False, on_delete=models.CASCADE)

        coins = models.PositiveSmallIntegerField(default=0)

        cold = models.BooleanField(default=False)
        haunted = models.BooleanField(default=False)
        obsessed = models.BooleanField(default=False)
        paranoid = models.BooleanField(default=False)
        reckless = models.BooleanField(default=False)
        soft = models.BooleanField(default=False)
        unstable = models.BooleanField(default=False)
        vicious = models.BooleanField(default=False)

        armor_light = models.BooleanField(default=False)
        armor_heavy = models.BooleanField(default=False)
        armor_special = models.BooleanField(default=False)

        harm_1_1 = models.CharField(max_length=300)
        harm_1_2 = models.CharField(max_length=300)
        harm_2_1 = models.CharField(max_length=300)
        harm_2_2 = models.CharField(max_length=300)
        harm_3 = models.CharField(max_length=300)


        friend = models.TextField(max_length=300)
        foe = models.TextField(max_length=300)

        abilities = models.ForeignKey(Ability, blank=True, on_delete=models.CASCADE)
        action = models.ForeignKey(Action, blank=True, on_delete=models.CASCADE)
        notes = models.ForeignKey(Note, blank=True, on_delete=models.CASCADE)

class Crew(models.Model):
        pass

class Turf(models.Model):
        pass

class Campain(models.Model):
        pass


