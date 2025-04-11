class ProductAgent:
    def __init__(self, product_data):
        self.product_data = product_data

    def get_relevant_products(self, category):
        # Make sure 'Category' column exists
        if "Category" not in self.product_data.columns:
            return []

        # Strip spaces and fix casing
        self.product_data["Category"] = self.product_data["Category"].astype(str).str.strip()

        # Filter by the category
        return self.product_data[self.product_data["Category"] == category]
