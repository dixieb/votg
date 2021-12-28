from .models import Report
from bootstrap_modal_forms.forms import BSModalForm

class NoteForm(BSModalForm):
    class Meta:
        model = Report
        fields = ['person', 'notes']


# class PersonForm(forms.Form):
#     firstName = forms.CharField(label='First Name', max_length=50)
#     lastName = forms.CharField(label='Last Name', max_length=50)
#     alias = forms.CharField(label='Alias', max_length=50, required=False)
#     gender = forms.CharField(label='Gender', max_length=1)
#     dob = forms.CharField(label='Date of Birth (dd/mm/yyyy)', max_length=10)
#     address = forms.CharField(label='Street Address', max_length=255)
#     city = forms.CharField(label='City', max_length=100)
#     permit = forms.CharField(label='Permit # ', max_length=10)
#
# class TicketForm(forms.Form):
#     firstName = forms.CharField(label='First Name', max_length=100)
#     lastName = forms.CharField(label='Last Name', max_length=100)
#     permit = forms.CharField(label="Driver's Permit", max_length=10)
#     vehicle = forms.CharField(label='Vehicle Registration', max_length=7)
#     offence = forms.CharField(label='Offence', max_length=255)
#     date_of_offence = forms.CharField(label='Date of Offence', max_length=10)
#     time_of_offence = forms.CharField(label='Time of Offence', max_length=6)
#     location = forms.CharField(label='Location of Offence', max_length=100)
#

