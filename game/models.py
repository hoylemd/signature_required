from django.db import models

class Scene(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    art_path = models.CharField(max_length=100, default="", blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
            return self.title

class Option(models.Model):
    text = models.CharField(max_length=1000)
    scene = models.ForeignKey(Scene, related_name="scenes_options")
    destination = models.ForeignKey(Scene, related_name="option_destinations")
    change_text_string = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
            return (self.text[:13] + '...') if len(self.text) > 16 else self.text
