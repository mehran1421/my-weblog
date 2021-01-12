from django import template
from ..models import Category,Article
from django.http import Http404

register=template.Library()

@register.simple_tag
def title(data="یادداشت های من"):
    return data


@register.inclusion_tag("blog/partials/category_nav.html")
def category_navbar():
    context={
        "category":Category.objects.filter(status=True)
    }
    return context