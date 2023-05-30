from django.contrib import admin
from django.urls import path, include
from accounts import views
from accounts.views import HomePageView, SignUpView, SignInView, VacancyPostingView, posted_vacancies, tenants_list, ApartmentDetailsView, ProfileView, apartment_edit, apartment_delete, tenant_details

app_name = 'accounts'

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
   
    path('make-request/', views.make_request, name='make_request'),
    path('owner/requests/', views.owner_requests, name='owner_requests'),
    path('login/', SignInView.as_view(), name='login'),
    path('vacancy-posting/', VacancyPostingView.as_view(), name='vacancy_posting'),
    path('posted-vacancies/', posted_vacancies, name='posted_vacancies'),
    
    path('accounts/', include('django.contrib.auth.urls')),
   path('apartment/<int:pk>/', ApartmentDetailsView.as_view(), name='apartment_details'),
   path('profile/', ProfileView.as_view(), name='profile'),
 path('accounts/profile/', views.profile, name='profile'),
 path('tenants-list/', views.tenants_list, name='tenants_list'),
path('apartment/<int:pk>/delete/', views.apartment_delete, name='apartment_delete'),
    path('apartment/<int:apartment_id>/edit/', views.apartment_edit, name='apartment_edit'),
    path('tenant/<str:username>/', views.tenant_details, name='tenant_details'),
     path('start_chat/<str:username>/', views.start_chat, name='start_chat'),
path('chat/<int:chat_id>/', views.chat, name='chat'),

    # Other URL patterns
    # Add other URL patterns for login, chat, notifications, etc.
]
