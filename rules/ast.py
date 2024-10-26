import re

def is_valid_rule(rule_string):
    # Regex pattern to validate rule strings
    # This pattern matches a rule structure that consists of:
    # - Variables (like user attributes)
    # - Logical operators (AND, OR)
    # - Parentheses for grouping
    # A variable can be a sequence of alphanumeric characters and underscores
    pattern = r'^(?:\s*(?:[A-Za-z0-9_]+|\(\s*(?:[A-Za-z0-9_]+(?:\s*(?:>|<|>=|<=|==|!=)\s*[A-Za-z0-9_]+)?)?\s*\)))(?:\s*(AND|OR)\s*(?:[A-Za-z0-9_]+|\(\s*(?:[A-Za-z0-9_]+(?:\s*(?:>|<|>=|<=|==|!=)\s*[A-Za-z0-9_]+)?)?\s*\))\s*)*$'

    # Check if the rule_string matches the pattern
    return bool(re.fullmatch(pattern, rule_string.strip()))

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type        # 'operator' for AND/OR, 'operand' for conditions
        self.left = left        # Left child node
        self.right = right      # Right child node
        self.value = value      # Value for operand nodes (e.g., age > 30)

    def __repr__(self):
        if self.type == 'operator':
            return f"({self.left} {self.value} {self.right})"
        return f"{self.value}"

def create_rule(rule_string):
    # Transform rule_string into an AST or another structure you need
    tokens = re.findall(r'\w+|AND|OR|\(|\)', rule_string)
    return tokens  # Adjust this to create a proper structure for your rules

def evaluate_rule(rule_ast, user_data):
    stack = []
    for token in rule_ast:
        if token in user_data:  # If the token is a variable
            stack.append(user_data[token])
        elif token == 'AND':
            if len(stack) < 2:
                raise ValueError("Insufficient operands for AND operator.")
            right = stack.pop()
            left = stack.pop()
            stack.append(left and right)
        elif token == 'OR':
            if len(stack) < 2:
                raise ValueError("Insufficient operands for OR operator.")
            right = stack.pop()
            left = stack.pop()
            stack.append(left or right)
        # Handle parentheses and other logic as needed

    return stack[0] if stack else False  # Return the final evaluated result

def combine_rules(rules):
    if len(rules) == 0:
        return None
    
    if len(rules) == 1:
        return create_rule(rules[0])
    
    root = create_rule(rules[0])
    
    for rule_string in rules[1:]:
        rule_ast = create_rule(rule_string)
        root = Node(type='operator', left=root, right=rule_ast, value='AND')
    
    return root  # Return the root of the combined AST
