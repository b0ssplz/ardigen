def fizzbuzz(n: int, m: int) -> None:
    """Prints numbers from n to m with FizzBuzz rules."""
    for i in range(n, m + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)


try:
    n, m = int(input().strip()), int(input().strip())
    if not (1 <= n < m <= 10000):
        raise ValueError("Input must be in range from 1 to 10000.")
    fizzbuzz(n, m)
except ValueError as e:
    print(f"Invalid input: {e}")

