from django.http import HttpRequest
from django.shortcuts import render

from document_tester.tester import test_document
from tester.forms import SettingsForm, DocumentForm


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
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = request.FILES['document']
            test_document(document)
    else:
        form = DocumentForm()
    return render(request, 'doctest.html', {'form': form})
