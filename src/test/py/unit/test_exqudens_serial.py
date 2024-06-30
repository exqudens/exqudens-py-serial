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
                    f"exqudens.Serial": {'level': logging.getLevelName(logging.DEBUG)},
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

            assert device is not None

            device.set_log_function(self.__cpp_log)
            self.__logger.info(f"version: '{device.is_set_log_function()}'")

            assert device.is_set_log_function()

            port = ""
            ports = device.list_ports()
            for p in ports:
                self.__logger.info(f"p: '{p}'")
                if p["hardware-id"].startswith("USB\\VID_0483&PID_5740"):
                    port = p["port"]
                    break
            self.__logger.info(f"port: '{port}'")

            assert len(port) > 0

            device.open(port=port, timeout_simple=500)
            self.__logger.info(f"device.is_open: '{device.is_open()}'")

            assert device.is_open()

            data_bytes = device.read_bytes(100)
            size = len(data_bytes)
            self.__logger.info(f"size: {size}")

            assert size == 0

            data = "hi test"
            data_bytes = list(data.encode())
            size = device.write_bytes(data_bytes)
            self.__logger.info(f"size: {size}")

            assert size == 7

            data_bytes = device.read_bytes(7)
            data = bytes(data_bytes).decode()
            self.__logger.info(f"data: '{data}'")

            assert data == "HI TEST"

            data_bytes = device.read_bytes(100)
            size = len(data_bytes)
            self.__logger.info(f"size: {size}")

            assert size == 0

            device.close()
            self.__logger.info(f"device.is_open: '{device.is_open()}'")

            assert not device.is_open()
        except Exception as e:
            self.__logger.info(e, exc_info=True)
            raise e

    def __cpp_log(self, file: str, line: int, function: str, id: str, level: int, message: str) -> None:
        try:
            if level == 1:
                logging.getLogger(id).critical(message)
            elif level == 2:
                logging.getLogger(id).error(message)
            elif level == 3:
                logging.getLogger(id).warn(message)
            elif level == 4:
                logging.getLogger(id).info(message)
            elif level == 5:
                logging.getLogger(id).debug(message)
            elif level == 6:
                logging.getLogger(id).info(message)
        except Exception as e:
            self.__logger.info(e, exc_info=True)
            raise e
