from django import forms
from .models import TeamMember

ROLES = (
    ("Admin", "ADMIN"),
    ("Regular", "REGULAR")
)

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.ChoiceField(widget=forms.RadioSelect, choices=ROLES)
        }

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'form-control'})