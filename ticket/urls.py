from django.urls import path

from ticket import views

urlpatterns = [
    path('createticket/', views.ticket_create, name='ticket_create'),
    path('createreview/', views.ticket_create, name='review_create'),
    path('review/<int:ticket_id>', views.review, name='review'),
    # path('ticket/edit_review', views.edit_review, name='edit_review'),
    # path('critique/<int:review_id>/delete', views.delete_review, name='delete_review'),
    # path('ticket/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    # path('ticket/<int:ticket_id>/edit', views.ticket_edit, name='edit_ticket'),
    # path('ticket/<int:ticket_id>/delete', views.ticket_delete, name='delete_ticket'),
    path('feed/', views.feed, name='feed'),
    path('post/', views.post, name= 'post'),
]

'''path('upload/', views.photo_upload, name='ticket_upload'),'''