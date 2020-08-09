from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = [
            'email',
            'first_name',
            'last_name',
            'earldom',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = [
        '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929',
        '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939',
        '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949',
        '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959',
        '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
        '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
        '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
        '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
        '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
        '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029',
    ]

    birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'earldom',
            'birthday',
            'email',
            'image',
        ]

