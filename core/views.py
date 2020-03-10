from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Snippet, Tag, Library
from .forms import SnippetForm


@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippet.html', {'snippets': snippets})