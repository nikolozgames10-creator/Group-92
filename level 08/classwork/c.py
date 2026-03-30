 # Logical Operators (ლოგიკური ოპერატორები) გამოიყენება True/False მნიშვნელობებთან მუშაობისთვის
# Python-ში გვაქვს 3 ძირითადი ლოგიკური ოპერატორი:
# 1) and
# 2) or


#  1 AND ოპერატორი
# აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე მხარე True არის
# სხვა ყველა შემთხვევაში აბრუნებს False-ს

# მაგალითები
# True and True  True
# True and False False
# False and True False
# False and False  False


#  2 OR ოპერატორი
# აბრუნებს True-ს, თუ მინიმუმ ერთი მაინც არის True
# მხოლოდ მაშინ აბრუნებს False-ს, როცა ორივე False არის

# მაგალითები
# True or True  True
# True or False  True
# False or True True
# False or False False


print(2 < 5)      #True
print(9 < 4)      #False
print(6 < 6)      #False


print(2 < 5)      #True
print(9 < 4)      #False
print(6 < 6)      #False

print(5 > 3 and 10 > 7)   #True (ორივე პირობა სწორია)
print(5 < 3 or 8 > 2)     #True (მეორე პირობა სწორია)