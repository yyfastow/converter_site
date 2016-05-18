from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.hello_nuzz, name='hello_nuzz'),
    url(r'times two/$', views.times_two_view, name='times_two'),
    url(r'tempurature/$', views.ctof_view, name='tempurature'),
    url(r'distance/$', views.distance_view, name='distance'),
    url(r'calculator/$', views.calculator_view, name='calculator'),
    url(r'tip calc/$', views.tip_calc_view, name='tipcalc'),
    url(r'shape/circle/$', views.circle_view, name='circle'),
    url(r'shape/rectangle/$', views.rectangle_view, name='rectangle'),
    url(r'shape/triangle/$', views.triangle_view, name='triangle'),
    url(r'shape/cube/$', views.cube_view, name='cube'),
    url(r'shape/sphere/$', views.sphere_view, name="sphere"),
    url(r'shape/cylinder/$', views.cylinder_view, name="cylinder"),
    url(r'shape/pyramid/$', views.pyramid_view, name="pyramid"),
    url(r'shape/trapezoid/$', views.trapezoid_view, name="trapezoid"),
]