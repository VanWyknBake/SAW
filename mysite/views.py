from django.shortcuts import render
from .models import Home, About, News, Profile, Category, Skills, Portfolio, Category2


def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #NEWS
    news = News.objects.order_by('-updated')
    

    # Skills
    categories = Category.objects.all()
    #SQUADS
    categories2 = Category2.objects.order_by('-name')

    # Portfolio
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'news': news,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'categories2': categories2,
    }

    return render(request, 'index.html', context)
