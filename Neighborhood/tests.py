from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hoods=Neighborhood(hood_name="Runda",hood_location="kitisuru",occupants=21)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hoods,Neighborhood))

    def test_save_method(self):
        self.hoods.save_hood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)