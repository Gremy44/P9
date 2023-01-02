from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from .forms import TicketForm, PhotoForm, ReviewForm
from users.models import Subscription
from itertools import chain
from django.db.models import CharField, Value, Q


def get_users_viewable_reviews(user):
    # recuperation des reviews sur les tickets que j'ai créé
    # import Q pour unir deux requetes
    reviews = Review.objects.filter(Q(ticket__author=user) | Q(author=user))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # recuperer les review des gens auquelles on est abonné
    abonnements = Subscription.objects.filter(follower=user)
    print('abonnements : ', abonnements)

    for abonnement in abonnements:
        review_abonnes = Review.objects.filter(
            author=abonnement.followed).exclude(ticket__author=user)
        review_abonnes = review_abonnes.annotate(
            content_type=Value('REVIEW', CharField()))
        print('review_abonnes : ', review_abonnes)
        reviews = chain(reviews, review_abonnes)

    return reviews


def get_users_viewable_tickets(user):
    # recuperation de mes tickets
    tickets = Ticket.objects.filter(author=user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # recuperation des tickets des abonnements
    abonnements = Subscription.objects.filter(follower=user)

    for abonnement in abonnements:
        ticket_abonnes = Ticket.objects.filter(author=abonnement.followed)
        ticket_abonnes = ticket_abonnes.annotate(
            content_type=Value('TICKET', CharField()))
        tickets = chain(tickets, ticket_abonnes)

    return tickets


@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request.user)
    tickets = get_users_viewable_tickets(request.user)

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )

    context = {
        'posts': posts,
    }
    return render(request, 'feed.html', context=context)


@login_required
def post(request):
    reviews = Review.objects.filter(author_id=request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(author_id=request.user)
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

    ticket_form = TicketForm()
    photo_form = PhotoForm()
    review_form = ReviewForm()

    # check if user want create simple ticket or ticket with review
    review_state = False

    if request.path == '/ticket/createreview/':
        review_state = True

    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        ticket_form = TicketForm(request.POST)
        review_form = ReviewForm(request.POST)

        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()

            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()

        if review_state is True:
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
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = ReviewForm()

    if request.method == 'POST':

        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
        return redirect('feed')

    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'review.html', context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('feed')
    context = {'edit_form': edit_form,
               'ticket_id': ticket.id,
               }
    return render(request, 'ticket_edit.html', context=context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    ticket = review.ticket

    edit_form = ReviewForm(instance=review)
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('feed')
    context = {'edit_form': edit_form,
               'review_id': review.id,
               'ticket': ticket,
               }
    return render(request, 'review_edit.html', context=context)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')

    return HttpResponse(status=403)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')

    return HttpResponse(status=403)
