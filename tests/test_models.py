#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ratings
------------

Tests for `ratings` models module.
"""

from django.test import TestCase

from ratings import models


class TestRatings(TestCase):

    def setUp(self):
        pass

    def test_something(self):
        rating = models.Rating(rating=4)
        print(rating)

    def tearDown(self):
        pass
