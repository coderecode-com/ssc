import logging

# Change Logging Level
# logging.basicConfig(level=logging.DEBUG)

# Change Message Format #1
# logging.basicConfig(format='%(message)s',level=logging.DEBUG)

# Change Message Format #2
# logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Change Message Format #3
# logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
#                     level=logging.DEBUG)

# Change Message Format #4
# logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.DEBUG)

# Change Message Format #5
logging.basicConfig(format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
