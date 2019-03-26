import time

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json

# Create your views here.
from .forms import DocumentForm,SignUpForm
# from scan_score.models import UploadImage


def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('select')
  else:
    form = SignUpForm()
  return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("Email: ", email, "Password: ", password)
        return redirect('select')
        # user = authenticate(email=email, password='password')
        # print(user)
        # if user:
        #     login(request, user)
        #     print("Email: ", email, "Password: ", password)
        #     return redirect('fileupload')
    return render(request, 'registration/login.html')

# @login_required
def home(requests):
    return render(requests, 'welcome.html')

@login_required
def thanks(requests):
    return render(requests, 'thank-you.html')

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            time.sleep(7)
            return redirect('thanks')
    else:
        form = DocumentForm()
    return render(request, 'fileupload.html', {'form': form})

@login_required
def select_test_type(request):

 return render(request, 'select-score.html')

@login_required
def index(request):
    # with open('/home/junaid/PycharmProjects/scan_score/media/document.json', 'r') as f:
    #     json_object = f.read()
    json_object = {
    "student_name": "Talha Mobin",
    "test_date": "2018-11-03",
    "test_form_no": "0001",
    "english": {
      "score": 32,
      "correct": 70,
      "incorrect": 5,
      "omitted": 0,
      "answers": {
        "q1": "B",
        "q2": "F",
        "q3": "C",
        "q4": "H",
        "q5": "A",
        "q6": "G",
        "q7": "D",
        "q8": "J",
        "q9": "B",
        "q10": "J",
        "q11": "C",
        "q12": "H",
        "q13": "D",
        "q14": "F",
        "q15": "A",
        "q16": "F",
        "q17": "D",
        "q18": "J",
        "q19": "B",
        "q20": "G",
        "q21": "A",
        "q22": "F",
        "q23": "D",
        "q24": "H",
        "q25": "B",
        "q26": "J",
        "q27": "D",
        "q28": "F",
        "q29": "C",
        "q30": "G",
        "q31": "B",
        "q32": "J",
        "q33": "A",
        "q34": "F",
        "q35": "A",
        "q36": "F",
        "q37": "C",
        "q38": "H",
        "q39": "D",
        "q40": "H",
        "q41": "C",
        "q42": "G",
        "q43": "B",
        "q44": "G",
        "q45": "A",
        "q46": "F",
        "q47": "D",
        "q48": "J",
        "q49": "B",
        "q50": "H",
        "q51": "D",
        "q52": "F",
        "q53": "C",
        "q54": "J",
        "q55": "A",
        "q56": "J",
        "q57": "B",
        "q58": "H",
        "q59": "D",
        "q60": "G",
        "q61": "A",
        "q62": "F",
        "q63": "B",
        "q64": "J",
        "q65": "A",
        "q66": "F",
        "q67": "C",
        "q68": "G",
        "q69": "C",
        "q70": "H",
        "q71": "A",
        "q72": "G",
        "q73": "D",
        "q74": "F",
        "q75": "C"
      }
    },
    "math": {
      "score": "32",
      "correct": "55",
      "incorrect": "5",
      "omitted": "0",
      "answers": {
        "q1": "E",
        "q2": "F",
        "q3": "C",
        "q4": "H",
        "q5": "B",
        "q6": "K",
        "q7": "D",
        "q8": "J",
        "q9": "B",
        "q10": "G",
        "q11": "E",
        "q12": "H",
        "q13": "E",
        "q14": "K",
        "q15": "A",
        "q16": "F",
        "q17": "D",
        "q18": "J",
        "q19": "E",
        "q20": "K",
        "q21": "C",
        "q22": "F",
        "q23": "D",
        "q24": "J",
        "q25": "E",
        "q26": "H",
        "q27": "A",
        "q28": "K",
        "q29": "C",
        "q30": "G",
        "q31": "B",
        "q32": "J",
        "q33": "A",
        "q34": "F",
        "q35": "E",
        "q36": "G",
        "q37": "C",
        "q38": "H",
        "q39": "D",
        "q40": "H",
        "q41": "C",
        "q42": "G",
        "q43": "E",
        "q44": "G",
        "q45": "D",
        "q46": "K",
        "q47": "B",
        "q48": "K",
        "q49": "B",
        "q50": "J",
        "q51": "D",
        "q52": "F",
        "q53": "C",
        "q54": "H",
        "q55": "A",
        "q56": "J",
        "q57": "C",
        "q58": "K",
        "q59": "B",
        "q60": "G",
      }
    },
    "reading": {
      "score": "32",
      "correct": "36",
      "incorrect": "4",
      "omitted": "0",
      "answers": {
        "q1": "B",
        "q2": "F",
        "q3": "C",
        "q4": "H",
        "q5": "A",
        "q6": "G",
        "q7": "D",
        "q8": "J",
        "q9": "B",
        "q10": "J",
        "q11": "C",
        "q12": "H",
        "q13": "D",
        "q14": "F",
        "q15": "A",
        "q16": "F",
        "q17": "D",
        "q18": "J",
        "q19": "B",
        "q20": "G",
        "q21": "A",
        "q22": "F",
        "q23": "D",
        "q24": "H",
        "q25": "B",
        "q26": "J",
        "q27": "D",
        "q28": "F",
        "q29": "C",
        "q30": "G",
        "q31": "B",
        "q32": "J",
        "q33": "A",
        "q34": "F",
        "q35": "A",
        "q36": "F",
        "q37": "C",
        "q38": "H",
        "q39": "D",
        "q40": "H"
      }
    },
    "science": {
      "score": "32",
      "correct": "36",
      "incorrect": "4",
      "omitted": "0",
      "answers": {
        "q1": "B",
        "q2": "F",
        "q3": "C",
        "q4": "H",
        "q5": "A",
        "q6": "G",
        "q7": "D",
        "q8": "J",
        "q9": "B",
        "q10": "J",
        "q11": "C",
        "q12": "H",
        "q13": "D",
        "q14": "F",
        "q15": "A",
        "q16": "F",
        "q17": "D",
        "q18": "J",
        "q19": "B",
        "q20": "G",
        "q21": "A",
        "q22": "F",
        "q23": "D",
        "q24": "H",
        "q25": "B",
        "q26": "J",
        "q27": "D",
        "q28": "F",
        "q29": "C",
        "q30": "G",
        "q31": "B",
        "q32": "J",
        "q33": "A",
        "q34": "F",
        "q35": "A",
        "q36": "F",
        "q37": "C",
        "q38": "H",
        "q39": "D",
        "q40": "H"
      }
    }
  }

    d = json.dumps(json_object)
    result = json.loads(d)

    # if request.method == 'GET':
    # {json_object: 'json_object'}
    return render(request,'index.html', {'result':result})



@login_required
def logout(request):
    if request.user.is_authenticated:
        return render(request, 'registration/login.html')

