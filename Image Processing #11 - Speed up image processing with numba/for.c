#include <stdio.h> // for printf()
#include <sys/time.h> // for clock_gettime()

void loop_func(){
  unsigned long sum = 0;
  for(int x = 0; x < 10000000; x++){
    sum += x;
  }
  printf("SUM[0 ~ 10000000] is %ld\n", sum);
  return;
}

int main() {
    struct timeval start, end;
    long secs_used,micros_used;

    gettimeofday(&start, NULL);
    loop_func();
    gettimeofday(&end, NULL);

    secs_used=(end.tv_sec - start.tv_sec); //avoid overflow by subtracting first
    micros_used= ((secs_used*1000000) + end.tv_usec) - (start.tv_usec);
    float secs_elapsed = micros_used * 1.0 / 1000000;
    printf("micros_used: %ld\n",micros_used);
    printf("sec used: %10.6f\n",secs_elapsed);
    return 0;
}