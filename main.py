"""this is my main project file."""

import classes

def main():
    print("this is the main function")
    obj = classes.Myclass("Alice")
    print(obj.greet())

if __name__ == "__main__":
    main()