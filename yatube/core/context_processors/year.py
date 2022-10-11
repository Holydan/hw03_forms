import datetime


def year(request):
    year_today = datetime.date.today()
    now = int(year_today.year)
    return {'year': now}
