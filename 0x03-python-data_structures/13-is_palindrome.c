#include "lists.h"
/**
 * check_if_Palindrome - checks if singly linked list is palindrome
 * @one: pointer to head of singly linked list
 * @two: head of singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int check_if_Palindrome(listint_t **one, listint_t *two)
{
	int result;

	if (two == NULL)
		return (1);

	result = check_if_Palindrome(one, two->next);
	if (result == 0)
		return (0);

	result = (two->n == (*one)->n);

	*one = (*one)->next;

	return (result);
}
/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (check_if_Palindrome(head, *head));
}