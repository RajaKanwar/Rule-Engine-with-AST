from django.urls import path
from .views import create_rule_view, evaluate_rule_view, combine_rules_view

app_name = 'rules'  # Use if you're using namespacing
urlpatterns = [
    path('create/', create_rule_view, name='create_rule'),
    path('evaluate/', evaluate_rule_view, name='evaluate_rule'),
    path('combine/', combine_rules_view, name='combine_rules'),
]
