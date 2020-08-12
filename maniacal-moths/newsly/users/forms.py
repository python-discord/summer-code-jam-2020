from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Choices:
    LANGUAGES = (
        ("AR", "Arabic"),
        ("BN", "Bengali"),
        ("BG", "Bulgarian"),
        ("ZH", "Chinese"),
        ("HR", "Croatian"),
        ("CS", "Czech"),
        ("DA", "Danish"),
        ("NL", "Dutch"),
        ("EN", "English"),
        ("ET", "Estonian"),
        ("FA", "Farsi"),
        ("FI", "Finnish"),
        ("FR", "French"),
        ("DE", "German"),
        ("EL", "Greek"),
        ("GU", "Gujarati"),
        ("HE", "Hebrew"),
        ("HI", "Hindi"),
        ("HU", "Hungarian"),
        ("ID", "Indonesian"),
        ("IT", "Italian"),
        ("JA", "Japanese"),
        ("KO", "Korean"),
        ("LT", "Lithuanian"),
        ("MK", "Macedonian"),
        ("MR", "Marathi"),
        ("NO", "Norwegian"),
        ("PL", "Polish"),
        ("PT", "Portugese"),
        ("PA", "Punjabi"),
        ("RO", "Romanian"),
        ("RU", "Russian"),
        ("SK", "Slovak"),
        ("SL", "Slovenian"),
        ("ES", "Spanish"),
        ("SV", "Swedish"),
        ("TH", "Thai"),
        ("TR", "Turkish"),
        ("UK", "Ukranian"),
        ("VI", "Vietnamese"),
    )
    COUNTRIES = (
        ("AR", "Argentina"),
        ("AU", "Australia"),
        ("AT", "Austria"),
        ("AZ", "Azerbaijan"),
        ("BE", "Belgium"),
        ("BM", "Bermuda"),
        ("BA", "Bosnia and Herzegovina"),
        ("BR", "Brazil"),
        ("BG", "Bulgaria"),
        ("CA", "Canada"),
        ("CL", "Chile"),
        ("ZH", "China"),
        ("CO", "Colombia"),
        ("HR", "Croatia"),
        ("CZ", "Czechia"),
        ("EG", "Egypt"),
        ("SZ", "Eswatini"),
        ("FR", "France"),
        ("DE", "Germany"),
        ("GB", "Great Britain"),
        ("GR", "Greece"),
        ("HU", "Hungary"),
        ("IS", "Iceland"),
        ("IN", "India"),
        ("IR", "Iran"),
        ("IE", "Ireland"),
        ("IL", "Israel"),
        ("IT", "Italy"),
        ("JP", "Japan"),
        ("KR", "Korea"),
        ("LT", "Lithuania"),
        ("LU", "Luxembourg"),
        ("MY", "Malaysia"),
        ("MT", "Malta"),
        ("ME", "Montenegro"),
        ("NL", "Netherlands"),
        ("NZ", "New Zealand"),
        ("NI", "Nicaragua"),
        ("NO", "Norway"),
        ("PH", "Philippines"),
        ("PL", "Poland"),
        ("PT", "Portugal"),
        ("RO", "Romania"),
        ("RU", "Russia"),
        ("SA", "Saudi Arabia"),
        ("RS", "Serbia"),
        ("ZA", "South Africa"),
        ("ES", "Spain"),
        ("SE", "Sweden"),
        ("TR", "Turkey"),
        ("UA", "Ukraine"),
        ("AE", "United Arab Emirates"),
        ("US", "United States of America"),
        ("VE", "Venezuela"),
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    language = forms.ChoiceField(choices=Choices.LANGUAGES)
    country = forms.ChoiceField(choices=Choices.COUNTRIES)

    class Meta:
        model = Profile
        fields = ["language", "country"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    language = forms.ChoiceField(choices=Choices.LANGUAGES)
    country = forms.ChoiceField(choices=Choices.COUNTRIES)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "language", "country"]
