from django import forms


class Zapis(forms.Form):
    Imię = forms.CharField(max_length=15)
    Nazwisko = forms.CharField(max_length=15)
    hasło = forms.CharField(max_length=8,widget=forms.PasswordInput)

class Lan(forms.Form):
    LANGUAGES = [
        ("angielski", "angielski"),
        ("niemiecki", "niemiecki"),
        ("francuski", "francuski"),
        ("hiszpański", "hiszpański")
    ]
    język = forms.ChoiceField(choices=LANGUAGES)
    

