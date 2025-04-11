class CustomerAgent:
    def __init__(self, customer_data):
        self.customer_data = customer_data

    def get_preferences(self, customer_id):
        customer = self.customer_data[self.customer_data["customer_id"] == customer_id]
        if customer.empty:
            return None
        return customer.to_dict(orient="records")[0]
