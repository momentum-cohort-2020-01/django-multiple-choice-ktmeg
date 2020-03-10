from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Snippet, Tag, Library, Language
from .forms import SnippetForm


@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippets.html', {'snippets': snippets})