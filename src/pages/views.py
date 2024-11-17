from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import RegisterForm

@login_required
def home_page_view(request):
    user = request.user
    user_notes = Note.objects.filter(creator=user)
    return render(request, 'index.html', {"notes": user_notes})

def create_new_user_view(request):
    method = request.method
    if method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login(request, authenticate(username=username, password=password))
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'newuser.html', {'form': form})

@login_required
def add_note_view(request):
    user = request.user
    note = request.POST.get('content', '').strip()
    Note.objects.create(creator=user, content=note)
    return redirect('/')

@login_required
def delete_note_view(request, noteid):
    user = request.user
    note = Note.objects.get(pk=noteid)
    if user == note.creator:
        note.delete()
    return redirect('/')
