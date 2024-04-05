using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] id_list, string[] report, int k) {
        Dictionary<string,List<string>> dic = new Dictionary<string,List<string>>();
        Dictionary<string,int> notion = new Dictionary<string,int>();
        
        for(int i = 0; i < id_list.Length; i++)
        {
            dic.Add(id_list[i], new List<string>());
            notion.Add(id_list[i],0);
        }
            
        
        for(int j = 0; j < report.Length; j++)
        {
            string tempa = report[j].Split(" ")[1];
            string tempb = report[j].Split(" ")[0];
            
            if(dic[tempa].IndexOf(tempb) == -1)
                dic[tempa].Add(tempb);
        }
        
        foreach(string key in dic.Keys)
        {
            if(dic[key].Count >= k) // 밸류에 해당하는 애들이 전부 노션++
            {
                foreach(string val in dic[key])
                    notion[val]++;
            }
                
        }
        
        return notion.Select(x => x.Value).ToArray();
    }
}