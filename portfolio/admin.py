from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)


class InternshipAdmin(admin.ModelAdmin):
    list_display = ('fullname',
                    'usn',
                    'email',
                    'college_name',
                    'offer_status',
                    'end_date',
                    'proj_report')
    search_fields=('fullname','usn,''email')
    list_filter=['college_name','proj_report','offer_status']
admin.site.register(Internship,InternshipAdmin)
