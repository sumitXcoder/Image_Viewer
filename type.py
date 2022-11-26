from random_word import RandomWords
import time
import readchar

# Function to convert seconds to minutes
def sec_to_min(secs):
    m, s = divmod(secs, 60)
    return m + (s / 60)


# Initializing the words using 'random_word' module
def Words():
    r = RandomWords()
    global words
    for i in range(4):
        words += r.get_random_word() + " "
    words += r.get_random_word()
    print(words)


# To calculate the typing speed in words per minute 'WPM'
def wpm():
    global words, errors, begin, end
    return round(((len(words) - errors) / 5) / (sec_to_min(end - begin)))


# Calculating the accuracy
def accuracy():
    global words
    myWord = ""
    errors = 0
    while myWord != words:
        key = readchar.readchar()
        if ord(key) == 127:
            print("\033[1D \033[1D", end="", flush=True)
            myWord = myWord[:-1]
        else:
            if len(myWord) < len(words):
                if key != words[len(myWord)]:
                    errors += 1
                    print("\033[91m", key, "\033[00m", end="", sep="", flush=True)
                else:
                    print(key, end="", flush=True)
            else:
                #printing the key in 'red' color when its an error
                print("\033[91m", key, "\033[00m", end="", sep="", flush=True)
            myWord += key

    acc = (len(words) - errors) / len(words) * 100
    print("\n")
    print("Accuracy : ", round(acc), "%", sep="") if acc >= 0 else print("Accuracy :0%")


errors = 0
words = ""
Words()
begin = time.time()
accuracy()
end = time.time()
print("\nSpeed    : ", wpm(), "wpm\n", sep="")
