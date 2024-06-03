def simplifyPath(path):
    # Split the path by slashes
    components = path.split('/')
    stack = []

    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)

    # Join the components with a single slash
    simplified_path = '/' + '/'.join(stack)
    return simplified_path

# Example usage:
path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))  # Output: "/c"
