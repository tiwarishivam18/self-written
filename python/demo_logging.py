import sys
import logging

demo_logger = logging.getLogger("demo_logger")
demo_logger.setLevel(logging.INFO)
demo_logger.handlers.clear()


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
demo_logger.addHandler(stream_handler)


demo_logger.debug("This is a debug message")
demo_logger.info("This is an info message")
demo_logger.warning("This is a warning message")
demo_logger.error("This is an error message")
