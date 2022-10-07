from django.apps import AppConfig
# from django.contrib.admin.apps import AdminConfig

# override default admin area to my admin area when we hti /admin this will open by default
# class CategoryAdminConfig(AdminConfig):
#     default_site = 'app.admin.CategoryAdminArea'


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
