


using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;

public class Solution
{
    public bool IsPalindrome(int x)
    {
        string sX = x.ToString();
        int i = 0;
        int j = sX.Length - 1;

        while (i < j)
        { 
            if (sX[i] != sX[j])
                return false;

            i++;
            j--;
        }

        return true;
    }


    // Number 6. ZigZag Conversion
    public string Convert(string s, int numRows)
    {
        bool isDown = false;
        int sLen = s.Length;
        int row;

        List<string> list = new List<string>();

        for(int i = 0; i< numRows && i < sLen; i++ )
        {
            list.Add(s[i].ToString());
        }


        int iter = list.Count;
        row = iter-1;

        while (iter < sLen)
        {

            if (row == 0)
            {
                isDown = true;
            }
            else if (row >= numRows-1)
            {
                isDown = false;
            }

            if (numRows > 1)
            {
                if (isDown )
                {
                    row++;  
                }
                else
                {
                    row--;

                }
            }
            list[row] += s[iter].ToString();


            iter++;
        }

        string result = "";
        for (int i = 0; i < list.Count; i++ )
        {
            result += list[i].ToString();
        }
        return result;
    }


    public bool IsPal(string s)
    {
        int i = 0;
        int j = s.Length - 1;

        while (i < j)
        { 
            if (s[i] != s[j])
                return false;

            i++;
            j--;
        }

        return true;
    }

    public string LongestPalindrome(string s)
    {
        int j=0;
        string lPal = "";

        if (s.Length < 2)
        {
            return s;
        }

        for (int i = 0; i < s.Length - 1; i++)
        {
            bool cont = true;
            j=s.Length - 1;
            while (i < j && cont && (j-i >= lPal.Length))
            {
                if (IsPal(s.Substring(i, j- (i-1))))
                {
                    if (lPal.Length < j)
                    {
                        lPal = s.Substring(i, j-(i-1));
                    }
                    cont = false;
                }
                j--;
            }
        }
        if (lPal.Length == 0)
        {
            return s[0].ToString();
        }

        return lPal;
    }

    static void Main()
    { 
        
        Solution s = new Solution();
        //var val = s.IsPalindrome(111);
        //var val = s.Convert("AB", 1);
        var val = s.LongestPalindrome("aacabdffffffkacaa");
        
        Console.WriteLine(val);
    }
}
