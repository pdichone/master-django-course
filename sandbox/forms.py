from django import forms

choices = [("happy", "Happy"), ("neutral", "Neutral"), ("sad", "Sad")]


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField()
    satisfaction = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "@gmail.com" not in email:
            raise forms.ValidationError("Please user your gmail email")
        return email
