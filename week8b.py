def postfixEvaluation(s):

    st = []

    for i in range(len(s)):

        c = s[i]

        if c >= '0' and c <= '9':
            temp = int(c)
            st.append(temp)

        else:
            op1 = st.pop()
            op2 = st.pop()

            if c == '+':
                st.append(op2 + op1)

            elif c == '-':
                st.append(op2 - op1)

            elif c == '*':
                st.append(op2 * op1)

            elif c == '/':
                st.append(op2 / op1)

        # continue for all characters

    return st.pop()


s = input("Enter postfix expression: ")

print("Result =", postfixEvaluation(s))