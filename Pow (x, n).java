class Solution {
    public double myPow(double x, int n) {
    if (n < 0) {
      n = -n;
      x = 1 / x;
    }

    double pow = 1;

    while (n != 0) {
        // for deciding even or odd we use bitwise ops 
        // as we know any binary that is even ends with 0 and odd ends with 1
        //  &  op  of 0,1 -> 0 ; 0,0 -> 0 ; 1,1 -> 1 
      if ((n & 1) != 0) {
        pow *= x;
      }
    //   logical shift op /unsigned right shift
    // this op shift the pattern to the right
    // n = 14 -- 1110 >>>1 = 111 i.e - 7
    //  inShort this op is equivalent to n/2
      x *= x;
      n >>>= 1;
    }

    return pow;
  }
}
