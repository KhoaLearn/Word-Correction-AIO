import streamlit as st

def levenshtein_distance(token1, token2):
    if len(token1) < len(token2):
        return levenshtein_distance(token2, token1)

    # Initialize previous row
    previous_row = range(len(token2) + 1)

    for i, c1 in enumerate(token1):
        current_row = [i + 1]
        for j, c2 in enumerate(token2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def load_vocab(uploaded_file):
    lines = uploaded_file.read().decode('utf-8').splitlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

def main():
    st.title("Word Correction using Levenshtein Distance")
    
    uploaded_file = st.file_uploader("Choose a vocabulary file", type="txt")
    if uploaded_file is not None:
        vocabs = load_vocab(uploaded_file)

        word = st.text_input('Word:')
        if st.button("Compute") and word:
            # Compute Levenshtein distance
            leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
            
            # Sort by distance
            sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
            correct_word = list(sorted_distances.keys())[0]
            st.write('Correct word: ', correct_word)

            col1, col2 = st.columns(2)
            with col1:
                st.write('Vocabulary:')
                st.write(vocabs)
            with col2:
                st.write('Distances:')
                st.write(sorted_distances)
    else:
        st.write("Please upload a vocabulary file to proceed.")

if __name__ == "__main__":
    main()
