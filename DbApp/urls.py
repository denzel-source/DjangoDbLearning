from django.urls import path

from . import views

urlpatterns=[

path('',views.bloglist,name='blog_list'),

    path('<int:post_id>',views.blog_detail,name='blog_detail'),
]