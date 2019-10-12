# Time Series Analysis of Amazon Data

## Description

Amazon product prices and other parameters vary with time. This project deals with the analysis of Amazon products data.

## Scope

 - A customer can know the best time to buy a product - before, during or after a sale
 - A company can understand how their productss and their competitors' products' prices, ratings, offers etc. are varying.

## Motivation

E-commerce product prices vary considerably over time. Knowing when to buy a product can help a consumer save money. It can be difficult to decide if a product should be bought at that point of time, or if the price will decrease or increase further.
There is a lack of analysis of Amazon product data, especially Amazon India products. We want to show how the product prices and other details vary over time - before, during and after a sale.

## Dataset

 - The data is collected by performing web scraping on Amazon India.
 - Details of 10 products are scraped periodically over the course of a few months.
 - The Web scraper is made using Scrapy python library. A PostgreSQL database is used to store and add to the database. The scraper and database are deployed to Heroku. The database is exported to a `.csv` file. The scraper program is at [this repository](https://github.com/Samyak2/amazon-scraper) (private repository)
 - The dataset consists of 29 columns.
 - As the data is being scraped everyday, it does not have a fixed number of rows. As of 10-10-2019 it has `1217 rows`.
 - Some of the columns of the dataset are:
     - `name`: Name of the product.
     - `price`: Price of the product including all discounts except lightning deals.
     - `url`: URL of the product.
     - `seller_name`: Name of the main/default seller.
     - `seller_rating`: Star rating of the main/default seller.
     - `num_seller_ratings`: Number of people who have rated the main/default seller.
     - `stars`: Star rating of the product (floating point decimal with one digit after the decimal).
     - `num_reviews`: Number of reviews for the product.
     - `answered_qs`: Number of questions answered. The value is `1000+` if there are more than 1000 questions.
     - `availibity`: Availibility of the product as described by a string. It can take any of these values:
         - `Currently unavailable.`
         - `In stock.`
         - `Only n left in stock.` where n is an integer.
         - `Only n left in stock (more on the way).` where n is an integer.
     - `time`: Time at which the data was scraped (With the timezone as GMT and NOT IST).
     - `deal_price`: Price during a lightning deal. No value is there is no lightning deal.
     - `ASIN`: A unique ID given by Amazon to a product. Not available for all products in this dataset.
     - `brand`: Brand name of the product.
     - `return_policy`: Defines the return policy of the product in a string.
     - `warranty`: Shows the warranty available on the product. Could be of the form `x Year Warranty` or `x Day Warranty`.
     - `pay_on_delivery`: Value can be Null/NaN or `Pay on Delivery`.
     - `amazon_delivered`: Value can be Null/NaN or `Amazon Delivered`.
     - `features`: A list of features in the form of a string with each value in the list separated by `||`.
     - `weight`: weight of the product. Can be different units hence it's a string.
     - `model`: Model number
     - `category`: List of categories the product falls in, in the form of a string with commas `,` as separator