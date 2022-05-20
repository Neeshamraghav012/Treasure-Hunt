from django.shortcuts import render
from django import forms
from .models import Team, Entries, Questions
from django.contrib import messages



class RegisterForm(forms.Form):

    tcode = forms.CharField(max_length = 255, required=False, label = "Team Code", widget = forms.TextInput(

    attrs = {

        'class':'form-control text-center',
        'placeholder':'abc@12',

    }))


# Create your views here.
def QRTokenView(request, qrtoken):

	if request.method == 'POST':

		form = RegisterForm(request.POST)

		if form.is_valid():

			flag = True

			tcode = form.cleaned_data['tcode']

			team = Team.objects.filter(tcode = tcode)

			question = Questions.objects.filter(qtoken = qrtoken)

			if team and question:

				tbno = ""
				qbno = ""
				qsno = ""
				tdone = ""

				for i in team:
					tbno = i.tbno
					tdone = i.tdone

				for i in question:
					qbno = i.qbno
					qsno = i.qsno


				if tbno == qbno:

					if qsno == (tdone + 1):

						team = Team.objects.get(tcode = tcode)
						team.tdone += 1
						team.save()

						entry = Entries(team = team, qtoken = qrtoken, isvalid = True)

						entry.save()

						messages.success(request, "Correct Answer!")
						return render(request, "game/index.html", {"qrtoken": qrtoken, "form": form})


					else:
						flag = False

				else:
					flag = False

			else:
				flag = False

			if not flag:

				team = Team.objects.filter(tcode = tcode)

				if team:
					team = Team.objects.get(tcode = tcode)
					entry = Entries(team = team, qtoken = qrtoken, isvalid = False)
					entry.save()

				messages.warning(request, "Oops, Wrong Answer try again.")
				return render(request, "game/index.html", {"qrtoken": qrtoken, "form": form})

	form = RegisterForm()
	return render(request, "game/index.html", {"qrtoken": qrtoken, "form": form})