import logging
from typing import Callable

from exqudens.pybind.serial import Serial as PyBindSerial


class Serial:
    """
    Serial class.
    """
    __logger = logging.getLogger(".".join([__name__, __qualname__]))
    __pybind_serial = None

    @classmethod
    def set_logger_level(cls, level: int = logging.DEBUG) -> None:
        try:
            cls.__logger.setLevel(level)
        except Exception as e:
            cls.__logger.error(e, exc_info=True)
            raise e

    @classmethod
    def get_logger_name(cls):
        try:
            return cls.__logger.name
        except Exception as e:
            cls.__logger.error(e, exc_info=True)
            raise e

    def __init__(self) -> None:
        try:
            self.__pybind_serial = PyBindSerial()
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def set_log_function(self, function: Callable[[str, int, str, str, int, str], None]) -> None:
        try:
            self.__pybind_serial.set_log_function(function)
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def get_version(self) -> str:
        try:
            return self.__pybind_serial.get_version()
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def list_ports(self) -> list[dict[str, str]]:
        try:
            return self.__pybind_serial.list_ports()
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def open(
        self,
        port: str,
        baud_rate: int = None,
        timeout_inter_byte: int = None,
        timeout_read_constant: int = None,
        timeout_read_multiplier: int = None,
        timeout_write_constant: int = None,
        timeout_write_multiplier: int = None,
        bite_size: int = None,
        parity: int = None,
        stop_bits: int = None,
        flow_control: int = None,
        timeout_simple: int = None
    ) -> None:
        try:
            if timeout_simple is not None:
                self.__pybind_serial.open_with_timeout_simple(
                    port,
                    timeout_simple
                )
            else:
                self.__pybind_serial.open(
                    port,
                    baud_rate if baud_rate is not None else 9600,
                    timeout_inter_byte if timeout_inter_byte is not None else 0,
                    timeout_read_constant if timeout_read_constant is not None else 0,
                    timeout_read_multiplier if timeout_read_multiplier is not None else 0,
                    timeout_write_constant if timeout_write_constant is not None else 0,
                    timeout_write_multiplier if timeout_write_multiplier is not None else 0,
                    bite_size if bite_size is not None else 8,
                    parity if parity is not None else 0,
                    stop_bits if stop_bits is not None else 0,
                    flow_control if flow_control is not None else 0
                )
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def is_open(self) -> bool:
        try:
            return self.__pybind_serial.is_open()
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e

    def close(self) -> None:
        try:
            self.__pybind_serial.close()
        except Exception as e:
            self.__logger.error(e, exc_info=True)
            raise e


Serial.set_logger_level(logging.INFO)
