from collections import deque

class Solution(object):
    def walls_and_gates(self, rooms):
        """

        From leetcode:
          https://leetcode.com/problems/walls-and-gates/

        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        
        Brute Force:
            1. Find all the gates O(n)
            2. For each cell O(n)
                a. If it is not a gate
                b. Iterate the gates and calculate distance
                c. Set to the smallest distance
            
            time: O(cells * number of gates) = O(n^2)
            space: O(number of gates) = O(n)
        
        BFS:
            1. Find all of the existing gates O(n)
            2. Append them onto a queue
            3. While the queue has items
                a. Visit nearby neighbors
                b. If is not infinity, continue
                c. Set them to previous_distance + 1
                d. add neighbors to the queue
            
            time: O(number of cells) = O(n) # two passes
            space: O(number of cells)
        """
        
        if not rooms or not rooms[0]:
            return
        
        gates = self.find_gates(rooms)
        queue = deque(gates)
        
        while queue:
            room_row, room_col = queue.popleft()
            current_distance = rooms[room_row][room_col]
            
            for next_row, next_col in self.nearby_rooms(rooms, room_row, room_col):
                if not (0 <= next_row < len(rooms)): continue
                if not (0 <= next_col < len(rooms[0])): continue
                if rooms[next_row][next_col] == -1: continue
                if rooms[next_row][next_col] < float('inf'): continue
                
                rooms[next_row][next_col] = current_distance + 1
                queue.append((next_row, next_col))
                
        
    def nearby_rooms(self, rooms, row, col):
        for row_add, col_add in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            yield row + row_add, col + col_add
    
    
    def find_gates(self, rooms):
        for row_index, row in enumerate(rooms):
            for col_index, value in enumerate(row):
                if value == 0:
                    yield row_index, col_index
  

if __name__ == "__main__":
    solution = Solution()

    rooms = [
      [float('inf'),-1,0,float('inf')],
      [float('inf'),float('inf'),float('inf'),-1],
      [float('inf'),-1,float('inf'),-1],
      [0,-1,float('inf'),float('inf')]]

    solution.walls_and_gates(rooms)
    
    print(rooms)