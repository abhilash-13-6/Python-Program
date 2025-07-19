def has_loop(node_map, current=1, visited=None):
    if visited is None:
        visited = set()
    if current is None:
        return False
    if current in visited:
        return True
    visited.add(current)
    return has_loop(node_map, node_map.get(current), visited)

print(has_loop({1:2,2:3,3:2}))
