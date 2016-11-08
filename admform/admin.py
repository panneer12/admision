from django.contrib import admin
from .models import TargetSemester, HighestDegree, DegreeAiming, AnnualBudget, SourceOfFund, USAPreference, ClimateCondtion, Countries,UserProfile
from django.utils.translation import ugettext as _


# Register your models here.
admin.site.register([TargetSemester,HighestDegree,DegreeAiming, 
	AnnualBudget, SourceOfFund, USAPreference, ClimateCondtion, Countries])

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
        localized_fields = ('full_name', 'dob')
        labels = {
            'full_name': _('Full Name'),
            'dob': _('Date Of Birth'),
        }
        help_texts = {
            'full_name': _('Some useful help text.'),
        }
        error_messages = {
            'full_name': {
                'max_length': _("This writer's name is too long."),
            },
        }

admin.site.register(UserProfile, UserProfileAdmin)