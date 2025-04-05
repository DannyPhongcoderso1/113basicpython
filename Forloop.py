from random import Random

#cau 1:
for i in range(1,11):
    print(i)
    
#cau 2:
def sum(n):
    sumN = 0
    for i in range(1,n+1):
        sumN += i
    return sumN

#cau 3:
def sum(n):
    sumN = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            sumN += i
    return sumN

#cau 4:
def vowels(string):
    vowelsL = [u,e,o,a,i]
    count = 0
    for i in string:
        if i in vowelsL:
            count += 1
    
    return count

#cau 5:
def count_words(string):
    listW = string.split()
    
    return len(listW)

#cau 6:
def guess_game():
    number = Random.randint(1,100)
    for i in range(5):
        numberGuess = int(input("nhap so ban doan: "))
        if numberGuess == number:
            print(f"ban doan dung sau {i+1} lan")
            break
        else:
            if numberGuess < number:
                print("so ban doan nho hon")
            else:
                print("so ban doan lon hon ")
    
    