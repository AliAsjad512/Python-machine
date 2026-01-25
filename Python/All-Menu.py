def main_menu():
    """Main menu to run all programs"""
    import sys
    
    programs = {
        '1': ('Quick Start Demo', quick_start),
        '2': ('Data Analysis', analyze_sales_data),
        '3': ('Weather App', weather_demo),
        '4': ('File Utilities', lambda: list_directory('.')),
        '5': ('Password Checker', password_checker_demo),
        '6': ('Exit', sys.exit)
    }
    
    while True:
        print("\n" + "="*60)
        print("🐍 PYTHON CODE COLLECTION")
        print("="*60)
        
        for key, (name, _) in programs.items():
            print(f"{key}. {name}")
        
        print("="*60)
        choice = input("\nSelect a program (1-6): ").strip()
        
        if choice in programs:
            name, func = programs[choice]
            print(f"\n▶ Running: {name}")
            print("-"*40)
            
            try:
                func()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user")
            except Exception as e:
                print(f"Error: {e}")
            
            if choice != '6':
                input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Please select 1-6")

def quick_start():
    """Quick start demonstration"""
    # This is the first example from above
    print("🎯 Python Code Ready!")
    print("\nBasic Operations:")
    a, b = 10, 5
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} ** {b} = {a ** b}")
    
    print("\nList Operations:")
    numbers = list(range(1, 6))
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Max: {max(numbers)}")
    
    print("\nString Operations:")
    text = "Hello Python"
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Reversed: {text[::-1]}")

# Run the main menu
if __name__ == "__main__":
    main_menu()