#include <stdio.h>
#include <unistd.h>

/**
 *
 */
int main()
{
	pid_t pid;

	while (1)
	{
		pid = fork();
		if (pid == -1)
		{
			perror("Error:");
			return (1);
		}
		printf("Zombie process created, PID: %u\n", pid);
	}
	return (0);
}
