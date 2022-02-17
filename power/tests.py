from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase, TestCase, Client

from django.urls import reverse,resolve

from django.contrib.auth.models import User

from power.views import about, contact, gallery, jobform, jobs, req_doc, visa_p, visa_step



class TestUrls(SimpleTestCase):

   

    def test_case_about_url(self):

        url=reverse('about')

        self.assertEquals(resolve(url).func,about)



    def test_case_gallery_url(self):

        url=reverse('gallery')

        self.assertEquals(resolve(url).func,gallery)


    def test_case_contact_url(self):

        url=reverse('contact')

        self.assertEquals(resolve(url).func,contact)


    def test_case_reqDoc_url(self):

        url=reverse('reqDoc')

        self.assertEquals(resolve(url).func,req_doc)


    def test_case_jobs_url(self):

        url=reverse('jobs')

        self.assertEquals(resolve(url).func,jobs)


    def test_case_visa_p_url(self):

        url=reverse('visa_p')

        self.assertEquals(resolve(url).func,visa_p)


    def test_case_visa_step_url(self):

        url=reverse('visa_step')

        self.assertEquals(resolve(url).func,visa_step)


    def test_case_jobform_url(self):

        url=reverse('jobform',args=[2])

        self.assertEquals(resolve(url).func,jobform)

  
