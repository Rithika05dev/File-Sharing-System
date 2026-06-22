from django.urls import path
from . import views

urlpatterns = [

    path('', views.my_files, name='my_files'),

    path('upload/', views.upload_file, name='upload'),

     path('shared/', views.shared_files, name='shared_files'),

    path('starred/', views.starred, name='starred'),

    path('trash/', views.trash, name='trash'),

    path('settings/', views.settings_page, name='settings'),

    path('delete/<int:id>/', views.delete_file, name='delete_file'),

    path('share/<int:id>/', views.share_file, name='share_file'),

    path('shared/', views.shared_files, name='shared_files'),

    path('star/<int:id>/',views.toggle_star,name='toggle_star'),

    path('restore/<int:id>/',views.restore_file,name='restore_file'),

    path('permanent-delete/<int:id>/',views.permanent_delete, name='permanent_delete'),
]  