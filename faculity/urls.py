from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.faculity_login, name='faculitylogin'),
    path('logout/', views.logout, name='logout'),
    path('corhomepage',views.corhomepage,name='corhomepage'),
    path('hodhomepage',views.hodhomepage,name='hodhomepage'),
    path('fachomepage',views.fachomepage,name='fachomepage'),
     path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="faculity/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="faculity/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="faculity/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="faculity/password_reset_done.html"),
         name="password_reset_complete"),
     path('send/<complains_id>', views.send, name='send'),
     path('reject/<complains_id>', views.reject, name='reject'),
     path('rej/<complains_id>', views.rej, name='rej'),
      path('reje/<complains_id>', views.reje, name='reje'),
     path('solution/<complains_id>', views.solution, name='solution'),
     path('solve/<complains_id>', views.solve, name='solve'),
     path('sol/<complains_id>', views.sol, name='sol'),
     path('sole/<complains_id>', views.sole, name='sole'),
     path('approved/<complains_id>', views.approved, name='approved'),
     path('approve/<complains_id>', views.approve, name='approve'),
     path('track/', views.track, name='track'),
     
]