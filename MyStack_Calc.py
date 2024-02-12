def calculation(sym, m, n):
    if sym == '/':
        try:
            n = m / n
            return n
        except ZeroDivisionError:
            print('Can\'t divide by Zero!')

    elif sym == '*':
        n = m * n
        return n
         
    elif sym == '+':
        n = m + n
        return n
       
    elif sym == '-':
        n = m - n
        return n
    
    else:
        print('Invalid Operator!')

if __name__ == "__main__":
    CStack = []                             #calculation stack
    DStack = []                             #display stack
    
    operand1 = input('Enter first operand: ')

    if operand1 == '=':
        print('Exit!')

    else:
        CStack.append(int(operand1))
        DStack.append(CStack[0])
        m = CStack[0]            
        while True:
            operator = input('Enter an operator: ')

# '=' will end the program and display the result 
            if operator == '=':
                if  len(DStack) == 1:
                    print('Result =',str(CStack[0]))
                    break
                else:
                    print('Your Result is:')
                    Final = ' '.join(map(str, DStack))
                    print(f'{Final} = {str(CStack[0])}')
                    break       

# 'c' is to clear the whole stack 
            elif operator.lower() == 'c':
                CStack.clear()
                DStack.clear()
                print('Clear!')

# 'x' will pop the last element from the stack   (pending)
            elif operator.lower() == 'x':
                pass

            elif operator not in ['+', '-', '*', '/']:
                print('Invalid Operator! Please enter a valid operator from +, -, *, /')
                continue

            else:
                CStack.append(operator)
                operand2 = input('Enter second operand: ')

# equal sign is to exit the program and display result
                if operand2 == '=':
                    if  len(DStack) == 1:
                        print('Result =',str(CStack[0]))
                        break
                    else:
                        print('Your Result is:')
                        Final = ' '.join(map(str, DStack))
                        print(f'{Final} = {str(CStack[0])}')
                        break     
# c is to clear the whole stack 
                elif operand2.lower() == 'c':
                    CStack.clear()
                    DStack.clear()
                    print('Clear!')
                    break

# x is to pop the last element of the stack
                elif operand2.lower() == 'x':
                    CStack.pop(-1)

                else:
                    CStack.append(int(operand2))

                    for element in CStack[1:]:
                            DStack.append(element)

                    # reverse all the values of CStack in DStack from top to bottom and then sum it
                    # CStack.reverse()
                    # m = CStack[-1]
                            
                    sym = CStack[1]
                    n = CStack[2]

                    res = calculation(sym, m, n)
                    if res == None:
                        break

                    else:
                        CStack[0] = m = res 
            
                        Final = ' '.join(map(str, DStack))
                        print(f'{Final} = {res}')

                    CStack.pop(-2)
                    CStack.pop(-1)


# list to string in python: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
# Final = ' '.join(str(item) for item in DStack)
# print(f'{Final} = {res}')