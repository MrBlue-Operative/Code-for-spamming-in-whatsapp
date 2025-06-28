import pyautogui
import random
import keyboard
import time

helping_verbs = [
    "am", "is", "are", "was", "were", "be", "being", "been", "have", "has",
    "had", "do", "does", "did", "will", "would", "shall", "should", "can", "could",
    "may", "might", "must"
]

adjectives = [
    "big", "small", "happy", "sad", "tall", "short", "bright", "dark", "fast", "slow",
    "hot", "cold", "loud", "quiet", "strong", "weak", "beautiful", "ugly", "young", "old",
    "rich", "poor", "kind", "mean", "clean", "dirty", "new", "old", "soft", "hard"
]

nouns = [
    "dog", "cat", "house", "car", "tree", "book", "pen", "chair", "table", "door",
    "window", "school", "teacher", "student", "city", "river", "mountain", "bird", "flower", "sky",
    "road", "friend", "family", "food", "water", "sun", "moon", "star", "cloud", "ball"
]

pronouns = [
    "I", "you", "he", "she", "it", "we", "they", "me", "him", "her",
    "us", "them", "my", "your", "his", "its", "our", "their", "mine", "yours"
]

adverbs = [
    "quickly", "slowly", "happily", "sadly", "loudly", "quietly", "well", "badly", "often", "never",
    "always", "sometimes", "yesterday", "today", "tomorrow", "here", "there", "everywhere", "now", "then"
]

prepositions = [
    "in", "on", "at", "under", "over", "beside", "behind", "in front of", "between", "among",
    "with", "without", "to", "from", "by", "about", "above", "below", "near", "far"
]

conjunctions = [
    "and", "but", "or", "so", "because", "although", "if", "unless", "while", "since"
]

extra_nouns = [
    "apple", "banana", "computer", "phone", "bag", "shoe", "clock", "lamp", "paper", "bottle",
    "street", "park", "beach", "forest", "lake", "hill", "valley", "bridge", "boat", "train"
]

# all word lists
all_words = (
    helping_verbs + adjectives + nouns + pronouns + adverbs + prepositions + conjunctions + extra_nouns
)

time.sleep(5)
sentenceSize = 20
while True:
    paragraph = ""
    for i in range(sentenceSize):

        index = random.randint(0, len(all_words) - 1)
        paragraph += all_words[index]
        paragraph += " "

    pyautogui.write(paragraph)
    pyautogui.press("enter")
    time.sleep(1)
    if keyboard.is_pressed('q'):
        break

print("Program terminated")