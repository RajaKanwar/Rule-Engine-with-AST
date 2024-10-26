from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Rule
from .ast import create_rule, evaluate_rule, combine_rules, is_valid_rule
import json 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only use this decorator if you want to disable CSRF for the view
def create_rule_view(request):
    if request.method == 'POST':
        rule_id = request.POST.get('rule_id')
        rule_string = request.POST.get('rule_string')

        if not is_valid_rule(rule_string):
            return render(request, 'rules/create_rule.html', {'error': 'Invalid rule structure'})

        rule = Rule(rule_id=rule_id, rule_string=rule_string)
        rule.save()
        return redirect('rules:create_rule')

    return render(request, 'rules/create_rule.html')


@csrf_exempt  # Only if CSRF needs to be disabled for this view
def evaluate_rule_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            rule_string = data.get('rule_string', '')
            user_data = data.get('user_data', {})

            # Validate the rule string
            if not is_valid_rule(rule_string):
                return JsonResponse({'error': 'Invalid rule string.'}, status=400)

            # Create the rule AST and evaluate it
            rule_ast = create_rule(rule_string)
            evaluation_result = evaluate_rule(rule_ast, user_data)

            return JsonResponse({'result': evaluation_result})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


def combine_rules_view(request):
    if request.method == 'POST':
        rule_ids = request.POST.getlist('rule_ids')  # Expecting a list of rule IDs
        rules = []

        for rule_id in rule_ids:
            try:
                rule = Rule.objects.get(rule_id=rule_id.strip())  # Strip whitespace from rule IDs
                rules.append(rule.rule_string)
            except Rule.DoesNotExist:
                return JsonResponse({'error': f'Rule {rule_id} not found'}, status=404)

        combined_rule_ast = combine_rules(rules)
        return JsonResponse({'combined_rule_ast': repr(combined_rule_ast)})

    return render(request, 'rules/combine_rules.html')
