# PYTHON BASIC DAY 10 - LOGGING

# Python’s logging module is a built-in library.
# that allows developers to track events that occur within an application during its runtime.
# Logging is important for software developing, debugging, and running.

import logging

# with logging level INFO i.e. level 20, it will shows messages above 20.
logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("this is the first code for logging")
# after running this file, one log file will get generated.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l:
    if i == 2:
        logging.info(i)
        logging.info(l)
        logging.warning("warning message as the user have found 2 in the list")
# previously we were writing print statement to check the result.
# instead of print statement you can see you result in the log file.

# <python logging level image>

# python logging level hierarchy
# 1. DEBUG - 10
# 2. INFO - 20
# 3. WARNING - 30
# 4. ERROR - 40
# 5. CRITICAL - 50

logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")

# mentioning of logging level will determine whether the message is going to be displayed or not.
# based on the level hierarchy, message are being displayed.
# (check line number 8, at the end logging level is mentioned)
