import pandas as pd
import matplotlib.pyplot as plt

column_names = ["id", "name", "price", "url", "seller_name", "seller_rating", "num_seller_ratings", "stars", "num_reviews", "amazon_choice", "answered_qs", "availibity", "more_product_links", "time", "lightning_deal", "deal_price", "ASIN", "brand", "return_policy", "warranty", "pay_on_delivery", "amazon_delivered", "cart_count", "features", "num_offers", "lowest_price", "weight", "model", "category"]
amazon_data = pd.read_csv("amazon_data_10-10-19h.csv", delimiter=";")
# amazon_data.columns = column_names
# amazon_data.to_csv("amazon_data_10-10-19h.csv", sep=";", encoding="utf-8", index=False)

print(amazon_data.head())

grouped_by_name = amazon_data.groupby("name")

for group_name, group_data in grouped_by_name:
    print(group_name)
    print(list(group_data["stars"]))
    plt.plot(list(group_data["stars"]))
    plt.show()