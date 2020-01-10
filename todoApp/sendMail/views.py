from django.shortcuts import render,redirect

def homepage(request):
    return render(
        request = request,
        template_name = 'sendMail/home_page.html',
        context = {}
    )