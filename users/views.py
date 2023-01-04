from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.conf import settings
from . import forms, models


def index(request):
    return render(request, 'users/index.html')


def logout_user(request):
    logout(request)
    return redirect('users/login')


class LoginPageView(View):
    template_name = 'users/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name,
                      context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('feed')
        message = 'Identifiants invalides.'
        return render(request, self.template_name,
                      context={'form': form, 'message': message})


def registration_page(request):
    form = forms.Registration()
    if request.method == 'POST':
        form = forms.Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'users/registration.html', context={'form': form})


@login_required
def subscription(request):
    abonnements = models.Subscription.objects.filter(follower=request.user)
    abonnes = models.Subscription.objects.filter(followed=request.user)

    if request.method == 'POST':
        User = get_user_model()
        username_saisie = request.POST.get('username')
        subscription = models.Subscription()
        subscription.follower = request.user
        subscription.followed = User.objects.filter(
            username=username_saisie).first()

        if models.Subscription.objects.filter(follower=request.user,
                                              followed=subscription.followed)\
                .exists():
            messages.add_message(request, messages.ERROR,
                                 "Vous suivez déjà cet utilisateur;")
        elif request.user.username == username_saisie:
            messages.add_message(request, messages.ERROR,
                                 "Vous ne pouvez pas vous suivre vous même")
        elif subscription.followed is None:
            messages.add_message(
                request, messages.ERROR,
                "Aucun utilisateur trouvé avec ce nom d'utilisateur.")
        else:
            subscription.save()

    context = {
        'follower': abonnes,
        'followed': abonnements,
    }

    return render(request, 'users/subscription.html', context=context)


@login_required
def unsubscribe(request):
    if request.method == 'POST':
        unsubscribe_id = request.POST.get('unsubscribe_id')
        unsub = models.Subscription.objects.get(id=unsubscribe_id)
        unsub.delete()
        return redirect('subscription')
