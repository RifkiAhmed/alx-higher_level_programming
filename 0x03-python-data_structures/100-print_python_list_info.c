#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - prints some basic info about Python lists
 *@p: pointer to a list object
 *Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int len = 0, i;
	PyListObject *list_ob;

	len = (int)PyList_Size(p);
	list_ob = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int)list_ob->allocated);

	for (i = 0 ; i < len; i++)
	{
		printf("Element %d: %s\n", i, list_ob->ob_item[i]->ob_type->tp_name);
	}
}
