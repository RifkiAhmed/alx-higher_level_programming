#include "lists.h"

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

	if (*head == NULL)
		return (1);
	data = malloc(sizeof(int));
	while ((*head)->next != NULL)
	{
		data[len] = (*head)->n;
		len++;
		data = realloc(data, sizeof(int) * len);
		*head = (*head)->next;
	}
	data[len] = (*head)->n;

	if (len % 2 == 0)
	{
		free(data);
		return (0);
	}

	for (i = 0; i <= (len / 2); i++)
	{
		if (data[i] != data[len - i])
		{
			free(data);
			return (0);
		}
	}
	free(data);
	return (1);
}
