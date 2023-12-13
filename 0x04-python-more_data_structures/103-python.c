#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list - prints some basic info about Python lists
 *
 * @p: Object of python
 *
 * Return: No Return
 */

void print_python_list(PyObject *p)
{
	long int a, size_list, memory;
	PyObject *thing;

	size_list = PyList_Size(p);
	memory = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %ld\n", size_list);
	printf("[*] Allocated = %ld\n", memory);

	for (a = 0; a < size_list; a++)
	{
		thing = PyList_GET_ITEM(p, a);
		printf("Element %ld: %s\n", a, ((thing)->ob_type)->tp_name);
		if (PyBytes_Check(thing))
			print_python_bytes(thing);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 *
 * @p: Object of python
 *
 * Return: No Return
 */
void print_python_bytes(PyObject *p)
{
	long int a, size_bytes;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size_bytes = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size_bytes);
	printf("  trying string: %s\n", string);

	if (size_bytes < 10)
		printf("  first %ld bytes:", size_bytes + 1);
	else
		printf("  first 10 bytes:"), size_bytes = 9;

	for (a = 0; a <= size_bytes; a++)
		if (string[a])
			printf(" %02hhx", string[a]);
		else
			printf(" 00");
	printf("\n");
}
