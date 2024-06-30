#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/stl/filesystem.h>

#include <exqudens/serial/Serial.hpp>

PYBIND11_MODULE(serial, object) {
    pybind11::class_<exqudens::Serial>(object, "Serial")
        .def(
            pybind11::init()
        )
        .def(
            "get_logger_id",
            &exqudens::Serial::getLoggerId
        )
        .def(
            "set_log_function",
            &exqudens::Serial::setLogFunction
        )
        .def(
            "is_set_log_function",
            &exqudens::Serial::isSetLogFunction
        )
        .def(
            "get_version",
            &exqudens::Serial::getVersion
        )
        .def(
            "list_ports",
            &exqudens::Serial::listPorts
        )
        .def(
            "open",
            pybind11::overload_cast<
                const std::string&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&,
                const unsigned int&
            >(&exqudens::Serial::open)
        )
        .def(
            "open_with_timeout_simple",
            pybind11::overload_cast<
                const std::string&,
                const unsigned int&
            >(&exqudens::Serial::open)
        )
        .def(
            "is_open",
            &exqudens::Serial::isOpen
        )
        .def(
            "close",
            &exqudens::Serial::close
        )
        .def(
            "write_bytes",
            [](exqudens::Serial* self, const std::vector<int>& value) {
                std::vector<unsigned char> bytes(value.begin(), value.end());
                return self->writeBytes(bytes);
            }
        )
        .def(
            "read_bytes",
            [] (exqudens::Serial* self, const size_t &size) {
                std::vector<unsigned char> bytes = self->readBytes(size);
                std::vector<int> result(bytes.begin(), bytes.end());
                return result;
            }
        );
}
