# Clothing Store E-Commerce Platform

Welcome to the Clothing Store E-Commerce Platform README. This project is an e-commerce platform for a company that sells clothing items. It allows customers to browse and purchase clothing items while enabling the company to manage their inventory and orders. The program is designed to provide a user-friendly menu-based interface for customers and the company to interact with the database.

## Project Overview

The Clothing Store E-Commerce Platform is built using Object-Oriented Programming (OOP) principles and includes the following features:

### Customer Features

1. **Registration and Login**:
   - Customers can register with their Name, Phone number, Email Id, and Password.
   - Registered customers can log in using their registered Email or Phone and Password.

2. **Browse Clothing Items**:
   - Customers can view all available clothing items on the platform.
   - They can filter items by category, brand, price range, and size.

3. **Add to Cart**:
   - Customers can add clothing items to their cart.

4. **View Cart**:
   - Customers can view all items in their cart.

5. **Checkout**:
   - Customers can enter shipping and payment information to complete their orders.

### Company Features (Admin User)

1. **Add Clothing Items**:
   - The company can add new clothing items to their inventory, providing information such as title, brand, price, category, size, and stock quantity.

2. **Retrieve Clothing Items**:
   - The company can retrieve information about existing clothing items by entering the item ID.

3. **Update Clothing Items**:
   - The company can update the stock quantity, title, brand, price, category, and size of an item in the inventory.

4. **Remove Clothing Items**:
   - The company can remove clothing items from their inventory by entering the item ID.

5. **View Orders**:
   - The company can view all orders made by customers and retrieve information about specific orders.

## Requirements

Before running the project, ensure you have the following:

- Python 3.x installed on your system.
- All necessary validations are implemented.
- Error handling is in place, with appropriate messages displayed to the user.
- A well-structured codebase following OOP principles.
- File handling techniques are used to store logging and error information.

## Project Structure

The project is structured as follows:

- `clothing_store.py`: The main program that implements the e-commerce platform using OOP principles.

## steps to run the project 

To get started with the Clothing Store Management System, follow these steps:

1. **Prerequisites**:
   - Ensure you have Python installed on your system.

2. **Clone the Project**:
   - Clone the project's repository from a version control system like GitHub, or download the project's source code if available.

3. **Navigate to the Project Directory**:
   - Use the `cd` command to navigate to the project directory where your main Python script is located.

4. Make sure you have Python and MySQL installed.

5. Install the required Python packages by running:
   
   ```bash
   pip install mysql-connector-python
   ```

6. Configure the database connection in the script by modifying the following lines:
   
   ```python
   self.mysql = my_database.connect(
       host = "localhost",
       user = "Your User Name",
       password = "Your Password")
   ```

7. **Run the Project**:
   - Run the main Python script that serves as the entry point to your project.

   ```
   python main.py
   ```

   Replace `main.py` with the actual name of your main script.

8. **Interact with the Project**:
   - After running the script, you can interact with the project based on the available functions and features provided by the OOP code.

9. **Customization (Optional)**:
   - If needed, you can customize the project by modifying the code within your Python script. Make changes to the OOP classes and methods to add or modify features.

10. **Testing**:
   - Thoroughly test the project to ensure that it functions as expected and handles various scenarios.

## Database

The system uses a MySQL database to store information about clothing items. The database is named `cloting_store`, and the main table is `clothing_item`.
