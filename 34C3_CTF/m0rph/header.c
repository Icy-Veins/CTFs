#include <sys/mman.h>
#include <stdio.h>

int main() 
{
    void *ptr = mmap(0, 0x1000, 0x7, 0x22, -1, 0);
    printf("%p\n", ptr);
}
