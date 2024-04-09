from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search recipes...", "class": "form-control mr-sm-2"}
        ),
    )
