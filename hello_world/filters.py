import django_filters
from django import forms
from .models import Posts

class postFilter(django_filters.FilterSet):
	published_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}), lookup_expr = 'date__exact')
	
	class Meta:
		model = Posts
		fields = ['published_on']