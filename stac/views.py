from django.http import HttpResponse
from django.shortcuts import render

def yoon(request):
    context2 = {
        'name': '심자윤',
        'img_src': 'https://w.namu.la/s/8bcf8f51cac9ed16e0843b4e9978122beeeaea027acc622b202adb2e3014aa742eb2297708975c6b74eeff3c2eec0a0931c31fce19237eda7495271519433b6aebbbf77d0ab8579ddb3ca4e35cf8dcec254a4c6008902e41e80a6226e1a4b4ee',
    }
    return render(request, 'stac/멤버.html', context=context2)

def sieun(request):
    context = {
        'name': '박시은',
        'img_src': 'https://w.namu.la/s/fe423b31f808026f359b0eb983a8350b60c82184394660cb9990e95b40c4adddf0fc09cb1562a3c1f867ad8d5c3acb48d4874a3586c3c72048a2e2bc67468f844887cafe66fb05407074ca83f07ac2beb79f5c00a36e336569475a180190306f',
    }
    return render(request, 'stac/멤버.html', context=context)

