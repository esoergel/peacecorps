from django.views.generic import UpdateView

from .models import PCVProfile, Teacher
from .forms import PCVForm

class UpdatePCVProfile(UpdateView):
    template_name = "user/pcv_update.html"
    model = PCVProfile
    form_class = PCVForm

    def get_object(self):
        return self.request.user.pcvprofile