== Supports: ==

**Python**:Python 2.6+

**Author**: dw.livion@yandex.ru


== Install: ==


<syntaxhighlight lang=bash>

    $ pip install pygraf
</syntaxhighlight>
or

<syntaxhighlight lang=bash>

    $ pip3 install pygraf
</syntaxhighlight>

== Command List: ==

*graph=pygraf.graf(n,mas)     
*graph.check_orient()
*graph.dfs(v,0)
*graph.print_dfs()
*graph.comp(True/False)
*graph.minwayves_wihtout_cicly(v,u)
*graph.minwayprint_wihtout_cicly(v,u)
*graph.add_rebro(v,u,c)
*graph.del_rebro(v,u)


== pygraf.graf(n,mas) ==

1. n - count of point
2. mas - massive of [First point,Second point,Cost]

Example init graph:

<syntaxhighlight lang=python>

   graph=pygraf.graf(3,[[1,2,2],[1,3,4]])

</syntaxhighlight>

== graph.check_orient() ==

Checking directed graph

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[1,3,4]])
   graph.check_orient()#return true - Directed; False - Undirected
</syntaxhighlight>

== graph.dfs(v,0) ==

Starting DFS algoritm from v-point

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.dfs(2,0)#Nothing return
</syntaxhighlight>

== graph.print_dfs() ==

Return result DFS algoritm from v-point

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.dfs(2,0)#Nothing return
   print(graph.print_dfs())#print [False,True,True]
</syntaxhighlight>

== graph.comp(True/False) ==

Only for Undirected graph, if graph directed return False

if True:

Return Connected component and List all component:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2]])
   print(graph.comp(True))#print "1->2" "1->3" "1"
</syntaxhighlight>
if False:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2]])
   print(graph.comp(False))#print "1"
</syntaxhighlight>

== graph.minwayves_wihtout_cicly(v,u) ==

Print min-cost from v to u

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.minwayves_wihtout_cicly(2,3)#print "4"
</syntaxhighlight>

== graph.minwayprint_wihtout_cicly(v,u) ==

Print min-cost from v to u

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.minwayprint_wihtout_cicly(2,3)#print "2 3"
</syntaxhighlight>
== graph.add_rebro(v,u,c) ==

Add path from "v" to "u" cost "c"

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.add_rebro(2,1,4)#add path from 2 to 1 cost 4
</syntaxhighlight>
== graph.del_rebro(v,u) ==

Delete path from "v" to "u"

Example init graph:

<syntaxhighlight lang=python>
   graph=pygraf.graf(3,[[1,2,2],[2,3,4]])
   graph.del_rebro(1,2)#delete path from «1» to «2»
</syntaxhighlight>
