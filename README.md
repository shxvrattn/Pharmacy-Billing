# Pharmacy Billing System

A simple Python project for managing pharmacy stock and billing. Built using CSV files, this system allows users to track inventory, add new medicines, and generate bills for customers efficiently.

## Features
* **Billing:** Calculate total costs based on medicine quantity and price.
* **Stock Management:** Add new stock or update existing quantities.
* **Inventory View:** Display all available medicines and their prices.
* **Data Storage:** Uses a CSV file (med.csv) to save data permanently.

## Technical Implementation
* **Lists & Nested Lists:** Used to store inventory data in memory.
* **File Handling:** Implements CSV reading/writing for data persistence.
* **Functions:** Modular code structure for billing and stock updates.

## Usage
1. Make sure you have Python installed.
2. Download `main.py` and `med.csv` to the same folder.
3. Run the program:
	python main.py
4. Select an option from the menu:
 * 1: Create a Bill
 * 2: Add Stock
 * 3: Delete Stock
 * 4: View Current Stock

## Files
* `main.py`: The script containing the logic for billing and inventory.
* `med.csv`: The data file where medicine details are stored.
