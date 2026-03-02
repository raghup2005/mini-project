import random
def main():
    num=random.randint(1,100)
    attempts=0
    max_attempts=6
    while attempts<max_attempts:
        try:
            guess=int(input("enter a number"))
        except ValueError:
            print("invalid input")
            continue
        attempts+=1
        if guess<num:
            print("low")
        elif guess>num:
            print("high")
        else:
            print(f"correct! guess with in {attempts}")
            return
        print(f"attempts left:{max_attempts-attempts}")
    print(f"game over! the number is {num}")
if __name__ == "__main__":
    main()
