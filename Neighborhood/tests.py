from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hoods=Neighborhood(id =1 ,hood_name="Runda",hood_location="kitisuru",occupants=21)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hoods,Neighborhood))

    def test_save_method(self):
        self.hoods.save_hood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)
    def test_delete_method(self):
        self.hoods.delete_hood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)==0)
    def test_search_neighborhood(self):
        self.hoods.save_hood()
        neighborhood=Neighborhood.search_neighbourhood(1)
        self.assertTrue(neighborhood.hood_name,"runda")
    def test_update_hood(self):
        self.hoods.save_hood()
        neighborhood=Neighborhood.search_neighbourhood(1)
        neighborhood.hoods="syokimau"
        self.assertTrue(neighborhood.hood_name,"syokimau")

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,user_location='Turkana')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_hood = Neighborhood(id=1,hood_name='Mtaani',hood_location="Nairobi",occupants=10)
        self.new_hood.save_hood()
        self.new_biz = Business(id=1,business_name='Bizna',business_email="biz@mail.com",business_owner=self.new_user,business_hood_id=self.new_hood)            

    def test_instance(self):
        self.assertTrue(isinstance(self.new_biz,Business))

    def test_save_instance(self):
        self.new_biz.save_business()
        biznas = Business.objects.all()
        self.assertTrue(len(biznas)>0)

    def test_delete_instance(self):
        self.new_biz.delete_business()
        biznas = Business.objects.all()
        self.assertTrue(len(biznas)==0)

    def test_find_biz(self):
        self.new_biz.save_business()
        bizz = Business.search_business(1)
        self.assertEqual(bizz.business_name,'Bizna')

    def test_update_business(self):
        self.new_biz.save_business()
        bizz = Business.search_business(1)
        bizz.business_name = 'Updated Bizna'
        self.assertEqual(bizz.business_name,'Updated Bizna')



