
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def get_ip(request):

    ip1 = request.META.get('REMOTE_ADDR', '')
    ip2 = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
    ip = ip1 or ip2 or '0.0.0.0'
    return ip


def validate(get_response):

    def middleware(request):

        current_ip = get_ip(request)

        if current_ip not in settings.ALLOWED_IPS:
            #messages.error(request, "Not allowed")
            logout(request)
            #return redirect("/")

        response = get_response(request)

        return response

    return middleware
