from django import forms

# define radio choice
# TODO: Best practice will be to generate these from the database
CATEGORY_RADIO_CHIOCES = (
    ("programming language", "Programming Language"),
    ("databases", "Databases"),
)
TAGS_RADIO_CHOICES = (
    ("python", "Python"),
    ("django", "Django"),
    ("sql", "SQL"),
    ("postgresql", "Postgresql"),
    ("beginner", "Beginner"),
    ("mid_level", "Mid-level"),
    ("advanced", "Advanced"),
    ("paid", "Paid"),
    ("free", "Free"),
)


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Title", "class": "title"})
    )
    link = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Enter URL"}))
    # default to input of type text, but can change with widget.
    description = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter Description"})
    )
    categories = forms.ChoiceField(
        choices=CATEGORY_RADIO_CHIOCES, widget=forms.RadioSelect
    )
    tags = forms.ChoiceField(choices=TAGS_RADIO_CHOICES, widget=forms.RadioSelect)
