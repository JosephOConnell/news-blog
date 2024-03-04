from django.shortcuts import render
from .models import News


def news(request):
    """
    Renders the NEWS page
    """
    news = News.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "news/news.html",
        {"news": news},
    )