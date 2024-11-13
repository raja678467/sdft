# inventory_management_system.py

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class InventoryManagementSystem:
    def __init__(self):
        self.users = []
        self.products = {}
        self.current_user = None
        self.low_stock_threshold = 10
        self.create_default_users()

    def create_default_users(self):
        self.users.append(User("admin", "adminpass", "Admin"))
        self.users.append(User("user", "userpass", "User"))

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Welcome, {user.role} {user.username}!")
                return True
        print("Invalid username or password.")
        return False

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        product = Product(product_id, name, category, price, stock_quantity)
        self.products[product_id] = product
        print("Product added successfully.")

    def edit_product(self):
        product_id = input("Enter product ID to edit: ")
        if product_id in self.products:
            product = self.products[product_id]
            product.name = input("Enter new name: ")
            product.category = input("Enter new category: ")
            product.price = float(input("Enter new price: "))
            product.stock_quantity = int(input("Enter new stock quantity: "))
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self):
        product_id = input("Enter product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        for product_id, product in self.products.items():
            status = "(Low stock)" if product.stock_quantity < self.low_stock_threshold else ""
            print(f"ID: {product_id}, Name: {product.name}, Category: {product.category}, "
                  f"Price: {product.price}, Stock: {product.stock_quantity} {status}")

    def search_product(self):
        search_term = input("Enter product name or category to search: ").lower()
        found = False
        for product in self.products.values():
            if search_term in product.name.lower() or search_term in product.category.lower():
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                      f"Price: {product.price}, Stock: {product.stock_quantity}")
                found = True
        if not found:
            print("No matching products found.")

    def adjust_stock(self):
        product_id = input("Enter product ID to adjust stock: ")
        if product_id in self.products:
            adjustment = int(input("Enter stock adjustment (positive to add, negative to subtract): "))
            product = self.products[product_id]
            product.stock_quantity += adjustment
            print("Stock adjusted successfully.")
        else:
            print("Product not found.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View All Products")
            print("5. Search Product")
            print("6. Adjust Stock")
            print("7. Logout")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.edit_product()
            elif choice == '3':
                self.delete_product()
            elif choice == '4':
                self.view_products()
            elif choice == '5':
                self.search_product()
            elif choice == '6':
                self.adjust_stock()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. View All Products")
            print("2. Search Product")
            print("3. Logout")
            choice = input("Select an option: ")
            if choice == '1':
                self.view_products()
            elif choice == '2':
                self.search_product()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        while True:
            print("\nInventory Management System")
            if self.login():
                if self.current_user.role == "Admin":
                    self.admin_menu()
                elif self.current_user.role == "User":
                    self.user_menu()
            self.current_user = None

# Run the inventory management system
if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()
