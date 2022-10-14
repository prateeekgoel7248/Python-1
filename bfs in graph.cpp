#include<bits/stdc++.h>
void preparelist(unordered_map<int,set<int>>&adjlist,vector<pair<int, int>> &edges){
       for(int i=0;i<edges.size();i++){
       int u=edges[i].first;
       int v=edges[i].second;
       adjlist[u].insert(v);
       adjlist[v].insert(u); 
   }
}
void bfs(unordered_map<int,set<int>>&adjlist, unordered_map<int,bool>&vis
       ,vector<int>&ans,int node)
{
       queue<int>q;
       q.push(node);
       vis[node]=1;
       while(!q.empty()){
           int front=q.front();
           q.pop();
           ans.push_back(front);//store front node in ans
           for(auto i:adjlist[front]){//traverse all neighbour of front node
               if(!vis[i]){
                   q.push(i);
                   vis[i]=1;
               }
           }
       }
}
vector<int> BFS(int vertex, vector<pair<int, int>> edges)
{
   // Write your code here
   unordered_map<int,set<int>>adjlist;
   vector<int>ans;
   unordered_map<int,bool>vis;
   preparelist(adjlist,edges);
   
   //traverse all component of graph
   for(int i=0;i<vertex;i++){
       if(!vis[i])
           bfs(adjlist,vis,ans,i);
   }
   return ans;
}