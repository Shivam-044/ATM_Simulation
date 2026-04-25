# ATM Simulation Engine 🏦

A professional-grade terminal application demonstrating a decoupled **Package Architecture** and reliable financial state management.

## ⚙️ Core Logic Features
- **Input Validation:** Prevents crashes from non-numeric inputs.
- **Business Rules:** Implements a $500.00 daily withdrawal limit.
- **Precision Formatting:** Uses currency-grade string formatting for all balances.
- **Transaction Ledger:** Real-time logging of all account activities.

## 🛠 Project Structure
- `atm_logic.py`: Contains the "Service Layer" where all math and validation reside.
- `main.py`: The "Presentation Layer" managing the infinite menu loop.

## 🚀 Usage
1. Clone the repo: `git clone https://github.com/Shivam-044/ATM-Simulation.git`
2. Run the system: `python main.py`

---
*Developed with a focus on Clean Code and Separation of Concerns.*