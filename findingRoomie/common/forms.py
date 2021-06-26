from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
# from .models import Userinfo 

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ['username','password1','password2','name','nickname','profile_img','gender','age','school','major',
        'studentID','sleep_habit','sleep_time','cleanliness',
        'cook','smoke','budget','hope_area','introduction',
        'profile_active']
        widgets = {
            'gender':
        }