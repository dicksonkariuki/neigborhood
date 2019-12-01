from django.db import models

class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return self.hood_name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def search_neighbourhood(cls,hood_id):
        hood = cls.objects.get(id=hood_id)
        return hood 

    def update_hood(self,name):
        self.hood_name = name
        self.save()
