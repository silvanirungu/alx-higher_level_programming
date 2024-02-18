#include "lists.h"
<<<<<<< HEAD

/**
 * check_cycle - check if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
**/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

=======
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
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
	return (0);
}
