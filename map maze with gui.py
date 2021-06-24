from pywebio.output import *
from pywebio.input import *
from pywebio.session import set_env

set_env(title="Path Finder",auto_scroll_bottom=True)

#dijkstra's algorithm
def solution(graph,src,dest,visited=[],distances={},predecessors={}):
    if src == dest:
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        readable=path[0]
        for index in range(1,len(path)): readable = path[index]+'--->'+readable
        put_html('<center> <b>PATH : </b>%s</center>' % (readable))
        put_html('<center><b>DISTANCE : </b>%s units</center>' % (str(distances[dest])))
        visited.clear()
        distances.clear()
        predecessors.clear()
    else :
        if not visited: 
            distances[src]=0
        
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        
        visited.append(src)
        
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        solution(graph,x,dest,visited,distances,predecessors)
#building gui
def gui():
    graph = {
                'main gate': {"admin block":100},
                'admin block': {"main gate":100, "bio block":39, "junction a":8, "junction g":7, "junction f":17, "mba college":60},
                'mba college': {"admin block":60},
                'decinial block': {'college ground':14, "junction e":5},
                'church': {'junction d':15, 'library':10, 'junction a':10, 'junction g':10},
                'bio block': {'junction b':27, 'admin block':39, 'service gate':33},
                'library': {'junction b':9, 'junction a':22, 'church':10},
                'auditorium': {'junction g':6},
                'canteen': {'junction c':9},
                'service gate': {'bio block':33},
                'boys hostel': {'junction c':12, 'junction b':13},
                'girls hostel': {'junction c':11},
                'college ground': {'decinial block':14, 'junction f':22},

                'junction a': {'library':22, 'church':10, 'admin block':8},
                'junction b': {'boys hostel':13, 'library':9, 'bio block':27},
                'junction c': {'canteen':9, 'girls hostel':11, 'junction d':19, 'boys hostel':12},
                'junction d': {'junction e':8, 'church':15, 'junction c':19},
                'junction e': {'junction d':8, "decinial block":5, "junction g":27},
                'junction f': {"admin block":17,  "junction g":15, "college ground":22},
                'junction g':{'church':10, 'auditorium':6, 'junction e':27, 'junction f':15, 'admin block':7}
            }

    data=input_group('select a location', [
        select('Source', options=graph.keys(), name='source'),
        select('Destination', options=graph.keys(), name='destination')
    ])

    if data['source'] == data['destination']:
        popup('ERROR', 'Source and destination are same!', size=PopupSize.SMALL)
        check()
        quit()

    put_text('\n\n')
    put_table([
        [data['source'], data['destination']]
    ],header=['SOURCE', 'DESTINATION'])
    put_text('Please wait...')

    put_html("Here is your shortest path! Enjoy<i class='far fa-laugh' style='font-size:24px'></i>")

    solution( graph, data['source'], data['destination'])
    check()
    
#try again button   
def check():
    again=radio('Try again',['Yes', 'No'])
    if again == 'Yes':
        gui()
    else:
        return style(put_text('Have a good day!'),'color:green')

if __name__=='__main__':
    put_html("<h1><center>SAHRDAYA PATH FINDER</center></h1>")
    put_image('https://static.wixstatic.com/media/2f31ab_be7a01c97a5c43e3a8e3a08306bd4819~mv2.png/v1/fill/w_653,h_685,al_c,q_90,usm_0.66_1.00_0.01/directedMap.webp').style('width: 75%; max-width: 100%; height: auto; margin-left: auto; display: block; margin-right: auto')

gui()

