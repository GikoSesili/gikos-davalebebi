# ცვლადი (Variable) არის სახელი, რომელიც მიუთითებს მეხსიერების უჯრედზე,
# სადაც ინახება რაღაც მნიშვნელობა (მონაცემი).
# ცვლადი გვაძლევს საშუალებას შევინახოთ ინფორმაცია და მოგვიანებით გამოვიყენოთ ან შევცვალოთ.
# 2) ცვლადის შექმნა
favorite_movie = "Inception"   # შენი საყვარელი ფილმი (შეგიძლია შეცვალო)

# 3) ცვლადის მნიშვნელობის გამოტანა
print(favorite_movie)
first_part = "გამარჯობა, "
second_part = "მსოფლიო!"

# კონკატინაცია (შეერთება)
result = first_part + second_part
print(result)   # გამოიტანს: გამარჯობა, მსოფლიო!
my_name = "დავით"   # შეცვალე შენი სახელით თუ გინდა

# გამოტანა 10-ჯერ
for i in range(10):
    print(my_name)
print((my_name + "\n") * 10)
# სტრინგი (str)
name = "დავით"

# მთელი რიცხვი (int)
age = 25

# ათწილადი (float)
height = 1.78

# შემოწმება ტიპების
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(height)) # <class 'float'>
# თავდაპირველად სტრინგი
info = "ჩემი ასაკი არის"

# განახლება — ახლა ინტეჯერი (რიცხვი) ინახება
info = 28

print(info)         # გამოიტანს: 28
print(type(info))   # <class 'int'>
# 1) კომენტარი ცვლადის შესახებ
# ცვლადი არის სახელი, რომელიც ინახავს მონაცემებს მეხსიერებაში.

# 2) და 3)
favorite_movie = "Inception"
print("ჩემი საყვარელი ფილმია:", favorite_movie)

# 4)
greeting = "გამარჯობა"
name = "დავით"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# 5)
my_name = "დავით"
print((my_name + "\n") * 10)

# 6)
name = "დავით"      # str
age = 25            # int
height = 1.78       # float

# 7)
info = "ტესტი"
info = 100          # ახლა ინტეჯერია
print(info)
