import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError


import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_invalid_add(self):
        url = f"{BASE_URL}/calc/add/a/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
    
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_invalid_substract(self):
        url = f"{BASE_URL}/calc/substract/a/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_invalid_multiply(self):
        url = f"{BASE_URL}/calc/multiply/a/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
    
    def test_api_invalid_divide(self):
        url = f"{BASE_URL}/calc/divide/a/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_invalid_power(self):
        url = f"{BASE_URL}/calc/power/a/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_invalid_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/-9"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_invalid_log10(self):
        url = f"{BASE_URL}/calc/log10/-100"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Expected HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
