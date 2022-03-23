#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle
 * @list: list head
 * Return: 1 if there is a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (list && list->next && temp)
	{
		if (list->next == temp)
			return (1);
		list = list->next;
	}
	return (0);
}
