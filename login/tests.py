from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase, TestCase, Client

from django.urls import reverse,resolve

from django.contrib.auth.models import User

from login.views import user_account 

#    test 1

def test_case_user_account_url(self):

        url=reverse('user_account')

        self.assertEquals(resolve(url).func,user_account)


