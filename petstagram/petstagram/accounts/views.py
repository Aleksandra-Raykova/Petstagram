from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.accounts.models import Profile, PetstagramUser
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from petstagram.pets.models import Pet


class UserRegisterView(views.CreateView):
    model = get_user_model()
    form_class = CreateProfileForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile-edit-page.html'
    success_url = reverse_lazy('profile-details')


class DeleteProfileView(views.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_profile=self.object.user))
        total_likes_count = sum(p.like_set.count() for p in pets)
        total_pets = len(pets)

        context.update({
            'profile': self.object,
            'is_owner': self.object.user.id == self.request.user.id,
            'total_likes_count': total_likes_count,
            'total_pets': total_pets,
            'pets': pets,
        })

        return context
