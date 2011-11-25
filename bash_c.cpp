#if 0
gcc -o /tmp/bash_cpp $0
echo "Compiled bash_cpp"
exec /tmp/bash_cpp
#endif

#include <stdio.h>
int main() {
    printf("Hello world!\n");
}
