__author__ = 'dwliv_000'
#coding:utf-8
import pygraf

#z=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2]])#неориентированный граф
#z=pygraf.graf(3,[[2,1],[2,3],[3,1],[1,3],[3,2]])#ориентированный граф
#t=[] - тест памяти и времени выполнения
#for j in range(2,1000000):
#    t.append([1,j,1])
#z=pygraf.graf(999999,t)
#z=pygraf.graf(8,[[2,1,2],[2,3,1],[3,1,2],[1,3,1],[1,2,5],[4,5,2],[5,4,1],[7,6,6],[6,7,8],[8,4,2]])#неоринетированный
graph=pygraf.graf(5,[[2,1],[2,3],[3,1],[1,3],[1,2],[3,2],[4,5],[5,4]])
print(graph.comp(False))
print(graph.check_orient())
#print(graph.print_dfs())#print [False,True,True]
#print(z.check_orient())#проверяем ориентированность графа  #false - ориентирован #true-неоринтирован
#z.dfs(1,0)
#print(z.comp(True))
#print(z.print_dfs())
#print(z.comp(True))
"""
z.minwayves_wihtout_cicly(2,3)
z.minwayprint_wihtout_cicly(2,3)
z.add_rebro(2,3,5)
z.del_rebro(2,3)
z.add_rebro(2,3,10)
z.minwayves_wihtout_cicly(2,3)
z.minwayprint_wihtout_cicly(2,3)
"""