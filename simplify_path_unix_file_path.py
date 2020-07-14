def simplify_path(path):
    temp_path = path.split("/")
    stack = []
    for i in temp_path:
        if ".." == i:
            if len(stack) > 0:
                stack.pop()
        elif i != "" and i != ".":
            stack.append(i)

    print("/" + "/".join(stack))


simplify_path("/../")
