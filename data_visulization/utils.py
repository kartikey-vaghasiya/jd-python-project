import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os

def generate_charts_and_save_images(csv_file):
    df = pd.read_csv(csv_file)

    # Assume the CSV has columns named 'product', 'cost', 'reviews', 'rating'
    name_column = 'product'  # Change this to the column containing names in your CSV

    # Convert columns to numeric (remove commas)
    numeric_columns = ['cost', 'reviews', 'rating']
    for col in numeric_columns:
        if df[col].dtype == 'O':  # Check if the column is of object (string) type
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')

    # Extract the first two words from the product name for better readability
    df[name_column] = df[name_column].apply(lambda x: ' '.join(x.split()[:2]))

    # Generate charts
    charts_data = {}

    # Bar Chart - Cost
    bar_chart_cost = df.plot.bar(x=name_column, y='cost', legend=False, figsize=(12, 8))
    bar_chart_cost.set_title('Cost of Products')
    bar_chart_cost.set_xlabel('Product')
    bar_chart_cost.set_ylabel('Cost (1k)')
    bar_chart_cost.set_xticklabels(df[name_column], rotation=45, ha='right')  # Rotate x-axis labels
    bar_chart_cost.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))  # Format y-axis labels to '1k'
    plt.tight_layout()
    charts_data['bar_chart_cost'] = plot_to_base64(bar_chart_cost, 'png')

    # Bar Chart - Reviews
    bar_chart_reviews = df.plot.bar(x=name_column, y='reviews', legend=False, figsize=(12, 8))
    bar_chart_reviews.set_title('Number of Reviews for Products')
    bar_chart_reviews.set_xlabel('Product')
    bar_chart_reviews.set_ylabel('Number of Reviews (1k)')
    bar_chart_reviews.set_xticklabels(df[name_column], rotation=45, ha='right')  # Rotate x-axis labels
    bar_chart_reviews.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))  # Format y-axis labels to '1k'
    plt.tight_layout()
    charts_data['bar_chart_reviews'] = plot_to_base64(bar_chart_reviews, 'png')

    # Bar Chart - Rating
    bar_chart_rating = df.plot.bar(x=name_column, y='rating', legend=False, figsize=(12, 8))
    bar_chart_rating.set_title('Ratings of Products')
    bar_chart_rating.set_xlabel('Product')
    bar_chart_rating.set_ylabel('Rating (1k)')
    bar_chart_rating.set_xticklabels(df[name_column], rotation=45, ha='right')  # Rotate x-axis labels
    bar_chart_rating.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))  # Format y-axis labels to '1k'
    plt.tight_layout()
    charts_data['bar_chart_rating'] = plot_to_base64(bar_chart_rating, 'png')

    # Bar Chart - Cost vs Reviews
    bar_chart_cost_reviews = df.plot.bar(x=name_column, y=['cost', 'reviews'], legend=True, figsize=(12, 8))
    bar_chart_cost_reviews.set_title('Comparison of Cost and Reviews for Products')
    bar_chart_cost_reviews.set_xlabel('Product')
    bar_chart_cost_reviews.set_ylabel('Value (1k)')
    bar_chart_cost_reviews.set_xticklabels(df[name_column], rotation=45, ha='right')  # Rotate x-axis labels
    bar_chart_cost_reviews.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))  # Format y-axis labels to '1k'
    plt.tight_layout()
    charts_data['bar_chart_cost_reviews'] = plot_to_base64(bar_chart_cost_reviews, 'png')

    # Bar Chart - Cost vs Rating
    bar_chart_cost_rating = df.plot.bar(x=name_column, y=['cost', 'rating'], legend=True, figsize=(12, 8))
    bar_chart_cost_rating.set_title('Comparison of Cost and Rating for Products')
    bar_chart_cost_rating.set_xlabel('Product')
    bar_chart_cost_rating.set_ylabel('Value (1k)')
    bar_chart_cost_rating.set_xticklabels(df[name_column], rotation=45, ha='right')  # Rotate x-axis labels
    bar_chart_cost_rating.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))  # Format y-axis labels to '1k'
    plt.tight_layout()
    charts_data['bar_chart_cost_rating'] = plot_to_base64(bar_chart_cost_rating, 'png')

    # Pie Chart - Reviews
    pie_chart_reviews = df.plot.pie(y='reviews', labels=df[name_column], autopct='%1.1f%%', legend=False, figsize=(12, 8))
    pie_chart_reviews.set_title('Percentage of Reviews for Products')
    plt.tight_layout()
    charts_data['pie_chart_reviews'] = plot_to_base64(pie_chart_reviews, 'png')

    # Save the images to files
    static_path = 'static'

    for chart_name, image_data in charts_data.items():
        image_path = os.path.join(static_path, f'{chart_name}.png')
        with open(image_path, 'wb') as f:
            f.write(base64.b64decode(image_data))

def plot_to_base64(plot, format='png'):
    buffer = io.BytesIO()
    plot.get_figure().savefig(buffer, format=format, bbox_inches='tight')
    buffer.seek(0)
    image_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    return image_data


