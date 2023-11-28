#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of singly linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *ptr_next_list, *ptr_next_next_list;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr_next_list = list->next;
	ptr_next_next_list = list->next->next;

	while (ptr_next_list != NULL && ptr_next_next_list != NULL
		&& ptr_next_next_list->next != NULL)
	{
		if (ptr_next_list == ptr_next_next_list)
			return (1);

		ptr_next_list = ptr_next_list->next;
		ptr_next_next_list = ptr_next_next_list->next->next;
	}

	return (0);
}