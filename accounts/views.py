import random
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import UserRegisterForm
from .models import MyUser, OtpCode
from utils import send_otp_code

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form= self.form_class
        return render(request, 'registration/user_register.html', {'form':form})
    
    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.filter(phone_number = form.cleaned_data['phone'])
            if otp.exists():
                messages.error(request, 'we send your code alreedy')
                return redirect('accounts:verify_code')
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info']={
                'phone_number':form.cleaned_data['phone'],
                'username':form.cleaned_data['username'],
                'password':form.cleaned_data['password'],
            }
            messages.success(request, _('we sent you a code'))
            return redirect('accounts:verify_code')
        return render(request, 'registration/user_register.html', {'form':form})
