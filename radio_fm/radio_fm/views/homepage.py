from django.shortcuts import render

from radio_fm.views import radio


def home_page_view(request):
    blocks = {'name': 'Kali :*'}

    frequency = request.GET.get('frequency')

    if request.method == 'GET':

        if 'play' in request.GET:

            radio.play_radio_station(frequency)

            blocks = {'name': 'Kali :*', 'frequency': frequency, 'status': 'Play'}

            return view(request, blocks)

        elif 'mute' in request.GET:

            blocks = {'name': 'Kali :*', 'frequency': frequency, 'status': 'Mute'}

            radio.mute_radio_station()

            return view(request, blocks)

        elif 'unmute' in request.GET:

            blocks = {'name': 'Kali :*', 'frequency': frequency, 'status': 'Unmute'}

            radio.unmute_radio_station(frequency)

            return view(request, blocks)

        elif 'stop' in request.GET:

            blocks = {'name': 'Kali :*', 'frequency': frequency, 'status': 'Stop'}

            radio.mute_radio_station()

            return view(request, blocks)

        else:

            blocks = {'message': 'Alarm Stopped'}
            return view(request, blocks)

    else:
        return view(request, blocks)


def view(request, blocks):
    return render(request, 'homepage.html', blocks)
