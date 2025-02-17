                if dic[tile] > 0:
                    # Choose the tile, update its count
                    dic[tile] -= 1
                    # Recurse to form new strings by adding this tile
                    dfs(st + tile, dic)
                    # Backtrack: restore the count of the tile
                    dic[tile] += 1

        # Start DFS with an empty string and the tile counts
        dfs("", count)
        
        # Return the number of unique combinations
        return len(answer)        
