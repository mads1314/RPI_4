from sample_alarm_latest.components.models import Timer
from sample_alarm_latest.components import switch
import logging


def set_alarm(request):

    alarm_data = request.POST.get('alarm_data')

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
