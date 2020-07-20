from django.contrib import admin
from .models import Faculity_info,Rejcomplaint,Acomplaint,solcomplaint,Appcomplaint,ComplaintUpdate,dcomplaint
#Register your models here.
class faculity_infoAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','user_name','email']
    list_display_links = ['first_name','user']
    search_fields = ['first_name','department','designation']

class acomplaintAdmin(admin.ModelAdmin):
    list_display = ['id','complain_about','complain_too','complain']
    list_display_links = ['complain_about']
    search_fields = ['complain_about', 'complain_too']
class dcomplaintAdmin(admin.ModelAdmin):
    list_display = ['id','complain_about','complain_too','complain']
    list_display_links = ['complain_about']
    search_fields = ['complain_about', 'complain_too']
class appcomplaintAdmin(admin.ModelAdmin):
    list_display = ['id','complain_about','complain_too','complain']
    list_display_links = ['complain_about']
    search_fields = ['complain_about', 'complain_too']
class rejcomplaintAdmin(admin.ModelAdmin):
    list_display = ['id','complain_about','complain_too','complain']
    list_display_links = ['complain_about']
    search_fields = ['complain_about', 'complain_too']
class solcomplaintAdmin(admin.ModelAdmin):
    list_display = ['id','complain_about','complain_too','complain']
    list_display_links = ['complain_about']
    search_fields = ['complain_about', 'complain_too']
class complaintupdateAdmin(admin.ModelAdmin):
    list_display = ['complain_id','update_desc']
    list_display_links = ['complain_id','update_desc']

admin.site.register(Acomplaint,acomplaintAdmin)
admin.site.register(dcomplaint,dcomplaintAdmin)
admin.site.register(Appcomplaint,appcomplaintAdmin)
admin.site.register(Faculity_info,faculity_infoAdmin)
admin.site.register(Rejcomplaint,rejcomplaintAdmin)
admin.site.register(solcomplaint,solcomplaintAdmin)
admin.site.register(ComplaintUpdate,complaintupdateAdmin)