from django.contrib import admin

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from admin01.models import Item,score,Team,Heading,Overs,Maindata,Over_count,show_over

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
	pass

admin.site.register(Item,MyModelAdmin)
admin.site.register(Team,MyModelAdmin)
admin.site.register(score,MyModelAdmin)
admin.site.register(Heading,MyModelAdmin)
admin.site.register(Overs,MyModelAdmin)
admin.site.register(Maindata,MyModelAdmin)
admin.site.register(Over_count,MyModelAdmin)
admin.site.register(show_over,MyModelAdmin)
