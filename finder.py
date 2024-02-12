import pandas as pd
from difflib import SequenceMatcher

def text_similarity(text1, text2, similarity_threshold=0.95):
    """
    Calculate the similarity ratio between two texts using SequenceMatcher.

    Parameters:
    - text1 (str): The first text.
    - text2 (str): The second text.
    - similarity_threshold (float): The threshold for considering texts as similar. Default is 0.95.

    Returns:
    - float: The similarity ratio between the two texts.
    """
    return SequenceMatcher(None, text1, text2).ratio() >= similarity_threshold

def find_similar_texts(dataframe, text_column, similarity_threshold=0.95):
    """
    Finds similar texts in a dataframe and assigns unique IDs to clusters of similar texts.

    Parameters:
    - dataframe (pd.DataFrame): The input dataframe containing a column named 'text_column'.
    - text_column (str): The name of the dataframe column to be considered for similarity calculation.
    - similarity_threshold (float): The threshold for considering texts as similar. Default is 0.95.

    Returns:
    - pd.DataFrame: Updated DataFrame with an additional 'ID' column.
    - pd.DataFrame: Count of unique and repeated items.
    """
    id_counter = 1
    id_dict = {}

    for i, (index, row) in enumerate(dataframe.iterrows()):
        if index not in id_dict:
            found_similar = False
            for j, (comp_index, comp_row) in enumerate(dataframe.iterrows()):
                if index != comp_index and comp_index not in id_dict:
                    sim = text_similarity(row[text_column], comp_row[text_column], similarity_threshold)
                    if sim:
                        if index not in id_dict:
                            id_dict[index] = id_counter
                            id_counter += 1
                        id_dict[comp_index] = id_dict[index]
                        found_similar = True

            if not found_similar and index not in id_dict:
                id_dict[index] = id_counter
                id_counter += 1

    dataframe['ID'] = dataframe.index.map(id_dict)

    # Count unique and repeated items
    unique_counts = dataframe['ID'].value_counts().reset_index()
    unique_counts.columns = ['ID', 'Quantity']

    return dataframe, unique_counts

# Example of usage
if __name__ == "__main__":



    # Creating a sample dataframe
    data = {
        'text': [
            'Hello, how are you?',
            'Hello, how are u?',
            'My name is Ergon',
            'My name isss Ergon',
            'This is a test.',
            'This is a test!',
            'Is this a test?',
            'Python is incredible',
            'My names Ergon!',
            'Greetings from across the globe!',
            'Howdy, feeling alright?',
            'How? feeling alright?',
            'This is merely a trial.',
            'This serves as an illustration.',
            'Python programming is astounding.',
            'Coding in Python is extraordinary.',
            'I m Ergon, nice metya.',
            'I m Ergon, nice to mt you',
            'Let me introduce myself, Ergon here.',
            'Just checking if the test is working.',
            'Just checking if the test is working.',
            'Just checking if the test is working!',
            'RU just checking if the test is working?',
            'Ergon is what I answer to.',
            'Hola, ¿cómo estás?',
            'Hola, cómo estás?',
            'Todo bien por aquí.',
            'Mi nombre es Ergon.',
            'Mi nombre es Ergon!',
            'Python es increíble.',
            'Hi, how are you?',
            'Hey, how are you?',
            'My name is Ergón',
            'This is just a test.',
            'This is just a   test.',
            'I am Ergón.',
            'Hola, ¿cómo va?',
            'Todo bien por acá.',
            'Mi nombre es   Ergon.',
            'Esto es  una prueba.'
        ]
    }
    
    
    
    df = pd.DataFrame(data)

    # Set the desired similarity threshold (e.g., 0.95)
    similarity_threshold = 0.8

    # Specify the desired text column
    text_column = 'text'

    # Find similar texts and IDs
    df, unique_counts = find_similar_texts(df, text_column, similarity_threshold)

    # Display the updated dataframe
    print("Updated DataFrame:")
    display(df)

    # Display the count dataframe
    print("\nCount of Unique and Repeated Items (in descending order):")
    display(unique_counts)
