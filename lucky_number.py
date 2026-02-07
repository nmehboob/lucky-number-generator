import random

def generate_lucky_number(name):
    """Generate a lucky number based on the name"""
    # Use name to create a seed
    seed_value = sum(ord(char) for char in name)
    random.seed(seed_value)
    
    lucky_number = random.randint(1, 100)
    return lucky_number

def main():
    print("=== Lucky Number Generator ===")
    user_name = input("Enter your name: ")
    
    lucky_num = generate_lucky_number(user_name)
    
    print(f"\nHello {user_name}!")
    print(f"Your lucky number today is: {lucky_num}")

if __name__ == "__main__":
    main()
