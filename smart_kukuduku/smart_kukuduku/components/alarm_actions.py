from smart_kukuduku.components.models import Timer
from smart_kukuduku.components import switch
import logging
from datetime import datetime


def set_alarm(request):

    date_data = request.POST.get('date')
    time_data = request.POST.get('time')

    alarm_data = datetime.strptime(date_data + ' ' + time_data, '%Y-%m-%d %H:%M')

    Timer.objects.update_or_create(id=1, defaults={'timer': alarm_data})

    timer_data = Timer.objects.get(id=1)

    return timer_data.timer


def clear_alarm():
    logging.warning("clear_alarm")

    # Clear record
    Timer.objects.all().delete()


def stop_alarm():
    logging.warning("stop_alarm")

    switch.turn_off_alarm()
