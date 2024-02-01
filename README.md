# **Data Analysis Report - Seungmin Lee**

## Introduction

- This analysis aims to explore the relationship between product prices and the number of reviews for items sold in shopping malls.
- The dataset was obtained by scraping data from the home and living category on the online shopping platform Etsy.
- The insights derived from this analysis will help devise strategies for setting optimal prices for home and living products to potentially increase sales rates, operating under the assumption that the number of reviews correlates with the sales performance.

The primary question guiding this analysis is:

- Does a lower product price correlate with a higher number of reviews?

## Data Description

The dataset comprises 1,472 rows and includes the following columns:

- **Title**: String variable representing the product title.
- **Price**: String variable denoting the product price.
- **Review**: String variable indicating the number of reviews for each product.

## Methodology

### Data Crawling

- The data was collected by scraping 50 pages of product data from Etsy's home and living category using BeautifulSoup.
- The objective was to extract the product name, price, and number of reviews. Error handling mechanisms were implemented to remove irrelevant data, resulting in a dataset free of missing values.

### Data Preprocessing

- Numeric units, such as "k" in the review column, were standardized to numerical values.
- Rows with zero prices were removed.
- Leading string characters, such as commas, in the price column were removed to retain only numerical values.

### Data Visualization

Matplotlib was utilized to create visualizations, including bar charts, to illustrate the distribution and relationships within the dataset.

## Analysis

Prior to analysis, basic statistics for the dataset regarding reviews were computed, including:

- Mean: 3906.62
- Median: 1027.5
- Standard Deviation: 8639.46
- Maximum: 92128.0
- Minimum: 1.0

- **Does a lower product price correlate with a higher number of reviews?**:



## Results

It was confirmed that reviews of products with a low price (~100) were significantly more than those with a higher price.
In addition, the higher the price, the fewer reviews, indicating that home and living category items are chosen by consumers as the price is lower.

## Self-Feedback

