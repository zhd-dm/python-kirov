import datetime as DT
from datetime import timedelta, datetime
from typing import List

from features.print.print import Print
from features.date_transformer.config.constants import FORMAT_DD_MM_YYYY, FORMAT_YYYY_MM_DD_HH_MM_SS


class DateTransformer:

    def _print_now_date(message: str, format = FORMAT_YYYY_MM_DD_HH_MM_SS):
        now = DT.datetime.now()
        current_time = now.strftime(format)
        Print().print_info(f'{message} -> {current_time}')

    def _get_list_of_dates(self, days: int, format = FORMAT_DD_MM_YYYY):
        today = datetime.today()
        half_year_ago = today - timedelta(days = days)

        date_list: List[datetime] = []

        while today > half_year_ago:
            date_list.insert(0, today.strftime(format))
            today -= timedelta(days = 1)

        return date_list

    def _get_count_difference_days(self,
        now: datetime,
        max_date: datetime
    ) -> int:
        last_date = datetime.combine(max_date, datetime.min.time())
        difference_days = (now.date() - last_date.date()).days
        return difference_days
