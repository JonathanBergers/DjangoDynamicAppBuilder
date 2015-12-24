from django.db import connection
from django.views.generic import View, FormView
from djangotest.utils import modelcreator


class FormCreateView(FormView):
    form_class = modelcreator.create_form('main')
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(self.get_form_kwargs()
        form.send_email()
        return super(ContactView, self).form_valid(form)