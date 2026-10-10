import string
import random
import sys

# Tool Name: Secure Password Generator[cite: 7]
# Author: Saad

def show_help():
    print("==========================================")
    print("      SECURE PASSWORD GENERATOR HELP      ")[cite: 7]
    print("==========================================")
    print("Usage:")
    print("  python password_generator.py          - Generate a password with prompt")[cite: 7]
    print("  python password_generator.py --help   - Show this help menu")[cite: 7]
    print("==========================================")

def generate_password(length=12):
    try:
        if length < 8:
            print("[-] Warning: Password length should be at least 8 characters for security.")
            length = 8
            
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    except Exception as e:
        print(f"[-] Error generating password: {e}")[cite: 7]
        return None

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_help()
        return

    print("==========================================")
    print("        SECURE PASSWORD GENERATOR         ")
    print("==========================================")
    
    try:
        user_input = input("Enter password length (Default 12): ")
        length = int(user_input) if user_input.strip().isdigit() else 12
        
        pwd = generate_password(length)
        if pwd:
            print(f"\n[+] Generated Secure Password: {pwd}")
            print("==========================================")
    except KeyboardInterrupt:
        print("\n[-] Program cancelled by user.")

if __name__ == "__main__":
    main()