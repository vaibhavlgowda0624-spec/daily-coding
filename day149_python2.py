import logging

logging.basicConfig(level=logging.ERROR)

try:
    print(5/0)
except ZeroDivisionError:
    logging.error("Division by zero")
