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
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	if (current->n < number)
	{
		while (current->next->n <= number)
			current = current->next;
		temp = current->next;
		current->next = new;
		new->next = temp;
		return (new);
	}
	if (current->n > number)
	{
		while (current->n >= number)
			current->next = current;
		temp = current->next;
		current->next = new;
		new->next = temp;
		return (new);
	}
	return (new);
}
