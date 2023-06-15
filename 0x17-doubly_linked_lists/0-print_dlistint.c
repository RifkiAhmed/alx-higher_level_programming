#include "lists.h"

/**
 * print_dlistint -  prints all the elements of a dlistint_t list
 * @h: pointer to the  head of doubly linked list
 *
 * Return: Length of linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	dlistint *temp;

	if (h == NULL)
		return (0);
	if (h->next == NULL)
	{
		printf("%d\n", h->n);
		return (1);
	}

	temp = h;
	while (temp)
	{
		printf("%d\n", h->n);
		count++;
		temp = temp->next;
	}
	return (count)
}
