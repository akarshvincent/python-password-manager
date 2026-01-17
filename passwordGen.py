def generate_password():
  from random import randint, choice, shuffle
  import string
  letters = list(string.ascii_letters)
  numbers = list(string.digits)
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  append_letter = [choice(letters) for _ in range(randint(8, 10))]
  append_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  append_symbols = [choice(symbols) for _ in range(randint(2, 4))]

  password_list = append_letter + append_numbers + append_symbols

  shuffle(password_list)

  password = "".join(password_list)
  return password
  print(f"Your password is: {password}")
