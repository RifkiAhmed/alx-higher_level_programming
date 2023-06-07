#include "lists.h"

/**
 * insert_node - function that inserts number into a sorted singly linked list
 * @head: pointer to a pointer of the start of the list
 * @number: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = number;
		(*head)->next = NULL;
		return *head;
	}
	current = (*head)->next;
	previous = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	while (current->next != NULL)
	{
		if (number < previous->n)
		{
			new->next = previous;
			*head = new;
			return (*head);
		}
		if (number < current->n && number >= previous->n)
		{
			new->next = current;
			previous->next = new;
			return (new);
		}
		current = current->next;
		previous = previous->next;
	}
	current->next = new;
	return (new);
}
