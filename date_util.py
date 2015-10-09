from datetime import datetime
import numpy


def get_date_diff_hrs(from_date, to_date):
    """Returns difference of hours between two dates excluding weekends."""

    weekdays = numpy.busday_count(from_date.date(), to_date.date())
    from_date_end_time = datetime(
        year=from_date.year, month=from_date.month, day=from_date.day,
        hour=23, minute=59, second=59)
    to_date_start_time = datetime(
        year=to_date.year, month=to_date.month, day=to_date.day)

    from_day_seconds = (from_date_end_time - from_date).total_seconds() + 1
    to_day_seconds = (to_date - to_date_start_time).total_seconds()

    total_seconds = from_day_seconds + to_day_seconds

    date_diff_hrs = (weekdays - 1) * 24 + total_seconds / 3600.0

    return date_diff_hrs
