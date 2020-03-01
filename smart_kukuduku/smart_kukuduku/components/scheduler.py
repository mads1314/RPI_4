from apscheduler.schedulers.background import BackgroundScheduler
from smart_kukuduku.components import switch


def schedule_alarm(timer_data):
    scheduler = BackgroundScheduler(timezone='Asia/Kolkata')

    # scheduler.add_job(execute_taks.turn_on_alarm, next_run_time=timer_data, args=[device, pygame])

    scheduler.add_job(switch.turn_on_alarm, next_run_time=timer_data)

    scheduler.start()
