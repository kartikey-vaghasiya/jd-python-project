import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use('Agg')

def analyze_and_visualize(file_path):
    # Load CSV data into a DataFrame
    df = pd.read_csv(file_path)

    # Create a static folder if it doesn't exist
    static_folder = 'static'
    os.makedirs(static_folder, exist_ok=True)

    # (1) Brand vs Average Prices Chart
    avg_prices = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    plt.bar(avg_prices.index, avg_prices, color='skyblue')
    plt.title('Brand vs Average Prices')
    plt.xlabel('Brand')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45, ha='right')
    for brand in avg_prices.head(10).index:
        plt.text(brand, avg_prices.loc[brand], f'{avg_prices.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_avg_prices.png'))
    plt.close()

    # (2) Brand vs Average Reviews Chart
    avg_reviews = df.groupby('brand')['reviews'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    plt.bar(avg_reviews.index, avg_reviews, color='lightgreen')
    plt.title('Brand vs Average Reviews')
    plt.xlabel('Brand')
    plt.ylabel('Average Reviews')
    plt.xticks(rotation=45, ha='right')
    for brand in avg_reviews.head(10).index:
        plt.text(brand, avg_reviews.loc[brand], f'{avg_reviews.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_avg_reviews.png'))
    plt.close()

    # (3) Brand vs Average Rating Chart
    avg_rating = df.groupby('brand')['rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    plt.bar(avg_rating.index, avg_rating, color='lightcoral')
    plt.title('Brand vs Average Rating')
    plt.xlabel('Brand')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    for brand in avg_rating.head(10).index:
        plt.text(brand, avg_rating.loc[brand], f'{avg_rating.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_avg_rating.png'))
    plt.close()

    # (4) Brand vs Mode Prices Chart
    mode_prices = df.groupby('brand')['price'].apply(lambda x: x.mode()[0])
    plt.figure(figsize=(10, 6))
    plt.bar(mode_prices.sort_values(ascending=False).index, mode_prices.sort_values(ascending=False), color='skyblue')
    plt.title('Brand vs Mode Prices')
    plt.xlabel('Brand')
    plt.ylabel('Mode Price')
    plt.xticks(rotation=45, ha='right')
    for brand in mode_prices.head(10).index:
        plt.text(brand, mode_prices.loc[brand], f'{mode_prices.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_mode_prices.png'))
    plt.close()

    # (5) Brand vs Mode Reviews Chart
    mode_reviews = df.groupby('brand')['reviews'].apply(lambda x: x.mode()[0])
    plt.figure(figsize=(10, 6))
    plt.bar(mode_reviews.sort_values(ascending=False).index, mode_reviews.sort_values(ascending=False), color='lightgreen')
    plt.title('Brand vs Mode Reviews')
    plt.xlabel('Brand')
    plt.ylabel('Mode Reviews')
    plt.xticks(rotation=45, ha='right')
    for brand in mode_reviews.head(10).index:
        plt.text(brand, mode_reviews.loc[brand], f'{mode_reviews.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_mode_reviews.png'))
    plt.close()

    # (6) Brand vs Mode Rating Chart
    mode_rating = df.groupby('brand')['rating'].apply(lambda x: x.mode()[0])
    plt.figure(figsize=(10, 6))
    plt.bar(mode_rating.sort_values(ascending=False).index, mode_rating.sort_values(ascending=False), color='lightcoral')
    plt.title('Brand vs Mode Rating')
    plt.xlabel('Brand')
    plt.ylabel('Mode Rating')
    plt.xticks(rotation=45, ha='right')
    for brand in mode_rating.head(10).index:
        plt.text(brand, mode_rating.loc[brand], f'{mode_rating.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'brand_vs_mode_rating.png'))
    plt.close()

    # (7) Top 10 Costly Products Chart
    top_prices = df.nlargest(10, 'price')[['product', 'price']]
    plt.figure(figsize=(12, 6))
    plt.barh(top_prices['product'], top_prices['price'], color='purple')
    plt.title('Top 10 Costly Products')
    plt.xlabel('Price')
    plt.ylabel('Product')
    plt.savefig(os.path.join(static_folder, 'top_10_costly_products.png'))
    plt.close()

    # (8) Top 10 Rated Products Chart
    top_ratings = df.nlargest(10, 'rating')[['product', 'rating']]
    plt.figure(figsize=(12, 6))
    plt.barh(top_ratings['product'], top_ratings['rating'], color='orange')
    plt.title('Top 10 Rated Products')
    plt.xlabel('Rating')
    plt.ylabel('Product')
    plt.savefig(os.path.join(static_folder, 'top_10_rated_products.png'))
    plt.close()

    # (9) Top 10 Reviewed Products Chart
    top_reviews = df.nlargest(10, 'reviews')[['product', 'reviews']]
    plt.figure(figsize=(12, 6))
    plt.barh(top_reviews['product'], top_reviews['reviews'], color='green')
    plt.title('Top 10 Reviewed Products')
    plt.xlabel('Reviews')
    plt.ylabel('Product')
    plt.savefig(os.path.join(static_folder, 'top_10_reviewed_products.png'))
    plt.close()

    # (10) Top 10 Brand vs Price/Rating Ratios Chart
    df['price_rating_ratio'] = df['price'] / df['rating']
    top_ratios = df.groupby('brand')['price_rating_ratio'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_ratios.index, top_ratios, color='purple')
    plt.title('Top 10 Brand vs Price/Rating Ratios')
    plt.xlabel('Brand')
    plt.ylabel('Price/Rating Ratio')
    plt.xticks(rotation=45, ha='right')
    for brand in top_ratios.head(10).index:
        plt.text(brand, top_ratios.loc[brand], f'{top_ratios.loc[brand]:.2f}', ha='center', va='bottom', color='black')
    plt.savefig(os.path.join(static_folder, 'top_10_brand_vs_price_rating_ratios.png'))
    plt.close()

    # (11) Additional Analysis 1: Distribution of Prices
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(static_folder, 'distribution_of_prices.png'))
    plt.close()

    # (12) Additional Analysis 2: Correlation between Price and Ratings
    plt.figure(figsize=(8, 8))
    plt.scatter(x=df['price'], y=df['rating'], color='coral', alpha=0.5)
    plt.title('Correlation between Price and Ratings')
    plt.xlabel('Price')
    plt.ylabel('Rating')
    plt.savefig(os.path.join(static_folder, 'correlation_between_price_and_ratings.png'))
    plt.close()


