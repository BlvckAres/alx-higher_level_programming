#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *base, *ball;

	if (list == NULL || list->next == NULL)
		return (0);

	base = list->next;
	ball = list->next->next;

	while (base && ball && ball->next)
	{
		if (base == ball)
			return (1);

		base = base->next;
		ball = ball->next->next;
	}

	return (0);
}
