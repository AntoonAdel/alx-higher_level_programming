#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Object of python
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

void print_python_list_info(PyObject *p)
{
	long int sizze, alloc_memory, a;
    PyObject *thing;

	sizze = PyList_Size(p);
	alloc_memory = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", sizze);
	printf("[*] Allocated = %ld\n", alloc_memory);

	for (a = 0; a < size; a++)
	{
		thing = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(thing)->tp_name);
	}
}