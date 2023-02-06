class Solution:
    def racecar(self, target: int) -> int:
        queue = [[0,1]]
        step = 0
        while queue:
            for i in range(len(queue)):
                position,speed = queue.pop(0)
                if target==position:
                    return step
                else:
                    queue.append([position+speed,speed*2])
                    cur_speed = -1 if speed > 0 else 1
                    if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                        queue.append([position,cur_speed])
            step+=1
      
#         queue = deque()
#         queue.append((0, 1, 0))
#         while queue:
#             currentNode, speed, steps = queue.pop()
            
#             if currentNode==target:
#                 return steps
#             queue.append((currentNode+speed, speed*2, steps+1))
#             if speed > 0:
#                 if currentNode + speed > target:
#                     queue.append((currentNode, -1, steps+1))
#             else:
#                 if currentNode + speed < target:
#                     queue.append((currentNode, 1, steps+1))
   
        
        
            
        