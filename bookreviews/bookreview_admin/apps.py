# from django.apps import AppConfig
#
#
# class BookreviewAdminConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'bookreview_admin'

from django.contrib.admin.apps import AdminConfig

class BookreviewAdminConfig(AdminConfig):
    default_site = 'bookreview_admin.admin.BookreviewAdmin'
    name = 'bookreview_admin'
