from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Snippet, Tag, Library, Language
from .forms import SnippetForm
from users.models import User

@login_required
def snippets(request):
    user = User.objects.get(username=request.user.username)
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'core/snippets.html', context=context)

def snippet_details(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    context = {'snippet': snippet, 'pk':pk}
    return render(request, 'core/snippet_details.html', context=context )

@login_required
def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        language = request.POST.get('language') 
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
        return redirect('snippets')
    else:
        form = SnippetForm()
    context = {'form': form}
    return render(request, 'core/add_snippet.html', context=context)

@login_required
def edit_snippet(request):
    user = User.object.get(username=request.user.username)
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
        return redirect('snippets')
    else:
        snippet = Snippet.objects.get(pk=pk)
        form = SnippetForm(instance=snippet)
    context = {'form':form}
    return render(request, 'core/edit_snippet.html', context=context)
