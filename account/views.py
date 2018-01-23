from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import SignUpForm, UserInformationUpdateForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'account/user_profile.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user
