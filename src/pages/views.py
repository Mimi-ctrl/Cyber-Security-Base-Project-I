from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Note
from .forms import RegisterForm
import traceback
import logging

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

def empty_page_view(request):
    #Replacing the following with the commented code will not reveal any details about the error to the user:    
    try:
        # Intentional error: division by zero causes an error
        result = 1 / 0
    except Exception as e:
        # Return an error message that includes a stack trace and detailed errors        
        error_message = f"Error: {str(e)}<br>Stack trace: <pre>{traceback.format_exc()}</pre>"
        return(HttpResponse(error_message))

    #The correct way to handle the error: 
    # logger = logging.getLogger(__name__)   
    # try:
    #     result = 1 / 0
    # except Exception as e:
    #     logger.error("An error occurred in view_with_error_handling", exc_info=True)
    #     return HttpResponse("Something went wrong. Please try again later.", status=500)
    # return HttpResponse(f"Result: {result}")
