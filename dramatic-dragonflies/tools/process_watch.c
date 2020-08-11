#include <stdio.h>
#include <pty.h>
#include <sys/types.h>
#include <sys/select.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <errno.h>
#include <termios.h>

int max(int a, int b)
{
    return a > b ? a : b;
}

int main(int argc, char **argv)
{
    if (argc <= 1)
    {
        printf("usage: process_watch executable *args\n");
        return 1;
    }
    int master;
    pid_t pid = forkpty(&master, NULL, NULL, NULL);
    if (pid == -1)
    {
        fputs("ERROR: fork failed\n", stderr);
        return 1;
    }
    if (pid == 0)
    {
        //slave
        execvp(argv[1], argv + 1);
    }
    else
    {
        //master
        struct termios settings;
        tcgetattr(0, &settings);
        settings.c_lflag &= ~ICANON;
        settings.c_lflag &= ~ECHO;
        tcsetattr(0, TCSANOW, &settings);
        char u[21];
        sprintf(u, "%020x", pid);

        for (;;)
        {
            fd_set read_set;
            FD_ZERO(&read_set);
            FD_SET(0, &read_set);
            FD_SET(master, &read_set);
            select(max(0, master) + 1, &read_set, NULL, NULL, NULL);
            if (FD_ISSET(0, &read_set))
            {
                char u[128];
                int len = read(0, u, 128);
                write(master, u, len);
            }
            if (FD_ISSET(master, &read_set))
            {
                char u[2048];
                int len = read(master, u, 2048);
                if (len == -1)
                {
                    return 0;
                }
                else
                {
                    write(1, u, len);
                }
            }
        }
    }
}
