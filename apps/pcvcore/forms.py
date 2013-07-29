from django.forms import ModelForm

from .models import PCVProfile, Teacher


class PCVForm(ModelForm):
    class Meta:
        model = PCVProfile
        fields = ["sector", "start_date", "end_date",
        "home_address", "home_state", "bio"]

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'school', 'grade', 'following', 'address', 'bio']
