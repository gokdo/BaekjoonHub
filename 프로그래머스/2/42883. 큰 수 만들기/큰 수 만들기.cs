using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public string solution(string number, int k) {
        Stack<int> stack = new Stack<int>();
        
        stack.Push(number[0]-'0');

        for(int i = 1; i < number.Length; i++)
        {
            if(k > 0 && stack.Peek() < number[i]-'0')
            {
                while(k>0 &&stack.TryPeek(out int result) && result < number[i]-'0')
                {
                    stack.Pop();
                    k--;
                }
                stack.Push(number[i]-'0');
                
            }
            else
            {
                stack.Push(number[i]-'0');
            }
        }
        
        return new string(stack.Reverse().Take(stack.Count-k).Select(x => (char)(x+'0')).ToArray());
    }
}