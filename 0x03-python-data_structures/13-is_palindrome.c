#include "lists.h"
#include <limits.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int len = 0, i;
	int *data;
	listint_t *ptr;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	ptr = *head;
	data = malloc(sizeof(int) * 1024);
	while (ptr->next != NULL)
	{
		if (len == 1023)
			data = malloc(sizeof(int) * 1024 * 2);
		data[len] = ptr->n;
		len++;
		ptr = ptr->next;
	}
	data[len] = ptr->n;
	len++;

	for (i = 0; i <= (len / 2); i++)
	{
		if (data[i] != data[len - 1 - i])
		{
			free(data);
			return (0);
		}
	}
	free(data);
	return (1);
}
