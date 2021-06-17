from django.http import response
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls.base import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no cheese for the enture month",
    "february": "Walk for at least 20 minuites every day!",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no cheese for the enture month",
    "may": "Walk for at least 20 minuites every day!",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no cheese for the enture month",
    "august": "Walk for at least 20 minuites every day!",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no cheese for the enture month",
    "november": "Walk for at least 20 minuites every day!",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html", {
        "months": months,
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text ,
            "month_name": month
        })
    except:
        raise Http404()
