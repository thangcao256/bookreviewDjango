# from django.contrib import admin
# from django.contrib.auth.admin import User
#
#
# class BookrAdmin(admin.AdminSite):
#     site_header = "Trung tâm đào tạo lập trình SOLID Việt Nam"
#
#
# admin_site = BookrAdmin(name='bookr_admin')
# admin_site.register(User)

from django.contrib import admin
from django.contrib.auth.admin import User

class BookreviewAdmin(admin.AdminSite):
    site_header = "Trung tâm đào tạo lập trình SOLID Việt Nam"

admin.site = BookreviewAdmin(name='bookreview_admin')
admin.site.register(User)
