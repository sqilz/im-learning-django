import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Question


def create_question(question_text, days):
    """Creates a question with the given `question_text` and published the given
     number of `days` offset to now (negative for questions published in the
     past, positive for questions that have yet to be published
    """


class QuestionMethodTests(TestCase):
    def test_Was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for qeustions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whise
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_Recent_question(self):
        """
        was_published_recently() sould return True for questions whose
        pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
