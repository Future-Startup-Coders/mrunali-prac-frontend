def rotateString(s, goal):
    for i in range(len(s)):
        if s[i] == goal[0]:
            if s[i:] + s[:i] == goal:
                return True
    
    return False

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))

def rotateString(s, goal):
        if len(goal) != len(s):
            return False
            
        s+=s[:-1]
        return goal in s

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))