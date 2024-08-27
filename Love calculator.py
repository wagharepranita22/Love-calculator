print("Welcome to the Love calculator !")
first = input("Your name :").lower()
second = input("their name name : ").lower()
love = first + second

l = love.count("l")
o = love.count("o")
v = love.count("v")
e = love.count("e")
t1 = int(l+o+v+e)

t = love.count("t")
u = love.count("u")
r = love.count("r")
e = love.count("e")
t2 = int(t+u+r+e)
t1 = str(t1)
t2 = str(t2)

t3 = t1+t2
t3=int(t3)
if t3 <= 10 and t3 >= 90:
    print(f"your score {t3},you go with each other like mentos and coke")
elif t3 in range(40,50):
    print(f"Your score  {t3},your alright together")
else:
    print(f"Your score {t3}!")

