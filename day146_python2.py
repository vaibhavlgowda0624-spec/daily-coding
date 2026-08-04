import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

logging.info("Application Started")
logging.warning("Sample Warning")

print("Logs written to app.log")
