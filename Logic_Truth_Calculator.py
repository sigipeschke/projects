"""
This file will take an input logic statement
This statement must be restricted to using the 5 basic logic sentential operators
and, or, not, if/then, if and only if
The logic used must also be restricted to 2 valued logic i.e. either True or False

Siegfried Peschke
Completed October 29, 2019
"""
class ComplexSentence:
    name = 'empty'
    value = True

def and_(p, q):
    """
    Has the form p & q
    """
    if p == True and q == True:
        return True
    else:
        return False
def or_(p, q):
    """
    Has the form p v q
    """
    if p == False and q == False:
        return False
    else:
        return True
def not_(p):
    """
    Has the form ~p
    """
    if p == True:
        return False
    else:
        return True
def if_(p, q):
    """
    Has the form p -> q
    """
    if p == True and q == False:
        return False
    else:
        return True
def iff_(p, q):
    """
    Has the form p <-> q
    """
    if p == q:
        return True
    else:
        return False
    
def userinput():
    """
    Takes user input to build the compound sentence.
    First it will take the variable names and associated truth value
    Then it will take the logical statement.
    Returns a dictionary with keys as variables names and values as truth values
    and the logical statement as a list.
    """
    var_dict = {}
    print('Input the variable names and their associated truth values \n'
          ' Use the format: Letter:Truth Value \n'
          ' Use T for True and F for False \n'
          ' Example: P:F \n'
          ' After each variable press return \n'
          ' Once finished type "end"')
    continueLoop = True
    while continueLoop == True:
        userin = input()
        if userin == 'end':
            continueLoop = False
        else:
            splituserin = userin.split(':')
            if len(userin) != 3:
                print('Incorrect format, try again')
            elif splituserin[1] == 'T':
                var_dict.update({splituserin[0] : True})
            elif splituserin[1] == 'F':
                var_dict.update({splituserin[0] : False})
            else:
                print('Incorrect format, try again')
            
    print('Input the logic statement using these rules: \n'
          ' and = & \n'
          ' or = v \n'
          ' not = ~ \n'
          ' if/then = -> \n'
          ' if and only if = <-> \n'
          ' Use round brackets to indicate order of operations. \n'
          ' You must use round brackets on negation statements as well. Ex: (~B) \n'
          ' Example: ((AvB)&(~(A&B)))')
    sentence = input()
    sentence = list(sentence)
    return var_dict, sentence

def identify_variable_t_vals(statement, var_dict):
    """
    Identifies the two variables in a simple statement
    """
    t_val_list = []
    for i in range(len(statement)):
        if statement[i] in var_dict:
            t_val_list.append(var_dict.get(statement[i]))
    return t_val_list

def identify_t_val(statement, t_vals):
    """
    Identifies what kind of operator is being used in a simple statement. Then calculates the truth value.
    """
    for i in range(len(statement)):
        if statement[i] == '&':
            return and_(t_vals[0], t_vals[1])
        elif statement[i] == 'v':
            return or_(t_vals[0], t_vals[1])
        elif statement[i] == '~':
            return not_(t_vals[0])
        elif statement[i] == '-':
            try:
                if statement[i+1] == '>':
                    return if_(t_vals[0], t_vals[1])
            except:
                print('Error: Invalid logic statement')
                return
        elif statement[i] == '<':
            try:
                if statement[i+1] == '-':
                    if statement[i+2] == '>':
                        return iff_(t_vals[0], t_vals[1])
            except:
                print('Error: Invalid logic statement')
                return
        else:
            pass
    print('Error: No logic statement found')
    return

def identify_brackets(statement):
    """
    This function identifies where open and close brackets lie and there string index.
    """
    brack_list = []
    for i in range(len(statement)):
        if statement[i] == '(':
            brack_list.append([i, statement[i]])
        elif statement[i] == ')':
            brack_list.append([i, statement[i]])
        else:
            pass
    return brack_list

def identify_parsing_order(statement):
    """
    This function identifies the order of operations based on brackets.
    Returns a list, whose elements contain pairs of statements and
    whose indices are the order of operations.
    """
    brackets = identify_brackets(statement)
    parsing_list = []
    for a in range(len(brackets)):
        if brackets[a][1] == ')':
            b = a
            while brackets[b][1] != '(':
                b -= 1
            parsing_list.append([brackets[b][0], brackets[a][0]])
            brackets[a] = ['nil', 'nil']
            brackets[b] = ['nil', 'nil']
    return parsing_list

def calc_truth_value(statement, var_dict):
    parsed_order = identify_parsing_order(statement)
    for i in range(len(parsed_order)):
        a, b = parsed_order[i]
        t_vals = identify_variable_t_vals(statement[a:b], var_dict)
        t_val = identify_t_val(statement[a:b], t_vals)
        var_dict.update({str(i) : t_val})
        statement[a+1] = str(i)
        for j in range(a+2,b):
            statement[j] = ','
    return t_val

def main():
    var_dict, statement = userinput()
    truth_value = calc_truth_value(statement, var_dict)
    print('The truth value of your statement is', truth_value, '\n')
    print('Would you like to calculate a new statement? \n'
          'Type "Y" for yes or "N" for no.')
    answer = input()
    if answer == 'Y':
        main()
    else:
        return

main()
