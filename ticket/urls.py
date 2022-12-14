from django.urls import path

from ticket import views

urlpatterns = [
    path('create/ticket', views.critique_upload, name='ticket_create'),
    path('create/critique', views.critique_upload, name='critique_create'),
    path('ticket/<int:ticket_id>', views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/edit', views.ticket_edit, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete', views.ticket_delete, name='delete_ticket'),
    path('home/', views.home, name='home'),
]

'''path('upload/', views.photo_upload, name='ticket_upload'),'''