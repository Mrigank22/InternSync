# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload_cv/',views.upload_cv,name='upload_cv'),
    path('create_job/',views.create_job,name='create_job'),
    path('search_job/',views.search_job,name='search_job'),
    path('apply_job/<int:job_id>',views.apply_job,name='apply_job'),
]