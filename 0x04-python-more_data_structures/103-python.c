#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int a;
	char *try_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", try_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (a = 0; a <= size && a < 10; a++)
		printf(" %02hhx", try_str[a]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int a;
        PyListObject *list = (PyListObject *)p;
        const char *typ;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (a = 0; a < size; a++)
        {
                typ = (list->ob_item[a])->ob_type->tp_name;
		printf("Element %a: %s\n", a, typ);
                if (!strcmp(typ, "bytes"))
                        print_python_bytes(list->ob_item[a]);
        }
}