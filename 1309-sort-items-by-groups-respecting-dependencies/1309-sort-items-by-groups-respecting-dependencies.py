class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id      
        
        for cur in range(n):
            for prev in beforeItems[cur]:
                item_graph[prev].append(cur)
                item_indegree[cur] += 1
                if group[cur] != group[prev]:
                    group_graph[group[prev]].append(group[cur])
                    group_indegree[group[cur]] += 1      

        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for nei in graph[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        stack.append(nei)
            return visited if len(visited) == len(graph) else []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)
        
        if not item_order or not group_order: 
            return []

        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        res = []
        for group_index in group_order:
            res += ordered_groups[group_index]
        return res