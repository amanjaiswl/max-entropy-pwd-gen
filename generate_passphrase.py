import random
from pathlib import Path

# Paths to input files
FILE_PATHS = {
    "animals": "wordlists/animal_pass.txt",
    "fruits": "wordlists/fruit_pass.txt",
    "common": "wordlists/common_words_pass.txt",
    "names": "wordlists/names_pass.txt"
}

def load_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def count_words(phrase):
    return len(phrase.split())

def select_phrases(files, max_words=4):
    remaining = max_words
    selected = []

    # Shuffle the categories to vary order
    keys = list(files.keys())
    random.shuffle(keys)

    for key in keys:
        if remaining == 0:
            break

        options = load_lines(files[key])
        random.shuffle(options)

        for phrase in options:
            word_count = count_words(phrase)
            if word_count <= remaining:
                selected.append((key, phrase))
                remaining -= word_count
                break

    return selected

def build_password(phrases):
    words = []
    for _, phrase in phrases:
        words.extend(phrase.lower().split())
    return ''.join(words)

def main():
    selected_phrases = select_phrases(FILE_PATHS)
    
    print("🔍 Selected phrases:")
    for category, phrase in selected_phrases:
       print(f"  [{category}] {phrase}")

    print("\n🔐 Final password:")
    print(build_password(selected_phrases))

if __name__ == "__main__":
    main()


