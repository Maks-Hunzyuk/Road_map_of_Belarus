from country import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'), 
    path('show_cities/<int:region_id>', views.show_cities, name='show_cities'),
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
    # path('get_comment/int<id:comm_id>/', views.get_comment, name='get_comment')
    
]

