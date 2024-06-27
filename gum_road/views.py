from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
class Homepage(generic.TemplateView):
    template_name = 'home_page.html'


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self.send_verification_email(user)
        messages.success(self.request, 'Signup successful! Please check your email for a verification link.')
        return super().form_valid(form)
    
    def send_verification_email(self, user):
        verification_link = self.request.build_absolute_uri(reverse('verify_email', args=[user.id]))
        send_mail(
            'Verify your email',
            f'Click on the following link to verify your email: {verification_link}',
            from_email= "nwokoronkem@gmail.com",
            recipient_list= [user.email],
            fail_silently=False,
        )
        
        
        
def verify_email(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "Your email has been verified. You can now log in.")
    return redirect('login')
    
