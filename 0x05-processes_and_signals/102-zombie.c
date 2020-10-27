#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 *
 */
int main()
{
    pid_t pid1, pid2, pid3, pid4, pid5;
    int status;

    while (1)
    {
        pid1 = fork();
        if (pid1 == -1)
        {
            perror("Error:");
            return (1);
        }
        if (pid1 > 0)
        {
            printf("Zombie process created, PID: %u\n", pid1);
            sleep(3);
        }
        else
            exit (0);
        pid2 = fork();
        if (pid2 == -1)
        {
            perror("Error:");
            return (1);
        }if (pid2 > 0)
        {
            printf("Zombie process created, PID: %u\n", pid2);
            sleep(3);
        }
        else
            exit (0);
        pid3 = fork();
        if (pid3 == -1)
        {
            perror("Error:");
            return (1);
        }
        if (pid3 > 0)
        {
            printf("Zombie process created, PID: %u\n", pid3);
            sleep(3);
        }
        else
            exit (0);
        pid4 = fork();
        if (pid4 == -1)
        {
            perror("Error:");
            return (1);
        }
        if (pid4 > 0)
        {
            printf("Zombie process created, PID: %u\n", pid4);
            sleep(3);
        }
        else
            exit (0);
        pid5 = fork();
        if (pid5 == -1)
        {
            perror("Error:");
            return (1);
        }
        if (pid5 > 0)
        {
            printf("Zombie process created, PID: %u\n", pid5);
            sleep(3);
        }
        else
            exit (0);
        infinite_while();
    }
    return (0);
}

/**
 *
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
