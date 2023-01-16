/*Author: Solai*/

int rightmostSetBitPos(int num)
{
    /*return value 1 if num is odd*/
    if(num & 1)
    {
        return 1;
    }

    /*for even num*/
    /*extract the rightmost bit alone from num
        step1. AND operation of num and num-1 will unset rightmost bit
            while keeping other set bits intact.
        step2. XOR operation of step1 result with num will yield result
            with rightmost bit set which is desired output*/
    int n = (num & (num-1)) ^ num;

    int rb_pos = 0;
    /*rightshift n by 1 each time and count that to know position of
    rightmost bit in num*/
    while(n)
    {
        n >>= 1;
        ++rb_pos;
    }

    return rb_pos;
}
