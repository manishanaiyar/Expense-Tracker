# Expense Tracker CLI

## Overview
The **Expense Tracker CLI** is a Python-based command-line application designed to help users efficiently manage and track their daily expenses. This lightweight and user-friendly tool allows users to add, view, edit, delete, and filter expenses while also providing a monthly expense summary.

## Features
- 📌 **Add Expense** – Record expenses with an amount, category, and date.
- 📊 **View Expenses** – Display all recorded expenses.
- ✏️ **Edit Expense** – Modify existing expense details.
- ❌ **Delete Expense** – Remove an expense entry.
- 🔍 **Filter by Category** – View expenses based on a specific category (e.g., Food, Travel, Shopping, etc.).
- 📆 **Monthly Summary** – Generate a monthly expense report.

## Technologies Used
- **Python** – Core programming language.
- **JSON** – Used for data storage.
- **OS Module** – Handles file operations.
- **Datetime Module** – Manages date inputs and formatting.

## Installation & Setup
### Prerequisites
Ensure you have Python installed. You can check this by running:
```sh
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/).

### Clone the Repository
```sh
git clone https://github.com/manishanaiyar/Expense-Tracker.git
cd Expense-Tracker
```

### Run the Application
```sh
python app.py
```

## Usage Guide
Once the program starts, the main menu will appear with the following options:
1️⃣ Add Expense  
2️⃣ View Expenses  
3️⃣ Edit Expense  
4️⃣ Delete Expense  
5️⃣ Filter by Category  
6️⃣ Monthly Expense Summary  
7️⃣ Exit  

Simply enter the corresponding number to perform an action.

## Example
**Adding an Expense:**
```
Enter expense amount: 500
Enter expense category (Food, Travel, Shopping, etc.): Food
Enter date (YYYY-MM-DD) [Default: Today]: 2025-02-20
✅ Expense added successfully!
```

**Viewing Expenses:**
```
📊 Your Expenses:
ID: 1 | Amount: ₹500 | Category: Food | Date: 2025-02-20
```

## Future Enhancements
- 🌐 **Web-based Expense Tracker** – Upgrade to a Flask + React web application.
- 🤖 **AI-Powered Categorization** – Implement machine learning for automatic expense categorization.
- 📱 **Mobile App Integration** – Develop a mobile-friendly version.

## Contributing
Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
📧 **Manish Anaiyar**  
GitHub: [manishanaiyar](https://github.com/manishanaiyar)

