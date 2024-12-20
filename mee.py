import time
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed tests can improve your skills.",
    "Always practice to become a better programmer.",
    "Learning to code is a valuable skill in today's world."
]

def typing_speed_test():
    print("Welcome to My Applications!!")
    print("\nYou will be given a sentence to type.")
    print("Type it as quickly and accurately as possible.")
    print("Press Enter when you're ready to start!\n")
    input("Press Enter to begin...")
    sentence = random.choice(sentences)
    print("\nType the following sentence:")
    print(f"\"{sentence}\"\n")
    start_time = time.time()
    user_input = input("Your Task: ")
    end_time = time.time()

    # Calculate time taken and words per minute (WPM)
    time_taken = end_time - start_time
    words_count = len(sentence.split())
    words_per_minute = (words_count / time_taken) * 60

    # Check for accuracy
    accuracy = sum(1 for a, b in zip(sentence, user_input) if a == b) / len(sentence) * 100

    print("\n--- Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

    # Feedback
    if accuracy == 100:
        print("Perfect accuracy! Great job!")
    elif accuracy >= 80:
        print("Good accuracy! Keep practicing!")
    else:
        print("Try to improve your accuracy. Practice makes perfect!")

# Run the typing speed test
if __name__ == "__main__":
    typing_speed_test()
