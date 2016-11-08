from django import forms
from django.forms import extras
from django.forms import ModelForm
from .models import UserProfile
from django.contrib.admin import widgets
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    dob = forms.CharField(label='Date of Birth')

    class Meta:
        model = UserProfile
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['target_gre_date'].widget = widgets.AdminDateWidget()

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


CHOICES = (
    (0, 'Male'), 
    (1, 'Female'), 
    (2, 'Other'),
)
year = (
	(0, '2014 or earlier'),
	(1, '2015'),
	(2, '2016'),
	(3, '2017'),
	(4, '2018'),
	(5, '2019'),
	(6, '2020 and above')
)
year_of_completion =  2000
class NameForm(forms.Form):
	# basic information
    full_name = forms.CharField(label='Full name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required = False)
    dob = forms.DateField(label='Date Of Birth',required = False)
    mobile_number = forms.CharField(max_length=10, required = False)
    email = forms.EmailField(label='Your Email', max_length=100, required = False)
    address = forms.CharField(label='Address', required = False)
    target_semester = forms.ChoiceField(choices=CHOICES,required = False)
    # test scores
    target_gre_date = forms.DateField(required = False)
    actual_gre_date = forms.DateField(required = False)
    target_verbal_score = forms.IntegerField(required = False)
    actual_verbal_score = forms.IntegerField(required = False)
    target_quant_score = forms.IntegerField(required = False)
    actual_quant_score = forms.IntegerField(required = False)
    target_awa_score = forms.IntegerField(required = False)
    actual_awa_score = forms.IntegerField(required = False)

    target_toefl_date = forms.DateField(required = False)
    actual_toefl_date = forms.DateField(required = False)
    target_toefl_score = forms.IntegerField(required = False)
    actual_toefl_score = forms.IntegerField(required = False)
    reading_score = forms.IntegerField(required = False)
    lestening_score = forms.IntegerField(required = False)
    speaking_score = forms.IntegerField(required = False)
    writing_score = forms.IntegerField(required = False)
   	#  acadmic qualifications
    highest_degree = forms.ChoiceField(choices=CHOICES, required = False)
    year_of_completion = forms.ChoiceField(choices=year, required = False)
    cgpa = forms.CharField(required = False)
    institute = forms.CharField(label='Institute and Affiliation', required = False)
    branch = forms.CharField(label='Branch / Major', required = False)
    subjects = forms.CharField(label='Subjects you liked', required = False)
    work_experience = forms.CharField(widget=forms.Textarea, required = False)
 	# study abroad goals
    degree_aiming_for = forms.MultipleChoiceField(choices=CHOICES, required = False)
    area_of_interest_1 = forms.CharField(required = False)
    area_of_interest_2 = forms.CharField(required = False)
    reason_for_interest = forms.CharField(required = False)
    short_term_goals = forms.CharField(required = False)
    long_term_goals = forms.CharField(required = False)

    # financing your foreign degree
    annual_budget = forms.MultipleChoiceField(choices=CHOICES, required = False)
    source_of_funds = forms.MultipleChoiceField(choices=CHOICES, required = False)
    # geographical preferences
    usa_city_or_countryside = forms.MultipleChoiceField(choices=CHOICES, required = False)
    climate_with_USA = forms.MultipleChoiceField(choices=CHOICES, required = False)
    in_addition_to_USA = forms.MultipleChoiceField(choices=CHOICES, required = False)
    # University Preferences
    any_prefered_universities = forms.CharField(required = False)
    importance_of_factors = forms.CharField(required = False)
    subject_area_interest = forms.CharField(required = False)
    university_rank = forms.CharField(required = False)
    cost = forms.IntegerField(required = False)
    location = forms.IntegerField(required = False)
    duration = forms.CharField(required = False)
    # Any other specific aspects to be considered
    gre_scores_reported_to = forms.CharField(required = False)


class ExampleForm(forms.Form):
    char_field = forms.CharField()
    choice_field = forms.ChoiceField(choices=CHOICES)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    file_fied = forms.FileField()
    password_field = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    boolean_field = forms.BooleanField()
