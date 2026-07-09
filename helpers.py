# GET THE VALID INPUT: 
def get_valid_input(prompt):
  while True:
    user_input = input(prompt).strip()
    if not user_input:
      print("--- Input cannot be empty ---\n")
      continue

    break

  return user_input
