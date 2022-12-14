from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
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


'''@login_required
# @permission_required('ticket.ticket_upload', raise_exception=True)
def ticket_upload(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        ticket_form = forms.TicketForm(request.POST)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):

            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()

            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()

            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'photo_form': photo_form,
    }
    
    return render(request, 'ticket/ticket.html', context=context)
'''
@login_required
# @permission_required('ticket.ticket_upload', raise_exception=True)
def critique_upload(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    critique_form = forms.CritiqueForm()

    critique_state = False

    if request.path == '/ticket/create/critique':
        critique_state = True

    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        ticket_form = forms.TicketForm(request.POST)
        critique_form = forms.CritiqueForm(request.POST)

        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()

        if critique_state == True:
            if critique_form.is_valid():
                critique = critique_form.save(commit=False)
                critique.author = request.user
                critique.ticket = ticket
                critique.save()
                critique_state = True

        return redirect('home')

    context = {
        'ticket_form': ticket_form,
        'photo_form': photo_form,
        'critique_form': critique_form,
        'critique_state': critique_state,
    }
    
    return render(request, 'ticket/critique.html', context=context)

'''@login_required
# @permission_required('ticket.ticket_upload', raise_exception=True)
def critique_upload(request):
    critique_form = forms.CritiqueForm()
    if request.method == 'POST':
        critique_form = forms.CritiqueForm(request.POST)
        if critique_form.is_valid:

            critique = critique_form.save(commit=False)
            critique.uploader = request.user
            critique.save()

    context = {
        'critique_form': critique_form,
    }
    
    return render(request, 'ticket/critique.html', context=context)'''

@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
    context = {'edit_form': edit_form,
               'ticket_id': ticket.id,
    }
    return render(request, 'ticket/edit_ticket.html', context=context)

def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    context = {'edit_form': edit_form,
               'delete_form': delete_form,
               'ticket_id': ticket.id,
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
    critique = models.Critique.objects.all()
    print(ticket_id)
    # print(critique[0].comment)
    
    cricri = [critiques for critiques in critique if critiques.ticket_id == ticket_id ]
    print(cricri)



    context = {
        'ticket':ticket,
        'critique':cricri,
    }
    return render(request, 'ticket/view_ticket.html', context=context)
