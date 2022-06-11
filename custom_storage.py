"""Module implementing interface to work with kivi storage.

Usage Example:
>>> from custom_storage import Storage
>>> from datetime import date
>>>
>>> name = "tmp.dict"
>>> storage = Storage(name)
>>>
>>> day = date.today()
>>> todays_rating = 5
>>> message = "Great Day"
>>> storage.put('mood', day, todays_rating, message)
>>>
>>> storage.get_message('mood', day)
Great Day
>>> storage.get_value('mood', day)
5
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

    def put(self, key, day, value, msg):
        """Add day to history dict by key in storage.

        Args:
        key: str - key containing activity;
        day: datetime.date;
        value: int - value of todays activity (1-5);
        msg: str - message of the day;
        """
        history_dict = self.get(key)
        history_dict[day] = {'value': value, 'msg': msg}
        self.storage.put(key, history=history_dict)

    def put_today(self, key, value, msg):
        """Add current day to history dict by key in storage.

        Args:
        key: str - key containing activity;
        value: int - value of todays activity (1-5);
        msg: str - message of the day;
        """
        day = date.today()
        self.put(key, day, value, msg)

    def get(self, key):
        """Return entire history dict by key in storage.

        Args:
        key: str - key containing history dict;

        Returns:
        dict - history dict if exists else None
        """
        if not self.storage.exists(key):
            self.storage.put(key, history={})
        if "history" not in self.storage.get(key):
            self.storage.put(key, history={})

        return self.storage.get(key).get("history")

    def get_message(self, key, day):
        """Return day's message.

        Args:
        key: str - key containing history dict;
        day: datetime.date;

        Returns:
        str - day's message;
        """
        history_dict = self.get(key)
        item = history_dict.get(day, {"value": None, "msg": ""})
        return item["msg"]

    def get_value(self, key, day):
        """Return day's value.

        Args:
        key: str - key containing history dict;
        day: datetime.date;

        Returns:
        int - day's value;
        """
        history_dict = self.get(key)
        item = history_dict.get(day, {"value": None, "msg": ""})
        return item["value"]
