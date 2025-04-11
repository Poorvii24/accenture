class RecommenderAgent:
    def __init__(self, customer_agent, product_agent):
        self.customer_agent = customer_agent
        self.product_agent = product_agent

    def recommend(self, customer_id):
        # No preferences provided, so we use a default category
        category = "Electronics"  # ← Make sure this exists in your product file's 'Category' column

        products = self.product_agent.get_relevant_products(category)

        # Return top 5 recommendations
        if not products.empty:
            return products.head(5)
        else:
            return []
