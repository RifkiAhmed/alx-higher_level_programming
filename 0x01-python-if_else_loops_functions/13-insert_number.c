#include "lists.h"

/**
 * insert_node - function that inserts number into a sorted singly linked list
 * @head: pointer to a pointer of the start of the list
 * @number: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	while (current->next != NULL)
	{
		if (number >= current->n)
		{
			new->next = current->next;
			current->next = new;
			free(current);
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	free(current);
	return (new);
}
