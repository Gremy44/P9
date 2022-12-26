from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from . import forms, models
from itertools import chain
from django.db.models import CharField, Value


@login_required
def feed(request):
    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    reviews = []
    has_review = False

    for ticket in tickets:
        review = models.Review.objects.filter(ticket_id=ticket.id)
        review = review.annotate(content_type=Value('REVIEW', CharField()))
        if review.exists():
            review = review.annotate(has_review = Value(False))
        else: 
            review = review.annotate(has_review = Value(True))
        reviews.extend(review)

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.date_created, 
        reverse=True
    )
    
    context = {
        'posts': posts,
        'has_review': has_review
    }
    return render(request, 'feed.html', context=context)


@login_required
def post(request):
    reviews = models.Review.objects.filter(author_id = request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = models.Ticket.objects.filter(author_id = request.user) 
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.date_created, 
        reverse=True
    )

    context = {
        'posts': posts,
    }
    return render(request, 'post.html', context=context)


@login_required
def ticket_create(request):

    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    review_form = forms.ReviewForm()

    # check if user want create simple ticket or ticket with review
    review_state = False

    if request.path == '/ticket/createreview/':
        review_state = True
        
    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        ticket_form = forms.TicketForm(request.POST)
        review_form = forms.ReviewForm(request.POST)

        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()

        if review_state == True:
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.ticket = ticket
                review.save()

        return redirect('feed')

    context = {
        'ticket_form': ticket_form,
        'photo_form': photo_form,
        'review_form': review_form,
        'review_state': review_state,
    }
    return render(request, 'ticket_create.html', context=context)

@login_required
def review(request, ticket_id):
    ticket = models.Ticket.objects.get(id = ticket_id)
    review_form = forms.ReviewForm()

    if request.method == 'POST':

        review_form = forms.ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()

    context = {
        'ticket':ticket,
        'review_form': review_form,
    }
    return render(request, 'review.html', context=context)
    