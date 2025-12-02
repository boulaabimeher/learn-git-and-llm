from greetings import say_hello
from calculator import add, multiply
from utils import show_title

def main():
    show_title("My Simple Python App")

    say_hello("Ahmed")

    print("Addition: 5 + 3 =", add(5, 3))
    print("Multiplication: 4 * 7 =", multiply(4, 7))

if __name__ == "__main__":
    main()
