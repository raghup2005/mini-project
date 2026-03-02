import random
def main():
    num=random.randint(1,100)
    attempts=0
    max_attempts=4
    points=0
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
            if attempts==1:
                points+=10
                print(f"you got {points}points")
            return
        print(f"attempts left:{max_attempts-attempts}")
    print(f"game over! the number is {num}")
if __name__ == "__main__":
    main()
