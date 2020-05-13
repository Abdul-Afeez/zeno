from django.test import TestCase
from csvapp.models import TestReport

report_id = 37390


class TestTestReport(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        TestReport.objects.create(report_id=report_id,
                                         temperature='1540.246686313794700000000000000000	',
                                         timestamp='2019-06-05 23:08:31.407799',
                                         duration='0 days 00:27:41.382812755')

    def test_duration_max_length(self):
        test_report = TestReport.objects.get(report_id=report_id)
        max_length = test_report._meta.get_field('duration').max_length
        self.assertEquals(max_length, 1000)

    def test_duration_field_label(self):
        test_report = TestReport.objects.get(report_id=report_id)
        field_label = test_report._meta.get_field('duration').verbose_name
        self.assertEquals(field_label, 'duration')

    def test_timestamp_max_length(self):
        test_report = TestReport.objects.get(report_id=report_id)
        max_length = test_report._meta.get_field('timestamp').max_length
        self.assertEquals(max_length, 60)

    def test_timestamp_field_label(self):
        test_report = TestReport.objects.get(report_id=report_id)
        field_label = test_report._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'timestamp')

    def test_created_at_auto_now_add(self):
        test_report = TestReport.objects.get(report_id=report_id)
        auto_now_add = test_report._meta.get_field('created_at').auto_now_add
        self.assertEquals(auto_now_add, True)
