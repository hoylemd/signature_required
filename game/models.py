from django.db import models
from django_extensions.db.fields import UUIDField

class Scene(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    art_path = models.CharField(max_length=100, default="", blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
            return self.title

class Session(models.Model):
    uuid = UUIDField()
    scene = models.ForeignKey(Scene, related_name="session_scene", default=0)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, default="")
    def __unicode__(self):
        return self.name

class Inventory(models.Model):
    session = models.ForeignKey(Session, related_name="inventory_session", default=0)
    item = models.ForeignKey(Item, related_name="inventory_item", default = 0)

class Option(models.Model):
    text = models.CharField(max_length=1000)
    scene = models.ForeignKey(Scene, related_name="scenes_options")
    destination = models.ForeignKey(Scene, related_name="option_destinations")
    change_text_string = models.CharField(max_length=1000, blank=True)
    required_item = models.ForeignKey(Item, related_name="option_item_required", null=True)
    prohibited_item = models.ForeignKey(Item, related_name="option_item_prohibited", null=True)
    def __unicode__(self):  # Python 3: def __str__(self):
            return (self.text[:13] + '...') if len(self.text) > 16 else self.text


