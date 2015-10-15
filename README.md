<h2> Supports: </h2>

**Python**:Python 2.6+

**Author**: dw.livion@yandex.ru


<h2>  Install: </h2> 


<syntaxhighlight lang=bash>

    $ pip install pygraf
</syntaxhighlight>
or

<syntaxhighlight lang=bash>

    $ pip3 install pygraf
</syntaxhighlight>

<h2>  Command List: </h2> 

*graph=pygraf.graf(n,mas)     
*graph.check_orient()
*graph.dfs(v,0)
*graph.print_dfs()
*graph.comp(True/False)
*graph.minwayves_wihtout_cicly(v,u)
*graph.minwayprint_wihtout_cicly(v,u)
*graph.add_rebro(v,u,c)
*graph.del_rebro(v,u)


<h2>  pygraf.graf(n,mas) </h2> 

1. n - count of point
2. mas - massive of [First point,Second point,Cost]

Example init graph:

<syntaxhighlight lang=c>

   graph=pygraf.graf(3,[[1,2,2],[1,3,4]])

</syntaxhighlight>

<h2>  graph.check_orient() </h2> 

Checking directed graph

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[1,3,4]])
   graph.check_orient()#return true - Directed; False - Undirected
</syntaxhighlight>

<h2>  graph.dfs(v,0) </h2> 

Starting DFS algoritm from v-point

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.dfs(2,0)#Nothing return
</syntaxhighlight>

<h2>  graph.print_dfs() </h2> 

Return result DFS algoritm from v-point

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.dfs(2,0)#Nothing return
   print(graph.print_dfs())#print [False,True,True]
</syntaxhighlight>

<h2>  graph.comp(True/False) </h2>

Only for Undirected graph, if graph directed return False

if True:

Return Connected component and List all component:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2]])
   print(graph.comp(True))#print "1->2" "1->3" "1"
</syntaxhighlight>
if False:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2]])
   print(graph.comp(False))#print "1"
</syntaxhighlight>

<h2>  graph.minwayves_wihtout_cicly(v,u) </h2> 

Print min-cost from v to u

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.minwayves_wihtout_cicly(2,3)#print "4"
</syntaxhighlight>

<h2>  graph.minwayprint_wihtout_cicly(v,u) </h2> 

Print min-cost from v to u

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.minwayprint_wihtout_cicly(2,3)#print "2 3"
</syntaxhighlight>

<h2>  graph.add_rebro(v,u,c) </h2> 

Add path from "v" to "u" cost "c"

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.add_rebro(2,1,4)#add path from 2 to 1 cost 4
</syntaxhighlight>

<h2>  graph.del_rebro(v,u) </h2> 

Delete path from "v" to "u"

Example init graph:

<syntaxhighlight lang=c>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.del_rebro(1,2)#delete path from «1» to «2»
</syntaxhighlight>
