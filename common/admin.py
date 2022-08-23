from django.contrib import admin
from common.models import User, Address, Comment, Comment_Files, Org, Profile, Comment_Files,Attachments,Document,APISettings,Google

# Register your models here.

admin.site.register(Org)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Comment_Files)
admin.site.register(Attachments)
admin.site.register(Document)
admin.site.register(APISettings)
admin.site.register(Google)


