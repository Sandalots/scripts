#include <stdio.h>
#include <stdlib.h>

// write me fast inverse square root 
float fisr(float x) {
    float xhalf = 0.5f * x;
    int i = *(int*)&x;
    i = 0x5f3759df - (i >> 1);
    x = *(float*)&i;
    x = x * (1.5f - xhalf * x * x);
    return x;
}


void random_test_fisr() {
    for (int i = 0; i < 10; i++) {
        float x = (float)rand() / RAND_MAX;
        float y = fisr(x);
        printf("fisr(%f) = %f\n", x, y);
    }
}


void test_fisr() {
    float x = 0.15625;
    float y = fisr(x);
    printf("fisr(%f) = %f\n", x, y);
}

int main() {
    random_test_fisr();
    return 0;
}