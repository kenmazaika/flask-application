import pytest

from flaskr import create_app
from flask import g, session

def test_config():
  assert not create_app().test_config
  assert create_app({'TESTING': True}).testing


def test_hello(client):
  with client:
    response = client.get('/')
    assert 'http://localhost/blog/' == response.headers['Location']