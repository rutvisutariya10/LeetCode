                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Append the cloned neighbor to the current node's neighbors list
                mapping[curr].neighbors.append(mapping[neighbor])
        
        return mapping[node]  # Return the cloned version of the start node

                # If the neighbor is not yet cloned, clone it and add it to the queue
            for neighbor in curr.neighbors:
            # Iterate through the neighbors of the current node
            
            curr = queue.popleft()
        while queue:
        
        mapping = {node: Node(node.val)}  # Create the first node in mapping
