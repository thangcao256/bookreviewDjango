from django import forms


SEARCH_CHOICE = (
    ("title", "Title"),
    ("contributor", "Contributor")
)

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=SEARCH_CHOICE)
