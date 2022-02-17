from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase, TestCase, Client

from django.urls import reverse,resolve

from django.contrib.auth.models import User
from admins.views import addVacancy, appliedDetail, appliedVacancy, editVacancy, msgrequest, totalusers, totalvacancy





class TestUrls(SimpleTestCase):

#    test 1

    def test_case_totaluser_url(self):

        url=reverse('totaluser')

        self.assertEquals(resolve(url).func,totalusers)

# test 2

    def test_case_appliedvacancy_url(self):

        url=reverse('appliedvacancy')

        self.assertEquals(resolve(url).func,appliedVacancy)

# test 3

    def test_case_totalvacacancy_url(self):

        url=reverse('totalvacancy')

        self.assertEquals(resolve(url).func,totalvacancy)


# test 4

    def test_case_msgrequest_url(self):

        url=reverse('msgrequest')

        self.assertEquals(resolve(url).func,msgrequest)

# test 5
        
    def test_case_addvacancy_url(self):

        url=reverse('addvacancy')

        self.assertEquals(resolve(url).func,addVacancy)


# test 6


    def test_case_editvacancy_url(self):

        url=reverse('editvacancy',args=[1])

        self.assertEquals(resolve(url).func,editVacancy)


