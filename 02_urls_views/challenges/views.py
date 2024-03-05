from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "30-day fitness challenge",
    "february": "Read a book every week challenge",
    "march": "Learn a new language challenge",
    "april": "Daily meditation challenge",
    "may": "Cook a new recipe every day challenge",
    "june": "30-day drawing challenge",
    "july": "No social media challenge",
    "august": "30-day gratitude challenge",
    "september": "Learn to play a musical instrument challenge",
    "october": "Write a short story every day challenge",
    "november": "30-day photography challenge",
    "december": "Random act of kindness challenge each day",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_test = monthly_challenges[month]
        response_data = f"<h1>{challenge_test}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1 style='color: red'>Page Not Found</h1>")
