#include "Python.h"

void print_ python_list(PyObject *p) {
    if (PyList_Check(p)) {
        int size = PyList_Size(p);
        printf("list type: %s\nsize: %d\n", Py_TYPE(p)->tp_name, size);

        for (int i = 0; i < size; i++) {
            PyObject *item = PyList_GetItem(p, i);
            printf("item[%d]: ", i);
            print_python_object(item);
        }
    } else {
        printf("not a valid list object\n");
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        PyBytesObject *b = (PyBytesObject *)p;
        Py_ssize_t size = PyBytes_GET_SIZE(b);
        printf("bytes type: %s\nsize: %lld\n", Py_TYPE(p)->tp_name, (long long)size);

        char *bytes = PyBytes_AsString(p);
        if (bytes != NULL) {
            printf("first 10 bytes: %.10s\n", bytes);
        } else {
            printf("bytes is NULL\n");
        }
    } else {
        printf("not a valid bytes object\n");
    }
}

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        double value = PyFloat_AS_DOUBLE(p);
        printf("float type: %s\nvalue: %.2f\n", Py_TYPE(p)->tp_name, value);
    } else {
        printf("not a valid float object\n");
    }
}

