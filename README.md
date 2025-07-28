# Political-Alignment-Classification

## Project Description
Our goal for this project is to classify the political leanings of political articles based on their word choice, in a sense, to train a model to pick up on the political bias of a political article by just looking at the words used in the article. We are exploring different NLP techniques and experimenting with them on both supervised and unsupervised learning techniques to see which model achieves the best natural distinction between the different political leanings.

For this project, we used web scraping with BeautifulSoup to collect political article URLs from news outlets that generally have political leanings of left, center, and right. We used articles from: Left outlets: LA Times, NBC, CNN, MSNBC, NPR Center outlets: Newsweek, ABC, BBC, Forbes, CNBC Right outlets: Fox, Daily Wire, NY Post, Breitbart, Federalist.

We collected the URLs from our URL scrapers and got additional article URLs from GroundNews to create our dataset for articles to scrape the titles and word content from. Our URL dataset with the corresponding stop phrases and start phrases to isolate the actual article content when webscraping.

In order to make our classifiers and analyze the political articles in our dataset, we extracted the article content from all of the articles so we could break down the articles into their individual tokens (words) and attempt to use word choice as the features for classification. We also attempted clustering through K-means and DBSCAN to attempt to find any patterns within the word choice of the political leanings or outlets.

Some other things we tried to find differences across the political leanings were testing sentiment analysis with existing libraries and using features other than words, such as rhetorical question usage and article length, to classify the articles into their respective political leanings.

## Techniques Used
**Bag of Words Model:** We used CountVectorizer to tokenize the titles and content of our articles. The bag of words vectors acted as our list of features for each article. Each unique word in the corpus of documents adds another feature to the list of features.

**TF-IDF:** In order to reduce the impact that words highly used across all articles have on the distance measures of our political article points, we used TF-IDF. We evaluated our classifiers and clustering attempts with and without TF-IDF.

**KNN Classification:** KNN acted as our main classifier technique which uses the word vectors of each article as the representation of each article in space. When testing the classifier, the point being added measures its distance (with cosine similarity) with all of the word vectors of existing political articles and picks the k articles with the closest distance. The new article is classified based on the majority of the k articles closen.

**K-means Clustering:** K-means clustering gives us a means through which we can try to find similarities or patterns among the articles within our dataset without needing to leverage their labeled political leanings. K-means clustering does not visualize well with the large feature vectors that the bag of words model generates. As a result, we tried to carry out k-means clustering with non-word features, such as rhetorical question usage.

**DBSCAN:** DBSCAN is a density based clustering, unsupervised method where the algorithm can cluster non-convex shapes. The algorithm iteratively expands the cluster by going through each individual data point within the cluster. DBSCAN was applied using the bag-of-words and tf-idf vectors. DBSCAN was also used to cluster non-word features like article length.

## Video Presentation
https://github.com/user-attachments/assets/ca1c667e-0f80-47e7-aa8b-4d75cd9c024d

## Libraries used:

**WordCloud:** A visualization tool that creates an image composed of words, where the size of each word indicates its frequency or importance in the text data. It's useful for getting a quick sense of the most common terms in a document.

**VADER (Valence Aware Dictionary and sEntiment Reasoner):** A rule-based sentiment analysis tool specifically tuned for social media and short texts. It classifies text sentiment as positive, negative, or neutral and returns a compound score indicating overall sentiment.

**DistilBERT:** A lightweight, faster version of BERT (Bidirectional Encoder Representations from Transformers) developed by Hugging Face. It retains 97% of BERT’s performance while being smaller and more efficient, making it suitable for NLP tasks like classification, sentiment analysis, and more.

**BeautifulSoup:** A Python library used for parsing HTML and XML documents. It enables easy extraction of data from web pages, often used in web scraping projects.

**pandas:** A powerful Python library for data manipulation and analysis. It provides data structures like DataFrames and Series to handle structured data efficiently.

**requests:** A Python library used to send HTTP/1.1 requests easily. It is commonly used for accessing APIs or retrieving web content (e.g., HTML pages for scraping).

**sklearn (scikit-learn):** A widely-used machine learning library in Python that provides tools for data preprocessing, classification, regression, clustering (like K-means and DBSCAN), model selection, and evaluation.

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** An unsupervised clustering algorithm in scikit-learn that groups together data points that are closely packed together and marks outliers as noise. It's useful for discovering clusters in data without needing to specify the number of clusters in advance.

## Conclusion
After running all of our techniques, we were not able to effectively cluster the political articles into clusters that resembled the general political leanings of each news outlet. We found that unsupervised learning techniques come up short when working with large vectors of features (the bag of words and TF-IDF vectors) because points are very sparse from each other. We observed this through the DB Scan process because the technique found a large number of noise points when using the bag of words and TF-IDF vectors as features while finding a much lower proportion of noise founds when running DB Scan on the numerical features of articles.
When we tried the KNN classifier, we found a bit better results when classifying left and right articles but found very low accuracy when classifying center articles. This leads us to believe that the center articles do not vary enough from the left and right political leanings to effectively classify them. In addition, the presence of the central articles bridges the gap between left and right articles which makes natural clusters harder to form and leads to more error in KNN classification. We tested out this theory by testing out our KNN classifier on podcasts that are either extreme left or extreme right. Our classifer was able to correctly classify the podcast scripts we tested out which suggests that our classifier has a harder time classifying articles that do not lean far toward one side.

We saw some interesting results when comparing sentiment analysis libraries of VADER and DistilBERT. VADER attributed positive sentiment to the right articles and negative sentiment to the left articles. This is expected because the current news will focus on actions taken by the current Republican government. Interstingly, VADER gave central articles the most negative sentiment. We believe this is due to the central articles being critical of both the left and right sides. VADER's sentiment analysis aligned with what we expected the overall sentiment of each political leaning to be. On the other hand, DistilBERT generally classifies all articles as having negative sentiment and is only able to capture some of the positive sentiment from the right articles. This tells us the importance of using suitable training data for model because VADER is trained on social media posts which is similar to our political article dataset while DistilBERT is trained on movie reviews which does not have the same nuance and length as political articles.

## More about the project

Here is the entire report: https://colab.research.google.com/drive/1mC5z1N9d1hBfDal4K3kwPmjvPx9BegWt?usp=sharing

## Contributors
- **Abdi Nava**
[LinkedIn](https://www.linkedin.com/in/abdinava/) | [GitHub](https://github.com/abdinava)

