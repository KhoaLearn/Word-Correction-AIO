# Word-Correction-AIO

Word-Correction-AIO is a simple Streamlit application that uses the Levenshtein distance algorithm to suggest the correct spelling for a given word based on a vocabulary list. This project is intended to help with word correction tasks by providing an easy-to-use web interface.

## Features

- Upload a custom vocabulary file
- Input a word to be corrected
- Compute the **Levenshtein** distance between the input word and each word in the vocabulary
- Suggest the closest correct word
- Display the vocabulary and the computed distances

## Requirements

- Python 3.6 or higher
- Streamlit

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/KhoaLearn/Word-Correction-AIO.git
cd Word-Correction-AIO
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Streamlit application:**

```bash
streamlit run main.py
```

2. **Upload your vocabulary file:**

   The vocabulary file should be a plain text file (`.txt`) with one word per line. For example:

   ```
   apple
   book
   dog
   hello
   never
   please
   random
   sleep
   start
   understand
   ```
3. **Enter a word to be corrected:**

   In the input box provided, type the word you want to correct and click the "Compute" button.
4. **View the results:**

   The application will display the suggested correct word along with the list of vocabulary words and their computed Levenshtein distances.

## Example

1. **Upload a vocabulary file:**
   ![Upload File](screenshots/upload.png)
2. **Enter a word to correct:**
   ![Input Word](screenshots/input.png)
3. **View the correction and distances:**
   ![Results](screenshots/results.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [me](https://github.com/KhoaLearn)!
