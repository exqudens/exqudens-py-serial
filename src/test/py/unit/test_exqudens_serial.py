import logging.config

from exqudens.serial import Serial


class TestExqudensSerial:
    """
    TestExqudensSerial class.
    """
    __logger = logging.getLogger(".".join([__name__, __qualname__]))

    @classmethod
    def setup_class(cls):
        """
        Setup class.
        """
        try:
            logging.config.dictConfig({
                'version': 1,
                'incremental': True,
                'loggers': {
                    f"{Serial.get_logger_name()}": {'level': logging.getLevelName(logging.DEBUG)},
                    f"{cls.__logger.name}": {'level': logging.getLevelName(logging.INFO)}
                }
            })
        except Exception as e:
            cls.__logger.info(e, exc_info=True)
            raise e

    def test_1(self):
        try:
            device = Serial()
            self.__logger.info(f"version: '{device.get_version()}'")

            ports = device.list_ports()
            for port in ports:
                self.__logger.info(f"port: '{port}'")
        except Exception as e:
            self.__logger.info(e, exc_info=True)
            raise e
