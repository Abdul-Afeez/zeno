from django.test import TestCase
from csvapp.models import Log

request = 'localhost:9000 GET'
log_id = None


class TestLog(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Log.objects.create(request=request)

    def test_request_max_length(self):
        log = Log(request=request)
        max_length = log._meta.get_field('request').max_length
        self.assertEquals(max_length, 4000)

    def test_request_field_label(self):
        log = Log(request=request)
        field_label = log._meta.get_field('request').verbose_name
        self.assertEquals(field_label, 'request')

    def test_created_at_auto_now_add(self):
        log = Log(request=request)
        auto_now_add = log._meta.get_field('created_at').auto_now_add
        self.assertEquals(auto_now_add, True)