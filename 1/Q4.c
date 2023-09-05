/*
*   "triangle validator" take three angles of a triangle and
*   print whether the triangle is possible to construct in ℝⁿ
*   basically check if the sum of three inputs is exactly
*   180. 
*/

#include<stdio.h>
#include<math.h>

int
main(void)
{
    double angle1, angle2, angle3;

    printf("Enter the three angles of the triangle.\n");
    scanf("%lf %lf %lf", &angle1, &angle2, &angle3);

    printf("Your triangle is %s\n", (angle1+angle2+angle3 == 180.0) ? "valid" : "invalid since the sum of its angles is not 180");
    return 0;
}