#include "lists.h"
#include <ctype.h>
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int count = 0;

	while (cur != NULL)
	{
		count += cur->n;
		/*if (isdigit(cur->n))
		{
			count++;
		}*/
		cur = cur->next;
	}
	if (count == 0)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
