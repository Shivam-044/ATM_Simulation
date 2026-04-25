import atm_logic as atm

def show_menu():
    print("\n" + "="*35)
    print(f"{'ATM SYSTEM':^35}")
    print("="*35)
    print("1. [VIEW]    Account Balance")
    print("2. [DEPOSIT] Add Funds")
    print("3. [CASH]    Withdraw Funds")
    print("4. [HISTORY] Mini-Statement")
    print("5. [EXIT]    Terminate Session")
    print("="*35)

def main():
    while True:
        show_menu()
        choice = input("Please select an option (1-5): ").strip()

        if choice == "1":
            print(f"\n>> Current Balance: ${atm.get_balance():,.2f}")

        elif choice == "2":
            val = input("Enter amount to deposit: ")
            success, message = atm.deposit(val)
            print(f">> {message}")

        elif choice == "3":
            print(f"(Note: Daily limit is $500.00)")
            val = input("Enter amount to withdraw: ")
            success, message = atm.withdraw(val)
            print(f">> {message}")

        elif choice == "4":
            print("\n--- TRANSACTION HISTORY ---")
            for entry in atm.get_statement():
                print(entry)
            print("---------------------------")

        elif choice == "5":
            print("\nSession ended. Please take your card. Goodbye!")
            break
        
        else:
            print("\n>> Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()