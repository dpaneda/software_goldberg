#if 0
sleep 1
gcc -o /tmp/bash_cpp $0
echo "Compiled bash_cpp"
exec /tmp/bash_cpp
#endif

#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TOKEN "42"

int main() {
    struct addrinfo hints;
    struct addrinfo *result, *rp;
    int sfd, s;

    sleep(1);

    memset(&hints, 0, sizeof(struct addrinfo));
    hints.ai_family = AF_UNSPEC;    /* Allow IPv4 or IPv6 */
    hints.ai_socktype = SOCK_STREAM; /* Datagram socket */
    hints.ai_flags = 0;
    hints.ai_protocol = 0;          /* Any protocol */

    s = getaddrinfo("localhost", "7777", &hints, &result);

    if (s != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(s));
        exit(EXIT_FAILURE);
    }

    for (rp = result; rp != NULL; rp = rp->ai_next) {
        sfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (sfd == -1)
            continue;

        if (connect(sfd, rp->ai_addr, rp->ai_addrlen) != -1)
            break;

        close(sfd);
    }
 

    if (rp == NULL) {
        fprintf(stderr, "Could not connect\n");
        exit(EXIT_FAILURE);
    }

    freeaddrinfo(result);

    write(sfd, TOKEN, strlen(TOKEN));
    close(sfd);

    printf("Token sent\n");
 }
