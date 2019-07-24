# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:32:32 2019

@author: ht2531
"""

import math

#Shortest Route

#Find shortest and build up

#Import files
edges_file = open('ttredges.txt', 'r')
vertices_file = open('ttrvertices.txt','r')


#Take in the data from Edges File
edges_original = dict()
edges_reversed = dict()

for line in edges_file:
    key,value = line.strip().split(',')
    if (key in edges_original):
        edges_original[key].append(value)
    else:
        edges_original[key] = [value]
        
    if(value in edges_reversed):
        edges_reversed[value].append(key)
    else:
        edges_reversed[value] = [key]


#Take in the data from the Vertices File
city_vertices = dict()
all_cities = list()

for line in vertices_file:
    key,x,y = line.strip().split(',')
    city_vertices[key] = [x,y]
    all_cities.append(key)
    
def checkEdges(origin_city, destination_city):
    if(origin_city in edges_original and destination_city in edges_original[origin_city]):
        return True
    elif(origin_city in edges_reversed and destination_city in edges_reversed[origin_city]):
        return True
    else:
        return False
        

def findEdgeCities(origin_city):
    edge_cities = list()
    
    for city in all_cities:
        if(checkEdges(origin_city,city)):
            edge_cities.append(city)
            
    return edge_cities

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

    
def findDistanceWithEdgeCities(origin_city):
    edge_cities = findEdgeCities(origin_city)
    
    distance_with_cities = dict()
    
    origin_city_x = int(city_vertices[origin_city][0])
    origin_city_y = int(city_vertices[origin_city][1])
    
    
    for city in edge_cities:
        city_x = int(city_vertices[city][0])
        city_y = int(city_vertices[city][1])
        #print(city_x)
        # Let's round it......
        distance_with_cities[city] = math.floor(distance([city_x,city_y],[origin_city_x,origin_city_y]))
        
    return distance_with_cities

#City to City Distance

city_distance = dict()

for city in all_cities:
    city_distance[city] = findDistanceWithEdgeCities(city)

#Find the best path from Point A to Point B    

def buildPath(origin_vertex):

    sptSet = []
    
    distance_to_vertices = dict()
    
    for vertex in all_cities:
        if(vertex == origin_vertex):
            distance_to_vertices[vertex] = 0
        else:
            distance_to_vertices[vertex] = 100000000000000
        
    while(True):
        minimum = 100000000000000
        for distance in distance_to_vertices.values():
            if distance < minimum:
                minimum = distance
        
        if (sptSet):
            return
        
        break
    
    print(distance_to_vertices)
    
    return


#print(findDistanceWithEdgeCities("Denver"))
#print(city_distance)
buildPath("NewYork","KansasCity")

edges_file.close()



