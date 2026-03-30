# == (ტოლია)

# 5 == 5 True
# 3 == 7 False
# 10 == 10.0 True 

#  >  (მეტია) 
# 5 > 3    True
# 2 > 4    False
# 10 > 10  False
# 7 > 1    True
# 9 > 8    True

# <  (ნაკლებია)
# 5 < 1 False
# 5 < 10 True
# 10 < 1 False
# 9 < 5 False
 
#  <=  (ნაკლებია ან ტოლია)
# 3 <= 5  True
# 4 <= 4  True
# 6 <= 2  False
# 10 <= 10 True
# 8 <= 9   True

#  >=  (მეტია ან ტოლია)
# 5 >= 5  True
# 6 >= 3  True
# 2 >= 4  False
# 10 >= 10 True
# 7 >= 8   False


#  !=  (არ არის ტოლი)
# 5 != 3  True
# 7 != 7  False
# 10 != 5  False
# 8 != 9  True



#2
# Logical Operator (ლოგიკური ოპერატორი) რომელიც გამოიყენება  მნიშნელობების (true/false) შესადარებლად მათი გამოყენებისას ისინი აბრუნებენ შედეგს ture ან false !

# and (და)
# True and True      # True
# True and False     # False
# False and True     # False
# False and False    # False

# or (ან)
# True or True       # True
# True or False      # True
# False or True      # True
# False or False     # False

print(5 > 3 and 10 > 7)   # True
print(2 == 2 and 3 > 5)   # False
print(True and False)     # False

print(5 < 3 or 8 == 8)    # True
print(False or False)      # False
print(10 > 5 or 2 > 7)    # True

fixed_number = 9
user_input = int(input("გთხოვთ შემოიყვანოთ რიცხვი:"))
if fixed_number > user_input:
    print("თქვენი რიცხვი მეტია ჩემს რიცხვზე")
else: 
    print("თქვენი რიცხვი არ არის მეტი ჩემს რიცხვზე")


name = "nika"
user_name = str(input("გთხოვთ შემოიყვანოთ თქვენი სახელი:"))
if name == user_name:
    print("სახელი ემთხვევა:")
else:
    print("სახელი არ ემთხვევა:") 
 


 #6   
age = int(input("შეიყვანე შენი ასაკი: "))
if age > 18:
    print("შენ ხარ სრულწლოვანი")
else:
    print("შენ არ ხარ სრულწლოვანი")


