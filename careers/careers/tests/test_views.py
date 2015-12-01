from django.core.urlresolvers import reverse

from careers.base.tests import TestCase
from careers.careers.tests import PositionFactory as JobvitePositionFactory
from careers.django_workable.tests import PositionFactory as WorkablePositionFactory


class PositionTests(TestCase):
    """Tests static pages for careers"""
    def test_position_case_sensitive_match(self):
        """
        Validate that a position match is returned from a case-sensitive job id and it doesn't
        raise a multiple records error.
        """
        job_id_1 = 'oflWVfwb'
        job_id_2 = 'oFlWVfwB'
        JobvitePositionFactory.create(job_id=job_id_1)
        JobvitePositionFactory.create(job_id=job_id_2)

        url = reverse('careers.position', kwargs={'job_id': job_id_1})
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['position'].job_id, job_id_1)

        url = reverse('careers.position', kwargs={'job_id': job_id_2})
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['position'].job_id, job_id_2)


class WorkablePositionDetailViewTests(TestCase):
    def test_base(self):
        position_1 = WorkablePositionFactory.create(title='bbb')
        position_2 = WorkablePositionFactory.create(category=position_1.category, title='aaa')
        status = self.client.get(reverse('careers.workable_position',
                                         kwargs={'shortcode': position_1.shortcode}))
        self.assertEqual(status.context_data['positions'], [position_2, position_1])
        self.assertEqual(status.context_data['position'], position_1)
