using System;

namespace TwoSum
{
    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {

            for (int i = 0; i < nums.Length - 1; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {

                    if (nums[i] + nums[j] == target)
                        return new int[] { i, j };
                }
            }
            return new int[] { 0, 0 };

            //var sortNums = new int[nums.Length];
            //Array.Copy(nums,sortNums,nums.Length);

            //Array.Sort(sortNums);

            //int i = 0;
            //int j = nums.Length-1;
            //int i1, i2;

            //while (i < j)
            //{
            //    if (sortNums[i] + sortNums[j] == target)
            //    {
            //        i1 = Array.IndexOf(nums, sortNums[i]);

            //        if (sortNums[i] == sortNums[j])
            //           i2 = Array.IndexOf(nums, sortNums[j], i1+1);
            //        else 
            //            i2 = Array.IndexOf(nums, sortNums[j], i1);
            //        return new int[2] { i1, i2 };
            //    }
            //    else if (sortNums[i] + sortNums[j] > target)
            //        j--;
            //    else
            //        i++;
            //}

        }

        static void Main(string[] args)
        {
            Solution s = new Solution();
            int[] val = { -1, -2, -3, -4, -5 };
            s.TwoSum(val, -8);
        }

    }

}
