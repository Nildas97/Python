# importing logging module
import logging

# assigning basic configuration
logging.basicConfig(
    filename="test3.log",
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s %(name)s %(message)s",
)

# using try and except block
# opening a file in read mode
try:
    logging.info("i am trying to read a file")
    with open("nil.txt", "r"):
        logging.info("sucessfully it has read a file")

except Exception as e:
    logging.critical("situation is critical")
    logging.error(e)
