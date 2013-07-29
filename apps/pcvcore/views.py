from django.views.generic import UpdateView, View
from django.http import Http404

from .models import PCVProfile, Teacher
from .forms import PCVForm, TeacherForm

class UpdatePCVProfile(UpdateView):
    template_name = "user/pcv_update.html"
    model = PCVProfile
    form_class = PCVForm

    def get_object(self):
        return self.request.user.pcvprofile

class UpdateTeacher(UpdateView):
    template_name = "user/pcv_update.html"
    model = Teacher
    form_class = TeacherForm

    def get_object(self):
        return self.request.user.teacher

class UpdateProfile(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.pcvprofile
            view = UpdatePCVProfile.as_view()
        except:
            try:
                request.user.teacher
                view = UpdateTeacher.as_view()
            except:
                raise Http404
        return view(request, *args, **kwargs)
