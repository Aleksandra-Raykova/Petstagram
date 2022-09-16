from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import mixins
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CustomLoginForm, \
    EditUserForm
from petstagram.accounts.models import Profile
from django.views import generic as views
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def edit_profile_view(request, slug):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user=request.user))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='home')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=Profile.objects.get(user=request.user))

    return render(request, 'accounts/profile-edit-page.html', {'user_form': user_form, 'profile_form': profile_form})


class UserRegisterView(views.CreateView):
    model = get_user_model()
    form_class = CreateProfileForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    authentication_form = CustomLoginForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    pass


class DeleteProfileView(mixins.LoginRequiredMixin, views.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def post(self, *args, slug):
        self.request.user.delete()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_profile=self.object))
        photos = list(Photo.objects.filter(created_by_user=self.object))[::-1]
        paginator = Paginator(photos, 10)
        page_number = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_number)
        photos_count = len(photos)
        total_likes_count = sum(p.like_set.count() for p in photos)

        context.update({
            'user': self.object.user,
            'profile': self.object,
            'is_owner': self.object.user.id == self.request.user.id,
            'total_likes_count': total_likes_count,
            'photos_count': photos_count,
            'pets': pets,
            'page_obj': page_obj,
        })

        return context
