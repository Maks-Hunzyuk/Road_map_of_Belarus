from country import views
from django.urls import path

app_name = 'country'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('show_cities/<int:region_id>', views.CityListView.as_view(), name='show_cities'),
    path('show_routers/', views.show_routers, name='show_routers'),
    path('list_events/', views.events_list, name="events_list"),
    path('photos/', views.show_photos, name='photos'),
    path('content_city/<int:city_id>/', views.show_city_info, name="city_info"),
    path('route_info/<int:route_id>/', views.show_route, name="show_route"),
    path('event_info/<int:event_id>/', views.show_event, name='show_event'),
    path('photos_info/<int:photo_id>/', views.show_photos_info, name='show_photo'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('comments/', views.add_comments),

]
