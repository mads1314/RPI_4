from django.shortcuts import render

from sample_alarm_latest.components import alarm, alarm_actions


# led = LED(14)

# led.off()

def home_page_view(request):
    blocks = {'name': 'Kali :*'}

    if request.method == 'POST':

        if 'set' in request.POST:

            # Set Alarm
            timer_data = alarm_actions.set_alarm(request)

            # Call background scheduler.py
            alarm.schedule_alarm(timer_data)

            blocks = {'stop_button': 'true', 'message': 'Alarm Set', 'time': timer_data}

            return view(request, blocks)

        # Else if block will get executed when user clicks on "clear" button
        elif 'clear' in request.POST:

            # Cancel Alarm
            alarm_actions.clear_alarm()

            blocks = {'message': 'Alarm Clear'}
            return view(request, blocks)

        else:
            # Stop Alarm
            alarm_actions.stop_alarm()

            blocks = {'message': 'Alarm Stopped'}
            return view(request, blocks)

    else:
        return view(request, blocks)


def view(request, blocks):
    return render(request, 'homepage.html', blocks)
