from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Snippet, Tag, Library, Language
from .forms import SnippetForm
from users.models import User

@login_required(login_url='/accounts/login')
def snippets(request):
    user = User.objects.get(username=request.user.username)
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'core/snippets.html', context=context)

@login_required(login_url='/accounts/login')
def snippet_details(request, pk):
    user = User.objects.get(username=request.user.username)
    snippet = Snippet.objects.get(pk=pk)
    context = {'snippet': snippet, 'pk':pk}
    return render(request, 'core/snippet_details.html', context=context )

@login_required(login_url='/accounts/login')
def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        language = request.POST.get('language')
        form.fields['language'].choices = [(language, language)]
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.save()
        return redirect('snippets')
    else:
        form = SnippetForm()
    context = {'form': form}
    return render(request, 'core/add_snippet.html', context=context)

@login_required(login_url='/accounts/login')
def edit_snippet(request, pk):
    user = User.objects.get(username=request.user.username)
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            form.save()
        return redirect('snippet_details', pk)
    else:
        snippet = Snippet.objects.get(pk=pk)
        form = SnippetForm(instance=snippet)
    context = {'form':form, 'snippet': snippet}
    return render(request, 'core/snippet_details.html', context=context)
