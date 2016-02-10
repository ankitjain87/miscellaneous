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


def get_date_diff_count(from_date, to_date):
    """Returns difference count between two dates excluding weekends."""
    if from_date and to_date:
        return numpy.busday_count(from_date.date(), to_date.date())

    return None


def format_hrs_in_days(hours):
    if hours < 1:
        return "{:.2f}".format(hours * 60) + 'min(s)' if hours > 0 else 0
    if hours < 24:
        return str(int(hours)) + 'hr(s)'

    d = hours/24
    h = hours % 24
    d = str(int(d)) + ' day(s)'
    if h > 0:
        d += ', ' + str(int(h)) + 'hr(s)'
    return d


def change_date_format(date):
    date = datetime.strptime(date, '%m/%d/%Y')
    return date.strftime('%Y-%m-%d %H:%M:%S')


def date_to_string(date):
    if date:
        return datetime.strftime(date, '%m/%d/%Y')

    return None
