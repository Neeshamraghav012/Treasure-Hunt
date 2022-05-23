from django.shortcuts import render
from django import forms
from .models import Team, Entries, Questions
from django.contrib import messages
from captcha.fields import CaptchaField



class RegisterForm(forms.Form):

    tcode = forms.CharField(max_length = 255, required=False, label = "Team Code", widget = forms.TextInput(
    attrs = {

        'class':'form-control text-center',
        'placeholder':'abc@12',

    }))

    captcha = CaptchaField()



# Create your views here.
def QRTokenView(request, qrtoken):

	if request.method == 'POST':

		form = RegisterForm(request.POST)

		flag = True


		if form.is_valid():


			tcode = form.cleaned_data['tcode']

			team = Team.objects.filter(tcode = tcode)

			question = Questions.objects.filter(qtoken = qrtoken)

			if team and question:


				get_team = Team.objects.get(tcode = tcode)
				get_question = Questions.objects.get(qtoken = qrtoken)

				tbno = get_team.tbno
				qbno = get_question.qbno
				qsno = get_question.qsno
				tdone = get_team.tdone


				if tbno == qbno:

					if qsno == (tdone + 1):

						team = Team.objects.get(tcode = tcode)
						team.tdone += 1
						team.save()

						entry = Entries(team = team, qtoken = qrtoken, isvalid = True)

						entry.save()

						messages.success(request, "Correct Answer!")
						return render(request, "game/index.html", {"qrtoken": qrtoken, "form": form, "link": get_question.nextlink})


					elif qsno <= (tdone):

						messages.success(request, "Already Solved!")
						return render(request, "game/index.html", {"qrtoken": qrtoken, "form": form, "link": get_question.nextlink})


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



