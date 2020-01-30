#include <iostream>

using namespace std;

int factorial(int num)
{
    if (num == 1){
        return num;
    }
    else
    {
        return num * factorial(num-1);
    }
}

int main()
{
    cout<<"factorial of 5 is ="<<factorial(5);

    return 0;
}
