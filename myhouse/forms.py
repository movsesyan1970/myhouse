from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from account.models import HouseUser

import re


class CreateUserForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    confirm_email = forms.CharField(label='Confirm email')
    complete_ssn = forms.CharField(max_length=11,help_text="In form 'xxx-xx-xxxx'")

    class Meta:
	model = HouseUser
	fields = ['title','first_name','last_name','suffix','sex','email','dob']

    def clean(self):
	cleaned_data = super(CreateUserForm,self).clean()

	if 'complete_ssn' in cleaned_data:
	    complete_ssn = cleaned_data['complete_ssn']
	    if not re.match('^\d{3}-\d{2}-\d{4}$',complete_ssn):
		self.add_error('complete_ssn',"Invalid ssn provided")

	if 'email' in cleaned_data and 'confirm_email' in cleaned_data:
	    email = cleaned_data['email']
	    confirm_email = cleaned_data['confirm_email']
	    if email != confirm_email:
		self.add_error('confirm_email', "Email Confirmation mismatch")

	if 'password' in cleaned_data and 'confirm_password' in cleaned_data:
	    password = cleaned_data['password']
	    confirm_password = cleaned_data['confirm_password']
	    if password != confirm_password:
		self.add_error('confirm_password',"Password confirmation mismatch")
	else:
	    self.add_error('password', "Password may not be emty")

class LoginUserForm(ModelForm):
#    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
	model = User
	fields = ['email','password']

"""
class AddressForm(ModelForm):

    class Meta:
	model = BasicAddress
	fields = ['str_line_1','str_line_2','appt_unit','city','state','zip_code','country']


"""