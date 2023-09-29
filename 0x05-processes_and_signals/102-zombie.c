#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */

int main(void)
{

	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}
	while (1)
	{
		sleep(1);
	}
	return (0);
}
