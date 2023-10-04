#include "lists.h"
/**
 * check_cycle - check if there is a cycle in a list
 * @list: pointer to linked list
 * Return: 1 if it is a list else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list, *tort = list;

	while( hare != NULL && tort != NULL)
	{
		hare = hare->next->next;
		tort = tort->next;
		if (hare == tort)
		{
			return (1);
		}
	}
	return (0);
}
