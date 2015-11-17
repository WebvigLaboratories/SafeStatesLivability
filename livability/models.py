from django.db import models

class Tools(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200,null=True,blank=True)
    url = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    year_developed = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Community_Size(models.Model):
    SIZE_CHOICES = (
        (1, '1-Urban'),
        (2, '2-Rural'),
    )
    toolname = models.ForeignKey(Tools)
    selection = models.SmallIntegerField(choices=SIZE_CHOICES)
    # 1 = Urban, 2 = Rural

    class Meta:
        ordering = ['toolname__name']

    def selection_verbose(self):
        return dict(Community_Size.SIZE_CHOICES)[self.selection]

class Assessment_Focus(models.Model):
    FOCUS_CHOICES = (
        (1, '1-Development or Transportation Projects'),
        (2, '2-Physical Environment of a Community, Neighborhood, or School'),
        (3, '3-Policy, Plan, Codes, or Standards'),
        (4, '4-Walkability, Bikability, and/or Transit Access'),
    )
    toolname = models.ForeignKey(Tools)
    selection = models.SmallIntegerField(choices=FOCUS_CHOICES)
    # 1 = Development or Transportation Project, 2 = Physical Environment of a Community, Neighborhood, or School
    # 3 = Policy, Plan, Codes, or Standards 4 = Walkability, Bikability, and/or Transit access

    class Meta:
        ordering = ['toolname__name']

    def selection_verbose(self):
        return dict(Assessment_Focus.FOCUS_CHOICES)[self.selection]

class Audience(models.Model):
    AUDIENCE_CHOICES = (
        (1, '1-Elected Officials'),
        (2, '2-Laypersons'),
        (3, '3-Planners'),
        (4, '4-PH Professionals'),
        (5, '5-School Officials'),
    )
    toolname = models.ForeignKey(Tools)
    selection = models.SmallIntegerField(choices=AUDIENCE_CHOICES)
    # 1 = Elected Officials, 2 = Laypersons, 3 = Planners, 4 = PH Professionals, 5 = School officials

    class Meta:
        ordering = ['toolname__name']

    def selection_verbose(self):
        return dict(Audience.AUDIENCE_CHOICES)[self.selection]

class Topics(models.Model):
    TOPIC_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )
    toolname = models.OneToOneField(Tools)
    # Yes/no 1/0
    q_transportation = models.SmallIntegerField(choices=TOPIC_CHOICES) #Transportation Choices & Safe, Multimodal Neighborhood
    q_housing = models.SmallIntegerField(choices=TOPIC_CHOICES) # Equitable Housing Options
    q_investment = models.SmallIntegerField(choices=TOPIC_CHOICES) # Investment in Existing Communities
    q_compact = models.SmallIntegerField(choices=TOPIC_CHOICES) # Compact, Mixed-use Design
    q_health = models.SmallIntegerField(choices=TOPIC_CHOICES) # Health-Promoting Design and Policies
    q_preservation = models.SmallIntegerField(choices=TOPIC_CHOICES) # Preservation Rural Areas & Open Space

    class Meta:
        ordering = ['toolname__name']

    def transportation_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_transportation]
    def housing_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_housing]
    def investment_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_investment]
    def compact_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_compact]
    def health_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_health]
    def preservation_verbose(self):
        return dict(Topics.TOPIC_CHOICES)[self.q_preservation]