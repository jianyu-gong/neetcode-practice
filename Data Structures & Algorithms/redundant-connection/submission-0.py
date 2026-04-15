class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        num_of_nodes = len(edges)

        for i in range(1, num_of_nodes + 1):
            par[i] = i
            rank[i] = 1

        def find_parent(x):
            if x != par[x]:
                par[x] = find_parent(par[x])

            return par[x]
        
        # print(par, rank)
        
        for n1, n2 in edges:
            p1, p2 = find_parent(n1), find_parent(n2)

            # print(n1, n2, p1, p2)

            if p1 == p2:
                return [n1, n2]

            else:
                if rank[p1] < rank[p2]:
                    par[p1] = p2

                elif rank[p1] > rank[p2]:
                    par[p2] = p1
                else:
                    par[p1] = p2
                    rank[p2] += 1
            # print(par)
        
        # return edges[-1]

        