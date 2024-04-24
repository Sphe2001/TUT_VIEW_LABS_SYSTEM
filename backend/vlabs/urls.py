from django.urls import path
from vlabs.views import users_views, applications_views, laboratory_views, computer_views, bookings_views


urlpatterns = [
    path('jwt/create/', users_views.CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', users_views.CustomTokenRefreshView.as_view()),
    path('jwt/verify/', users_views.CustomTokenVerifyView.as_view()),
    path('logout/', users_views.LogoutView.as_view()),


    path('laboratories/',
         laboratory_views.LaboratoryList.as_view()),
    path('laboratories/<uuid:pk>/',
         laboratory_views.LaboratoryDetail.as_view()),

    path('computers/', computer_views.ComputersList.as_view()),
    path('computers/<uuid:pk>/', computer_views.ComputersDetail.as_view(),),

    path('applications/', applications_views.ApplicationsList.as_view(),),
    path('applications/<uuid:pk>/',
         applications_views.ApplicationDetail.as_view()),

    path('bookings/', bookings_views.BookingsList.as_view()),
    path('bookings/<uuid:pk>/', bookings_views.BookingsDetail.as_view(),),
    path('bookings/create/', bookings_views.CreateBookingsAPIView.as_view())

]
