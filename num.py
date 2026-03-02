import random
def main():
    num=random.randint(1,100)
    attempts=0
    while True:
        guess=int(input("enter a number"))
        attempts+=1
        if guess<num:
            print("low")
        elif guess>num:
            print("high")
        else:
            print(f"correct! guess with in {attempts}")
            break
if __name__=="_main__":
    main()
