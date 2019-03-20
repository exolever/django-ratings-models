#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ratings
------------

Tests for `ratings` models module.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from ratings import models


class TestRatings(TestCase):

    def setUp(self):
        pass

    def test_simple_rating_model(self):
        # Data
        user_from = get_user_model().objects.create()
        overall_rating = models.OverallRating.objects.create()

        # Do action
        rating = models.Rating.objects.create(user=user_from, rating=4, overall_rating=overall_rating)

        # Asserts
        self.assertTrue(rating.pk)
        self.assertEqual(rating.user, user_from)

    def test_simple_overall_rating_model_update(self):
        # Data
        user_from = get_user_model().objects.create()
        overall_rating = models.OverallRating.objects.create()
        rating = models.Rating.objects.create(user=user_from, rating=4, overall_rating=overall_rating)

        # Do action
        overall_rating.update()

        # Asserts
        self.assertEqual(overall_rating.rating, rating.rating)

    def tearDown(self):
        pass
