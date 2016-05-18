from django import template
from converter.models import Shape

register = template.Library() 


@register.inclusion_tag("converter/nav_shape.html")
def nav_shape_list():
    shapes = Shape.objects.all()
    return {'shapes': shapes}
