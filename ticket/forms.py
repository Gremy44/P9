from django import forms

from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image']

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # critique_form = forms.BooleanField(widget=forms.HiddenInput, initial=False)
    class Meta:
        model = models.Ticket
        fields = ['title', 'content']

class CritiqueForm(forms.ModelForm):
    class Meta:
        model = models.Critique
        fields = ['title', 'rate', 'comment']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)