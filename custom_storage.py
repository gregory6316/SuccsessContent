"""Module implementing interface to work with kivi storage.

Usage Example:
>>> from custom_storage import Storage
>>>
>>> name = "tmp.dict"
>>> storage = Storage(name)
>>>
>>> todays_rating = 5
>>> storage.put_history('mood', todays_rating)
>>>
>>> storage.get_history('mood')
[5]
>>> new_day_rating = 4
>>> storage.put_history('mood', new_day_rating)
>>> storage.get_history('mood')
[5, 4]
>>>
>>> storage.get_days_passed('mood')
0
>>> storage.update_last_day('mood')
>>> # After several days
>>> storage.get_days_passed('mood')
5
>>> days_passed = storage.get_days_passed('mood')
>>> storage.append_zeros('mood', passed_days - 1)
>>> storage.get_history('mood')
[5, 4, 0, 0, 0, 0]


Tips:
1. After putting new value to history (storage.put_history)
   don't forget to update current day (storage.update_last_day)
2. If you want to append zeros to history (storage.append_zeros)
   with number of passed days (storage.get_days_passed)
   subtract 1 from passed days, because "today" - "yesterday" = 1,
   and there should not be additional 0.
"""
from datetime import date
from kivy.storage.dictstore import DictStore

class Storage:
    """Class Storage."""

    def __init__(self, storage_name):
        """Initialize DictStorage.

        Args:
        storage_name: str - name of storage;
        """
        self.storage = DictStore(storage_name)

    def inited(self):
        """Get inited."""
        return self.storage.exists("inited")

    def set_inited(self):
        """Set inited as True."""
        if not self.storage.exists("inited"):
            self.storage.put("inited", value=True)

    def put_history(self, key, value):
        """Append value to history list by key in storage.

        Args:
        key: str - key containing history list and last day;
        value - value to be appended to history;
        """
        history = self.get_history(key)
        print('Got history:', history)
        history.append(value)
        print('Elem appended:', history)
        self.storage.put(key=history)
        #self.storage.store_sync()
        #print('Synced')
        print('New history:')
        print(self.storage.get(key).get("history"))

    def get_history(self, key):
        """Return entire history list by key in storage.

        Args:
        key: str - key containing history list and last day;

        Returns:
        list - history list if exists else None
        """
        if not self.storage.exists(key):
            self.storage.put(key, history=[])
        if "history" not in self.storage.get(key):
            self.storage.get(key)['history'] = []
            self.storage.store_sync()
        return self.storage.get(key).get("history")

    def pop_from_history(self, key):
        """Erase last value from history and return it.

        Args:
        key: str - key containing history list and last day;
        """
        history = self.get_history(key)
        if len(history) > 0:
            elem = history.pop()
            self.storage.store_sync()
            return elem
        return None

    def set_last_day(self, key, day):
        """Set the last day stored by key to new day.

        Args:
        key: str - key where day and history are stored;
        day: datetime.date - new day to be set;
        """
        if not self.storage.exists(key):
            self.storage.put(key, last_day=day)
        else:
            self.storage.get(key)["last_day"] = day
            self.storage.store_sync()


    def get_last_day(self, key):
        """Get the last day stored by key to new day.

        Args:
        key: str - key where day and history are stored;
        """
        if not self.storage.exists(key):
            self.storage.put(key, last_day=None)
        return self.storage.get(key).get("last_day", None)

    def update_last_day(self, key):
        """Update last day stored in storage by key.

        Args:
        key: str - key containing value of last day and history list;
        """
        today = date.today()
        self.set_last_day(key, today)

    def get_days_passed(self, key):
        """Return number of passed days from current day day stored by key.

        Args:
        key: str - key containing value of last day and history list;
        """
        today = date.today()
        if not self.storage.exists(key):
            self.storage.put(key, last_day=today)
        last_day = self.storage.get(key).get('last_day', today)
        if not last_day:
            last_day = today
        return (today-last_day).days

    def append_zeros(self, key, num):
        """Append zero values to history list by key.

        Args:
        key: str - key containing history list and last day;
        num: int - number of zeros to be put in list;
        """
        for _ in range(num):
            self.put_history(key, 0)
