#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node in order into a sorted linked list
 * @head: pointer to pointer of previous node of the lined list
 * @number: int to be stored in new node
 * Return: address to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL || current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->n > number || current->next->n > number)
				break;
			current = current->next;
		}
		temp = current->next;
		current->next = new;
		new->next = temp;
		return (new);
	}
	return (new);
}
