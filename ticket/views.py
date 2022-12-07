from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from . import forms, models

'''@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo.uploader = request.user
        photo.save()
        return redirect('home')
    return render(request, 'ticket/ticket.html', context={'form': form})'''


@login_required
#@permission_required('ticket.ticket_upload', raise_exception=True)
def ticket_upload(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    critique_form = forms.CritiqueForm()
    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        ticket_form = forms.TicketForm(request.POST)
        critique_form = forms.CritiqueForm(request.POST)
        if all([ticket_form.is_valid(), photo_form.is_valid(), critique_form.is_valid()]):

            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()

            critique = critique_form.save(commit=False)
            critique.uploader = request.user
            critique.save()

            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.critique = critique
            ticket.save()

            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'photo_form': photo_form,
        'critique_form': critique_form,
    }
    return render(request, 'ticket/ticket.html', context=context)

@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
            if 'delete_ticket' in request.POST:
                delete_form = forms.DeleteTicketForm(request.POST)
                if delete_form.is_valid():
                    ticket.delete()
                    return redirect('home')
    context = {'edit_form': edit_form,
               'delete_form': delete_form,
    }
    return render(request, 'ticket/edit_ticket.html', context=context)

@login_required
def home(request):
    photos = models.Photo.objects.all()
    ticket = models.Ticket.objects.all()
    return render(request, 'ticket/home.html', context={'photos': photos, 'tickets':ticket})

@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'ticket/view_ticket.html', {'ticket':ticket})