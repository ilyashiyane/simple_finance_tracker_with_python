# 💰 Personal Finance Tracker (CLI)

A simple and efficient **command-line personal finance tracker** built with Python.
This application allows users to manage their income and expenses, view summaries, and organize transactions by category.

---

## 🚀 Features

* ➕ Add income and expenses
* 📊 View financial summary (total income, expenses, balance)
* 📂 Filter transactions by category
* 📜 Display all transactions in a clean format
* 💾 Persistent storage using JSON file
* 🧭 Interactive CLI using `questionary`

---

## 🛠️ Technologies Used

* Python 3.x
* `questionary` (for interactive CLI menus)
* `json` (data storage)
* `datetime` (date validation)
* `os` (file handling)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
```

2. Install dependencies:

```bash
pip install questionary
```

---

## ▶️ Usage

Run the application:

```bash
python AP.py
```

You will see an interactive menu:

```
PERSONAL FINANCE TRACKER
1. Add income
2. Add expense
3. View all transactions
4. View summary
5. Filter by category
6. Save & Quit
```

---

## 📁 Data Storage

All transactions are saved locally in:

```
transactions.json
```

Each transaction includes:

* Type (income / expense)
* Amount
* Category
* Description
* Date (YYYY-MM-DD)

---

## 📊 Example Output

```
2026-06-03  income     Salary          +5000.00 DH  Monthly salary
2026-06-02  expense    Food            -120.50 DH   Groceries
```

---

## ⚙️ Validation

* Date format must be: `YYYY-MM-DD`
* Year must be between **1950 and current year**
* Amount must be a positive number

---

## 📌 Future Improvements

* Export data to CSV
* Monthly reports
* Data visualization (charts)
* GUI version (Tkinter / Web app)

---

## 👤 Author

Hiyane Ilyas

---

## 📄 License

This project is open-source and available under the MIT License.
