from django.urls import path
from .views import home_page_view, add_note_view, create_new_user_view, delete_note_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('add/', add_note_view, name='add'),
    path('createNewUser/', create_new_user_view, name='newuser'),
    path('deleteNote/<int:noteid>', delete_note_view, name='delete')
]
