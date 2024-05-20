address = "1.1.1.1"

dot = "."
sem_dot = "[.]"
new_address = address.replace(dot, sem_dot)
    
print(new_address)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        dot = "."
        sem_dot = "[.]"
        new_address = []

        if dot in address:
            parts = address.split(dot)
            for i in range(len(parts) - 1):
                new_address.append(parts[i])
                new_address.append(sem_dot)
            new_address.append(parts[-1])  # Append the last part without an additional '[.]'

        # Join the list into a single string
            new_address = "".join(new_address)
        return new_address