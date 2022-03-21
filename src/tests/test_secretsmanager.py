from secretsmanager.secretsmanager import SecretsManager
import unittest
from unittest.mock import patch
import pytest
import sys


def test_output(awssecrets_connection):
    assert awssecrets_connection.region_name == 'us-west-2'
    assert awssecrets_connection.db_secret.has_key('host') == True
    assert awssecrets_connection.db_secret.has_key('username') == True
    assert awssecrets_connection.db_secret.has_key('password') == True
    assert awssecrets_connection.db_secret.has_key('port') == True
    assert awssecrets_connection.db_secret.has_key('dbname') == True