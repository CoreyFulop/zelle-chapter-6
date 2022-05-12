# old_macdonald.py

def verse_outer():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def verse_unique(animal, noise):
    print(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!")
    print(f"With a {noise}, {noise} here and a {noise}, {noise} there.")
    print(f"Here a {noise}, there a {noise}, everywhere a {noise} {noise}.")

def sing_song(animal, noise):
    verse_outer()
    verse_unique(animal, noise)
    verse_outer()

animals = ["cow", "dog", "sheep", "cat", "mouse"]
noises = ["moo", "bark", "baa", "meow", "squeak"]

def main():
    for i in range(len(animals)):
        sing_song(animals[i], noises[i])
        print()

main()