"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.admin import category_admin_site, subcategory_admin_site

urlpatterns = [
    path("admin/", admin.site.urls),
    path('category-admin/',category_admin_site.urls),
    path('subcategory-admin/',subcategory_admin_site.urls)
]


# changing site administration title
admin.site.index_title = "E-Learning"

# changing header

admin.site.site_header = "E-Learning Administration"

# changing site title on browser tab
admin.site.site_title = "E-Learning Admin Site"