# Finder: Text Similarity Clustering

This code provides a function to find and cluster similar texts within a DataFrame based on a similarity threshold. It utilizes the SequenceMatcher from the difflib library to calculate text similarity ratios and assigns unique cluster IDs to similar texts. Access the code [[ here ]](https://github.com/ergoncugler/finder-text-similarity-clustering/blob/main/finder.py).

## Functions:
### **text_similarity(text1, text2, similarity_threshold=0.95)**

Calculates the similarity ratio between two texts using SequenceMatcher.

Parameters:
```python
text1 (str): # The first text.
text2 (str): # The second text.
similarity_threshold (float): # The threshold for considering texts as similar. Default is 0.95.
```

Returns:
```python
float: # The similarity ratio between the two texts.
```

### **find_similar_texts(dataframe, text_column, similarity_threshold=0.95)** 

Finds similar texts in a DataFrame and assigns unique IDs to clusters of similar texts.

Parameters:
```python
dataframe (pd.DataFrame): # The input DataFrame containing a column named 'text_column'.
text_column (str): # The name of the DataFrame column to be considered for similarity calculation.
similarity_threshold (float): # The threshold for considering texts as similar. Default is 0.95.
```

Returns:
```python
pd.DataFrame: # Updated DataFrame with an additional 'ID' column.
pd.DataFrame: # Count of unique and repeated items.
```

## Example of Usage:

```python
if __name__ == "__main__":
    # Creating a sample dataframe
    data = { 'text': [...] }
    df = pd.DataFrame(data)

    # Set the desired similarity threshold (e.g., 0.95)
    similarity_threshold = 0.8

    # Specify the desired text column
    text_column = 'text'

    # Find similar texts and IDs
    df, unique_counts = find_similar_texts(df, text_column, similarity_threshold)

    # Display the updated dataframe
    print("Updated DataFrame:")
    display(df.head())

    # Display the count dataframe
    print("\nCount of Unique and Repeated Items (in descending order):")
    display(unique_counts)
```

## Example of Output:

Clustering assigns a unique "ID" to each classified content, making it possible to identify those associated as similar by the same "ID" number, as we see in the example output (calibrated at 80%), below:

![image](https://github.com/ergoncugler/find-similar-texts/assets/81989837/2b90b44e-ada4-4c98-91ed-93979314d6e4)

___

## More About:

Its use is highly encouraged and recommended for academic and scientific research, content analysis, sentiment and speech. It is free and open, and academic use is encouraged. Its responsible use is the sole responsibility of those who adapt and manipulate the data.

___

## Author Info:

Ergon Cugler de Moraes Silva, from Brazil, mailto: <a href="contato@ergoncugler.com">contato@ergoncugler.com</a> / Master's Program in Public Administration and Government, Getulio Vargas Foundation (FGV).

### How to Cite it:

**SILVA, Ergon Cugler de Moraes. Finder: Text Similarity Clustering. (feb) 2024. Avaliable at: <a>https://github.com/ergoncugler/finder-text-similarity-clustering/<a>.**
