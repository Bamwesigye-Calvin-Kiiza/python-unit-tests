def main():
    x = int(input("Enter a value of x: "))
    print('x squared is ', square(x))


def square(number):
    squared = number + number
    return squared


if __name__ == "__main__":
  main() 