from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

# Create your models here.
class  TargetSemester(models.Model):
	semester_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.semester_name

class HighestDegree(models.Model):
	degree_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.degree_name

class DegreeAiming(models.Model):
	degree_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.degree_name

class AnnualBudget(models.Model):
	budget_value = models.CharField(max_length = 30)

	def __str__(self):
		return self.budget_value

class SourceOfFund(models.Model):
	fund_by = models.CharField(max_length = 30)

	def __str__(self):
		return self.fund_by

class USAPreference(models.Model):
	preference_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.preference_name

class ClimateCondtion(models.Model):
	condtion_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.condtion_name

class Countries(models.Model):
	countries_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.countries_name

GENDRE_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('d', "Don't wish to specify")
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

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	full_name = models.CharField(max_length = 100, blank=True)
	gender = models.CharField(max_length=1, choices=GENDRE_CHOICES, blank=True)
	dob = models.DateField(blank = True, null = True)
	mobile_number = models.CharField(max_length=10, blank = True)
	email = models.EmailField(blank = True, null = True)
	address = models.CharField(max_length=100, blank = True)
	target_semester = models.ForeignKey(TargetSemester, blank=True, null = True)
	# test scores
	target_gre_date = models.DateField(blank = True, null = True)
	actual_gre_date = models.DateField(blank = True, null = True)
	target_verbal_score = models.IntegerField(blank = True, null = True)
	actual_verbal_score = models.IntegerField(blank = True, null = True)
	target_quant_score = models.IntegerField(blank = True, null = True)
	actual_quant_score = models.IntegerField(blank = True, null = True)
	target_awa_score = models.IntegerField(blank = True, null = True)
	actual_awa_score = models.IntegerField(blank = True, null = True)
	target_toefl_date = models.DateField(blank = True, null = True)
	actual_toefl_date = models.DateField(blank = True, null = True)
	target_toefl_score = models.IntegerField(blank = True, null = True)
	actual_toefl_score = models.IntegerField(blank = True, null = True)
	reading_score = models.IntegerField(blank = True, null = True)
	lestening_score = models.IntegerField(blank = True, null = True)
	speaking_score = models.IntegerField(blank = True, null = True)
	writing_score = models.IntegerField(blank = True, null = True)
	#  acadmic qualifications
	highest_degree = models.ForeignKey(HighestDegree, blank = True, null = True)
	year_of_completion = models.CharField(max_length=1, choices=year, blank = True, null = True)
	cgpa = models.FloatField(blank = True, null = True)
	institute = models.CharField(max_length=250, blank = True, null = True)
	branch = models.CharField(max_length=100, blank = True, null = True)
	subjects = models.CharField(max_length=100, blank = True, null = True)
	work_experience = models.CharField(max_length=1000, blank = True, null = True)
	# study abroad goals
	degree_aiming_for = models.ForeignKey(DegreeAiming, blank = True, null = True)
	area_of_interest_1 = models.CharField(max_length=100, blank = True, null = True)
	area_of_interest_2 = models.CharField(max_length=100, blank = True, null = True)
	reason_for_interest = models.CharField(max_length=1000, blank = True, null = True)
	short_term_goals = models.CharField(max_length=5000, blank = True, null = True)
	long_term_goals = models.CharField(max_length=5000, blank = True, null = True)
	# financing your foreign degree
	annual_budget = models.ForeignKey(AnnualBudget, blank = True, null = True)
	source_of_funds = models.ForeignKey(SourceOfFund, blank = True, null = True)
	# geographical preferences
	usa_city_or_countryside = models.ForeignKey(USAPreference, blank = True, null = True)
	climate_with_USA = models.ForeignKey(ClimateCondtion, blank = True, null = True)
	in_addition_to_USA = models.ForeignKey(Countries, blank = True, null = True)
	# University Preferences
	any_prefered_universities = models.CharField(max_length=150, blank = True, null = True)
	importance_of_factors = models.CharField(max_length=1000, blank = True, null = True)
	subject_area_interest = models.CharField(max_length=1000, blank = True, null = True)
	university_rank = models.CharField(max_length=1000, blank = True, null = True)
	cost = models.IntegerField(blank = True, null = True)
	location = models.IntegerField(blank = True, null = True)
	duration = models.CharField(max_length=50, blank = True, null = True)
	# Any other specific aspects to be considered
	gre_scores_reported_to = models.CharField(max_length=1000, blank = True, null = True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
	    return reverse('userprofile-detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return u"%s" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
