from django.shortcuts import render
from . import models
from . import forms

# Create your views here.


def login(response,information=""):
    if response.method == "POST":
        form = forms.Zapis(response.POST)
        if form.is_valid():
            fname = form.cleaned_data["Imię"]
            fsurename = form.cleaned_data["Nazwisko"]
            fpasscode = form.cleaned_data["hasło"]
            x = models.Uczen.objects.filter(name=fname).filter(surename=fsurename)
            if x.exists():
                if x.first().passcode == fpasscode:
                    response.session["uczen_id"] = x.first().id
                    if "uczen_id" in response.session:
                        user = str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().name) + " " + str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().surename)
                    else:
                        user = "Zaloguj się"
                    return render(response, "zapisy/thanks.html",{ "user": user, "info": "Dziękujemy" })
                else:
                    information = "Hasło jest niewłaściwe!"
            else:
                information = "Imię lub nazwisko jest niewłaściwe!"
    form = forms.Zapis()

    if "uczen_id" in response.session:
        user = str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().name) + " " + str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().surename)
    else:
        user = "Zaloguj się"
    context = {
        'form': form,
        'info': information,
        'user': user
    }
    return render(response, 'zapisy/login.html', context)

def thanks(response):
    if "uczen_id" in response.session:
        if response.method == "POST":
            index = response.POST.get("id")
            egzamin = models.Termin.objects.filter(id=index).first()
            uczen = models.Uczen.objects.filter(id=response.session["uczen_id"]).first()
            if egzamin.language == "polski":
                uczen.polski = egzamin
            else:
                uczen.obcy = egzamin
            egzamin.available = False
            uczen.save()
            egzamin.save()

        user = str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().name) + " " + str(models.Uczen.objects.filter(id=response.session["uczen_id"]).first().surename)
    else:
        user = "Zaloguj się"
    context = {
        'user': user,
    }
    return render(response, "zapisy/thanks.html",context)

def logout(response):
    if "uczen_id" in response.session:
        response.session.pop("uczen_id")
    context = {
        'user': "Zaloguj się",
    }
    return render(response, "zapisy/log_out.html", context)


def user_panel(response):
    if "uczen_id" in response.session:
        uczen = models.Uczen.objects.filter(id=response.session["uczen_id"]).first()
        user = str(uczen.name) + " " + str(uczen.surename)
        
        if uczen.polski is not None:
            polski_zapis = False
        else:
            polski_zapis = True   
        if uczen.obcy is not None:
            obcy_zapis = False
        else:
            obcy_zapis = True

        context = {
            'user': user,
            'polski_zapis': polski_zapis,
            'obcy_zapis': obcy_zapis,
        }
        if not polski_zapis:
            context["polski"] = uczen.polski
        if not obcy_zapis:
            context["obcy"] = uczen.obcy
        
        
        return render(response, "zapisy/user_panel.html",context)
    else:
        return login(response,"Zaloguj się, aby dostać się do panelu użytkownika")

def zapisy(response, lan):
    if "uczen_id" in response.session:
        uczen = models.Uczen.objects.filter(id=response.session["uczen_id"]).first()
        user = str(uczen.name) + " " + str(uczen.surename)
        if lan == "obcy":
            if response.method == "POST":
                form = forms.Lan(response.POST)
                if form.is_valid():
                    language = form.cleaned_data["język"]
                    terminy = models.Termin.objects.filter(language=language).filter(available=True).exclude(teacher_surename=uczen.english_teacher).exclude(teacher_surename=uczen.foreign_teacher).all()
                    form2 = forms.Lan()
            
                    context = {
                        "form": form2,
                        "user": user,
                        "terminy": terminy,
                        "message": "Właśnie wyszukujesz dostępne egzaminy ustne w języku " + language + "m",
                        "obcy": True,
                        "exists": not terminy.exists()
                    }
                     
            else:
                terminy = models.Termin.objects.filter(available=True).exclude(teacher_surename= uczen.english_teacher).exclude(teacher_surename= uczen.foreign_teacher).all()
                form = forms.Lan()
                context = {
                    'form': form,
                    'user': user,
                    'terminy': terminy,
                    'message': "Wyszukujesz właśnie dostępne egzaminy ustne w języku obcym",
                    "obcy": True,
                    "exists": not terminy.exists()
                }
                
        else:
            terminy = models.Termin.objects.filter(language="polski").filter(available=True).exclude(teacher_surename=uczen.polish_teacher).all()
            context = {
                "user": user,
                "terminy": terminy,
                "message": "Właśnie wyszukujesz dostępne egzaminy ustne języka polskiego",
                "obcy": False,
                "exists": not terminy.exists()
            }
        return render(response, "zapisy/zapisy.html",context)             
    else:
        return login(response,"Zaloguj się, aby zapisać się na egzamin")


def wypis(response):
    if "uczen_id" in response.session:
        uczen = models.Uczen.objects.filter(id=response.session["uczen_id"]).first()
        if response.method == "POST":
            index = response.POST.get("id")
            egzamin = models.Termin.objects.filter(id=index).first()
            if egzamin.language == "polski":
                uczen.polski = None
            else:
                uczen.obcy = None
            egzamin.available = True
            uczen.save()
            egzamin.save()
        user = str(uczen.name) + " " + str(uczen.surename)
        context = {
            "user": user
        }
        return render(response, "zapisy/wypis.html", context)
    else:
        return login(response,"Zaloguj się, aby wypisać się z egzaminu")

def not_found(response,exception):
    if "uczen_id" in response.session:
        uczen = models.Uczen.objects.filter(id=response.session["uczen_id"]).first()
        user = str(uczen.name) + " " + str(uczen.surename)
    else:
        user = "Zaloguj się"   
    context = {
        "user": user
    } 
    return render(response, "zapisy/page_not_found.html", context)












