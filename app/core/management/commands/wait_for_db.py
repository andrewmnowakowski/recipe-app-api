import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to pause execution until database is availble"""

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        db_con = None
        while not db_con:
            try:
                db_con = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable. Waiting one second.')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
