def checkbp(exp):
    d={")":"(","}":"{","]":"["}
    stack=[]
    for x in exp:
        if x in "{[(":
            stack.append(x)
        elif x in ")}]":
            if not stack:
                print("not balanced",x)
                break
            elif len(stack)!=0:
                if d[x]==stack[-1]:
                    stack.pop()
                else:
                    print("unbalanced exp",x)
        else:
            continue
    if not stack:
        print("balanced parenthesis")
    else:
        print("unbalanced parenthesis")
checkbp("(a*b)")
checkbp("(a*b")
checkbp("(a+b)*(c+d)")
