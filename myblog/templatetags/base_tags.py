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
        "category":Category.objects.active()
    }
    return context

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content,classes):
	return {
		"request": request,
		"link_name": link_name,
		"link": "account:{}".format(link_name),
		"content": content,
		"classes":classes,
	}