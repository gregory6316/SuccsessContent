"""File with tests of custom_storage package."""

import os
import tempfile
from datetime import date, timedelta

from custom_storage import Storage

def test_storage_inited():
    """Test storage set_inited() and inited() methods."""
    with tempfile.NamedTemporaryFile(suffix='.dict', delete=False) as file:
        storage = Storage(file.name)

        try:
            assert not storage.inited()
            storage.set_inited()
            assert storage.inited()
        finally:
            file.close()
            os.unlink(file.name)

def test_storage_put_get():
    """Test storage put() and get() methods."""
    with tempfile.NamedTemporaryFile(suffix='.dict', delete=False) as file:
        storage = Storage(file.name)
        storage.set_inited()

        day1 = date.today()
        day2 = date.today() + timedelta(days=1)
        day3 = date.today() + timedelta(days=-1)

        storage.put('mood', day1, 5, "Great Day!")
        storage.put('mood', day2, 3, "Normal Day")
        storage.put('mood', day3, 2, "Bad sleep")

        try:
            assert storage.get_message('mood', day1) == "Great Day!"
            assert storage.get_message('mood', day2) == "Normal Day"
            assert storage.get_message('mood', day3) == "Bad sleep"

            assert storage.get_value('mood', day1) == 5
            assert storage.get_value('mood', day2) == 3
            assert storage.get_value('mood', day3) == 2
        finally:
            file.close()
            os.unlink(file.name)

def test_storage_put_today():
    """Test storage put_today() method."""
    with tempfile.NamedTemporaryFile(suffix='.dict', delete=False) as file:
        storage = Storage(file.name)
        storage.set_inited()

        day = date.today()
        storage.put_today('mood', 5, "Great Day!")

        try:
            assert storage.get_message('mood', day) == "Great Day!"
            assert storage.get_value('mood', day) == 5

            storage.put_today('mood', 3, "Regular Day")

            assert storage.get_message('mood', day) == "Regular Day"
            assert storage.get_value('mood', day) == 3
        finally:
            file.close()
            os.unlink(file.name)
