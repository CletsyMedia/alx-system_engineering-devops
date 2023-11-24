#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs forever and returns nothing
 * Return: 0 in the end
 */
int infinite_while(void)
{
	while (1)
	{
	sleep(1);
	}
	return (0);
}

/**
 * main - the entry to a program that creates 5 zombie processes
 * Return: 0 on success
 */
int main(void)
{
	int children;
	pid_t pid;

	for (children = 0; children < 5; children++)
	{
	pid = fork();
	if (pid == -1)
	{
	perror("fork");
	exit(1);
	}
	if (pid == 0)
	{
	/* Child process */
	printf("Zombie process created, PID: %i\n", (int)getpid());
	exit(0); /* Each child exits immediately to become a zombie */
	}
	}

	if (pid != 0)
	{
	infinite_while();
	}

	return (0);
}
