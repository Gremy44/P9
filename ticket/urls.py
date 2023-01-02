from django.urls import path

from ticket.views import ticket_create, review, edit_review, \
    edit_ticket, delete_ticket, delete_review, feed, post

urlpatterns = [
    path('createticket/', ticket_create, name='ticket_create'),
    path('createreview/', ticket_create, name='review_create'),
    path('review/<int:ticket_id>', review, name='review'),
    path('reviewedit/<int:review_id>', edit_review, name='edit_review'),
    path('ticketedit/<int:ticket_id>', edit_ticket, name='edit_ticket'),
    path('ticketdelete/<int:ticket_id>', delete_ticket, name='delete_ticket'),
    path('reviewdelete/<int:review_id>', delete_review, name='delete_review'),
    path('feed/', feed, name='feed'),
    path('post/', post, name='post'),
]
