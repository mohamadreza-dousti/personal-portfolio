from django.shortcuts import render
from .models import Skill, Project, Language, Education, Experience


def portfolio_view(request):
    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "languages": Language.objects.all(),
        "educations": Education.objects.all(),
        "experiences": Experience.objects.all(),
    }

    return render(request, 'portfolio.html', context)
