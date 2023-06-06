#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks linked list has a cycle in it or not
 * @list: pointer to linked list
 *
 * Return: 0 if ther is no  cycle, else 1 if thers is
 */
int check_cycle(listint_t *list)
{
	listint_t *node = NULL;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (1);

	if (list->next != NULL)
		node = list->next;
	else
		return (0);
	if (node->next == NULL)
		return (0);
	while (node->next != NULL)
	{
		if (node->next == list)
		{
			free(node);
			node = NULL;
			return (1);
		}
		node = node->next;
	}
	free(node);
	node = NULL;
	return (0);
}
