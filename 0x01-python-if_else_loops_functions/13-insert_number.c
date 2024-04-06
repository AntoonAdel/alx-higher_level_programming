#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: value in singly linked list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp1 = *head, *temp2;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!temp1 || temp1->n >= number)
	{
		new_node->next = temp1, *head = new_node;
		return (new_node);
	}

	temp2 = temp1->next;
	while (temp1 && temp2 && (temp2->n < number))
		temp1 = temp1->next, temp2 = temp1->next;

	temp1->next = new_node, new_node->next = temp2;
	return (new_node);
}