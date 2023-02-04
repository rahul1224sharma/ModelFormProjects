from django.shortcuts import render
from ModelFormApp import forms
# Create your views here.
def Studentview(request):
    sentdata=False;
    formsobj=forms.StudentForm()
    if request.method=='POST':
        formsobj=forms.StudentForm(request.POST);
        if formsobj.is_valid():
            print('Given or submitted form data')
            formsobj.save(commit=True)
            sentdata=True;
            formsobj=forms.StudentForm()
    return render(request,'ModelFormApp/form.html',{'form1':formsobj,'sentdata':sentdata})