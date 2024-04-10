import unittest
from datetime import datetime, timezone
from pytest.datetime_helpers import dt_now, dt_utc, dt_ts, dt_ts_def, dt_floor_day, dt_from_ts, shorten_date, dt_humanize, format_date, format_ms_time

import arrow

class TestDateTimeFunctions(unittest.TestCase):
    
    def test_dt_now(self):
        # Kiểm tra xem hàm dt_now() trả về một đối tượng datetime
        self.assertIsInstance(dt_now(), datetime)
    
    def test_dt_utc(self):
        # Kiểm tra xem hàm dt_utc() trả về một đối tượng datetime
        self.assertIsInstance(dt_utc(2024, 4, 10), datetime)
    
    def test_dt_ts(self):
        # Kiểm tra xem hàm dt_ts() trả về một số nguyên
        self.assertIsInstance(dt_ts(), int)
    
    def test_dt_ts_def(self):
        # Kiểm tra xem hàm dt_ts_def() trả về một số nguyên
        self.assertIsInstance(dt_ts_def(None), int)
    
    def test_dt_floor_day(self):
        # Kiểm tra xem hàm dt_floor_day() trả về một đối tượng datetime
        self.assertIsInstance(dt_floor_day(datetime.now()), datetime)
    
    def test_dt_from_ts(self):
        # Kiểm tra xem hàm dt_from_ts() trả về một đối tượng datetime
        self.assertIsInstance(dt_from_ts(1618062087000), datetime)
    
    def test_shorten_date(self):
        # Kiểm tra xem hàm shorten_date() trả về một chuỗi
        self.assertIsInstance(shorten_date("1 day 2 hours 3 minutes 4 seconds ago"), str)
    
    def test_dt_humanize(self):
        # Kiểm tra xem hàm dt_humanize() trả về một chuỗi
        self.assertIsInstance(dt_humanize(datetime.now()), str)
    
    def test_format_date(self):
        # Kiểm tra xem hàm format_date() trả về một chuỗi
        self.assertIsInstance(format_date(datetime.now()), str)
    
    def test_format_ms_time(self):
        # Kiểm tra xem hàm format_ms_time() trả về một chuỗi
        self.assertIsInstance(format_ms_time(1618062087000), str)

if __name__ == '__main__':
    unittest.main()
