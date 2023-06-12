#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_list_info(PyObject *p)
{
	int len = 0, i;

	len = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = \n");

	for (i = 0 ; i < len; i++)
	{
		printf("Element %d: %s\n", i, (char *)*(Py_TYPE(p))->PyType_Type);
	}
}
