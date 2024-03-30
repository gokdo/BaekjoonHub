using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;

public class Solution {
    public string solution(string X, string Y) {
        StringBuilder answer = new StringBuilder();
        StringBuilder empty = new StringBuilder();
        
        Dictionary<int,int> dicX = new Dictionary<int,int>();
        Dictionary<int,int> dicY = new Dictionary<int,int>();
        
        for(int i = 0; i <= 9; i++)
        {
            dicX.Add(i,0);
            dicY.Add(i,0);
        }
        
        foreach(char x in X)
        {
            dicX[x-'0'] += 1;
        }
        foreach(char y in Y)
        {
            dicY[y-'0'] += 1;
        }
        
        for(int j = 9; j >= 0; j--)
        {
            int min = Math.Min(dicX[j],dicY[j]);
            char c = (char)(j+'0');
            
            answer.Append(c,min);
        }
        if(answer.Equals(empty)) return "-1";
        else if(answer.Length == Math.Min(dicX[0],dicY[0])) return "0";
        
        return answer.ToString();
    }
}