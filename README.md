<div align="center">
  <h1>Fake News Detection</h1>
  <h3>Machine Learning Model to Identify Fake News</h3>
</div>

## 📌 Overview
This project is a Machine Learning application designed to detect fake news articles. It utilizes Natural Language Processing (NLP) techniques and a Logistic Regression model to classify news articles as either **Real** or **Fake** based on their content.

## 📂 Dataset
The project uses the **ISOT Fake News Dataset** (or similar source), consisting of two CSV files:
-   `True.csv`: Contains real news articles.
-   `Fake.csv`: Contains fake news articles.

These files are located in the `datasets/` directory.

## 🛠 Features
-   **Data Preprocessing**: removal of stopwords, stemming, and tokenization.
-   **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
-   **Model**: Logistic Regression for binary classification.
-   **Evaluation**: Accuracy score on training and testing data.

## 🚀 Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd fake_news_detection
    ```

2.  Install dependencies:
    ```bash
    pip install pandas numpy scikit-learn nltk
    ```

3.  Download NLTK stopwords (if not already present):
    ```python
    import nltk
    nltk.download('stopwords')
    ```

## 💻 Usage

1.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook detection.ipynb
    ```
2.  Run all cells to load data, train the model, and evaluate performance.
3.  The notebook includes a manual testing section where you can input a specific news article to see the prediction.

## 📊 Results
The model achieves high accuracy on the test set. (Update with specific accuracy after running).

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
