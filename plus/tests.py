from django.test import TestCase
from django.contrib.auth.models import User
from models import testFuct

# Create your tests here.
class testFucta(TestCase):
    def test_db(self):
        print User.objects.all()
        #testFuct.objects.create(name="asd")
        print testFuct.objects.all()