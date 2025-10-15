from collections import deque

def lexicographically_smallest_string(s):
    visited = set()
    queue = deque([s])
    smallest = s

    while queue:
        current = queue.popleft()
        if current < smallest:
            smallest = current

        for k in range(1, len(s) + 1):
            # Reverse first k characters
            first_k = current[:k][::-1] + current[k:]
            if first_k not in visited:
                visited.add(first_k)
                queue.append(first_k)

            # Reverse last k characters
            last_k = current[:-k] + current[-k:][::-1]
            if last_k not in visited:
                visited.add(last_k)
                queue.append(last_k)

    return smallest
