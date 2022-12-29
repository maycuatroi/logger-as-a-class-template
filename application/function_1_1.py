import logging

from src.logger.log_message_define import D_COMN_01
from src.logger.z_logger import ZLogger

# do logic function 1


# sample bassic logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def do_logic_1():
    # do the logic

    # start logging
    code, message_template, level = D_COMN_01
    message_template.format(process_name="process1", elapsed_time=123.45)
    message = f"{code}: {message_template}"
    logger.log(level, f"{code}:{message}")


# end do logic function 1

# sample loger as a class
z_logger = ZLogger()


def do_logic_1():
    # do the logic

    # start logging
    z_logger.log_elapsed_time("process1", 123.45)
