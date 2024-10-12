import csv

# Function to identify missing letters in a word
def identify_word(partial_word, target_word):
    attempts = 0
    completed_word = list(partial_word)

    # Iterate over the characters in the partial word
    for i, char in enumerate(partial_word):
        if char == '*':
            attempts += 1  # Each '*' counts as an attempt
            completed_word[i] = target_word[i]  # Replace '*' with the corresponding letter

    return ''.join(completed_word), attempts


# Function to process the CSV file and count total attempts
def process_csv(file_path):
    total_attempts = 0

    # Open and read the CSV file
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        # Process each row in the CSV file
        for row in reader:
            game_code, partial_word, target_word = row  # Read game code, partial word, and target word
            completed_word, attempts = identify_word(partial_word, target_word)  # Identify the word

            # Add attempts for this word to the total attempts count
            total_attempts += attempts

            print(f"Game {game_code}: {partial_word} -> {completed_word} (Attempts: {attempts})")

    print(f"\nTotal attempts: {total_attempts}")

    # Check if the total number of attempts is under 1200
    if total_attempts < 1200:
        print("Success: Total attempts are under 1200!")
    else:
        print("Failure: Total attempts exceeded 1200.")


if __name__ == "__main__":
    # Path to the CSV file
    file_path = 'cuvinte_de_verificat.txt'
    process_csv(file_path)
