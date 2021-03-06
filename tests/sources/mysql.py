import os
from .base import SourceTestCase


HOST = os.environ.get('MYSQL_HOST', 'localhost')
USER = os.environ.get('MYSQL_USER', '')
PASSWORD = os.environ.get('MYSQL_PASSWORD', '')


class TestCase(SourceTestCase):
    generator = 'mysql'
    output_name = 'chinook_mysql.json'

    def generate(self):
        client = self.module.Client(database='chinook',
                                    host=HOST,
                                    user=USER,
                                    password=PASSWORD)

        return client.generate()
