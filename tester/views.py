from django.http import HttpRequest
from django.shortcuts import render

from tester.forms import SettingsForm


def index(request: HttpRequest):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            link = request.build_absolute_uri(
                f'/doctest?t={data["margin_top"]}&r={data["margin_right"]}' +
                f'&b={data["margin_bottom"]}&l={data["margin_left"]}&font={data["font_name"]}'
            )
            return render(request, 'index.html', {'form': form, 'link': link})
    else:
        form = SettingsForm()
        return render(request, 'index.html', {'form': form})


def doctest(request: HttpRequest):
    return render(request, 'doctest.html')
