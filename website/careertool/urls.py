from careertool import views
from django.urls import path

urlpatterns = [
    #path('',views.login,name="login"),
    path('',views.main,name="main"),
    path('check',views.check,name="check"),
    path('map',views.map,name="map"),
    path('c1',views.c1,name="c1"),
    path('c2',views.c2,name="c2"),
    path('c3',views.c3,name="c3"),
    path('c4',views.c4,name="c4"),
    path('c5',views.c5,name="c5"),
    path('c6',views.c6,name="c6"),
    path('c7',views.c7,name="c7"),
    path('c8',views.c8,name="c8"),
    path('q1',views.q1,name="q1"),
    path('q2',views.q2,name="q2"),
    path('q3',views.q3,name="q3"),
    path('q4',views.q4,name="q4"),
    path('q5',views.q5,name="q5"),
    path('q6',views.q6,name="q6"),
    path('q7',views.q7,name="q7"),
    path('q8',views.q8,name="q8"),
    path('q9',views.q9,name="q9"),
    path('q10',views.q10,name="q10"),
]