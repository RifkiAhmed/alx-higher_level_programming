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
	listint_t *current;

	current = list;
	while (current->next)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
