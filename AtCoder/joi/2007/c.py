from string import ascii_uppercase as u

c = u[3:] + u[:3]
t = dict(zip(c, u))
s = input()

print("".join([t[i] for i in s]))
