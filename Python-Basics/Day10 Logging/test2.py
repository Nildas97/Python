import logging

logging.basicConfig(
    filename="test2.log",
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(name)s %(message)s",
)


def divide(a, b):
    logging.info(f"this number entered by user is {a} and {b}")
    try:
        logging.info("we are into function")
        div = a / b
        logging.info("we have completed a division operation")
        return div
    except Exception as e:
        logging.exception(e)


(divide(3, 4))
# here this program will give an error, ZeroDivisionError.
# in the cloud platform, error like this will not be able to view in the console.
# for this logging the message will come into play.
