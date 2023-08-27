def is_balanced(expression):
    stack = []
    brackets_mapping = {'(': ')', '[': ']', '{': '}'} #match each opening bracket to its corresponding closing bracket.
    #uncertain
    # the solution implemented below is a product of stack overflow and chatgpt
    for string in expression:
        if string in brackets_mapping.keys():
            stack.append(string)
        elif string in brackets_mapping.values():
            if not stack  or brackets_mapping[stack.pop()] != string:
                return False
            
    return len(stack) 