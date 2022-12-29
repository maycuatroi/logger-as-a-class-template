import logging

from src.logger.log_message_define import D_COMN_01, D_COMN_02, D_COMN_03


class ZLogger(logging.Logger):
    def __init__(self, name: str = "Zlogger", level: int = logging.NOTSET):
        super().__init__(name, level)

        self.addHandler(logging.StreamHandler())
        # Add cloud logging handler
        self.__add_cloud_logging_handler()

        # Add AWS logging handler
        self.__add_aws_logging_handler()

    def log_elapsed_time(self, process_name: str, elapsed_time: float):
        """
        Log elapsed time for a process.
        Args:
            process_name(str): Name of the process
            elapsed_time(float): Elapsed time in seconds
        """
        self.__do_log(*D_COMN_01, process_name=process_name, elapsed_time=elapsed_time)

    def __do_log(self, code: str, template: str, level: int, **kwargs):
        message = template.format(**kwargs)
        full_message = f"{code}: {message}"
        self.log(level, full_message)
    def log_invalid_result(self, result: str, value: any):
        """
        Log an invalid result.
        Args:
            result(str): Name of the result
            value(any): Value of the result
        """
        self.__do_log(*D_COMN_02, result=result, value=value)

    def log_shape(self, name: str, shape: tuple):
        """
        Log the shape of an object.
        Args:
            name(str): Name of the object
            shape(tuple): Shape of the object
        """
        self.__do_log(*D_COMN_03, name=name, shape=shape)



    def __add_cloud_logging_handler(self):
        """
        Add a handler for logging to a cloud service.
        """

    def __add_aws_logging_handler(self):
        """
        Add a handler for logging to Amazon Web Services (AWS).
        """
