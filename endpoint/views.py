from django.http import JsonResponse
from django.views.decorators.http import require_GET
import datetime
import pytz

@require_GET
def endpoint_view(request):
    '''values for slack_name and track'''
    slack_name = "HGNx"
    track = "Backend"

    '''current day of the week'''
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    '''current UTC time with validation (+/- 2 minutes)'''
    current_utc_time = datetime.datetime.now(pytz.utc)

    '''Calculate the time window to return current UTC time'''
    time_window = datetime.timedelta(minutes=2)
    utc_time_within_window = current_utc_time - time_window <= current_utc_time <= current_utc_time + time_window

    if not utc_time_within_window:
        return JsonResponse({
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "",
            "github_repo_url": "",
            "status_code": 400
        })

    '''GitHub URLs'''
    github_file_url = "https://github.com/Mathewkoech/Stageoo1_endpoint/blob/master/endpoint/views.py"
    github_repo_url = "https://github.com/Mathewkoech/Stageoo1_endpoint"

    return JsonResponse({
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    })
