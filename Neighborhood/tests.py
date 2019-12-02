from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hood_name=Neighborhood(hood_name="Runda")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hood_name,Neighborhood))
