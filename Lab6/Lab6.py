import numpy as np
import matplotlib.pyplot as plt 
import networkx as nx 
import os
import random

def nodes(data_file = None):
	"""
	Reads in a data file and plots it accordingly (plots node connections)

	Parameters
	----------
		data_file (str) 	: The data file you would like to read in

	Returns
	-------
		Nothing, but plots the data
	"""

	# Start doing this
	if data_file == None: # Check if there is an input file, and do something
		file = "contiguous-usa.dat" # If there isn't we're doing autofind, so hardcode the expected path
		if not os.path.exists(file): # Check if the path exists, if not return
			print("\n\tCannot auto-find file, [ continguous-usa.dat ] is not in the current working directory!\n\t")
			return
	else:
		file = data_file # locally save the file like before
		if not os.path.exists(file): # Check if it exists
			print("\n\tCannot auto-find file, [ " + data_file + " ] - It could not be found!\n\t")
			return
	
	# Open the file to read
	open_file = open(file, "r")

	# Read in the lines of the file into an array
	lines_in_file = open_file.readlines()
	open_file.close() # Close the file, since we are done with it
	
	# Take the contents of the file and convert them into a dictionary
	keys = [] # Get the keys
	vals = [] # Get the vals

	for i in range(len(lines_in_file)): # iterate through the entire thang
		lines_in_file[i] = lines_in_file[i].replace("\n", "") # Remove the "\n" 
		_key, _val = lines_in_file[i].split() # Split the string, so you get the two strings separated by a space
		keys.append(_key)
		vals.append(_val)

	# Create a NetworX graph and plot the sucker
	Graph = nx.Graph() # Make the newtworkX graph
	for i in range(len(keys)): # For each key in the dictionary
		Graph.add_node(keys[i]) # Make a node for the key
		Graph.add_edge(keys[i], vals[i]) # Make an edge for the key
	
	Graph_layout = nx.spring_layout(Graph)
	# Draw the graph and show it
	nx.draw(Graph, pos=Graph_layout, with_labels=True) # Draw the graph
	plt.show()
	
def plot_paths(G, node_from, node_to):
	"""
	Takes a Graph, and a start and end point, and finds the shortest path between them

	Parameters
	----------
		G (nx.Graph) 	: The already made nx.Graph object
		node_from (str) : A starting node
		node_to (str)	: An ending node

	Returns
	-------
		Nothing, but plots the data
	"""
	# Quite literally doing a bit of trolling

	# Start by calling the NetworkX function
	DJ = nx.shortest_path(G, source=node_from, target=node_to, method="dijkstra") # gets the shortest path between to nodes on a graph using dijkstra's method
	A_ster = nx.astar_path(G, source=node_from, target=node_to) # Finds the path between the inputted nodes using the A* method

	G_layout = nx.spring_layout(G) # Create a specific layout for the data (spring_layout I guess since I like how it looks)
	nx.draw(G, pos=G_layout, with_labels=True) # Draw the preliminary graph

	# Code found from https://stackoverflow.com/questions/24024411/highlighting-the-shortest-path-in-a-networkx-graph, since no test case
	DJ_edges = list(zip(DJ,DJ[1:])) # Get a list of tuples from the shortest path we found
	plt.figure() # Create a new figure
	nx.draw(G, pos=G_layout, with_labels=True) # Draw the graph
	nx.draw_networkx_nodes(G, pos=G_layout, nodelist=DJ,node_color='r') # highlight the nodes that are on the shortest path
	nx.draw_networkx_edges(G, pos=G_layout, edgelist=DJ_edges,edge_color='r',width=5) # highlight the edges between the nodes on the shortest path
	plt.show() # Show it all 

def weights(data_file=None):
	"""
	Reads in a data file and plots it accordingly (plots node connections)

	Parameters
	----------
		data_file (str) 	: The data file you would like to read in

	Returns
	-------
		Nothing, creates a new file (contiguous-usa.dat) and plots a weighted graph
	"""
	# Start doing this
	if data_file == None: # Check if there is an input file, and do something
		file = "contiguous-usa.dat" # If there isn't we're doing autofind, so hardcode the expected path
		if not os.path.exists(file): # Check if the path exists, if not return
			print("\n\tCannot auto-find file, [ continguous-usa.dat ] is not in the current working directory!\n\t")
			return
	else:
		file = data_file # locally save the file like before
		if not os.path.exists(file): # Check if it exists
			print("\n\tCannot auto-find file, [ " + data_file + " ] - It could not be found!\n\t")
			return
	
	read_file = open(file, "r") # Read in the input file
	read_file_lines = read_file.readlines() # Get a list containing all of the lines in the file
	for i in range(len(read_file_lines)): # for each line in the file, replace the \n character
		read_file_lines[i] = read_file_lines[i].replace("\n", "")

	# Create the new file
	write_file = open("contiguous-usa_redux.dat", "w") # create the new file
	for line in read_file_lines: # write our new lines to the file, which is the previous lines + a random number
		write_file.write(line + " " + str(float(random.randrange(0, 100)/100)) + "\n")

	# Close both files
	read_file.close()
	write_file.close()
	write_file_open = open("contiguous-usa_redux.dat", "r") # OPen back up the file we just made
	lines_in_file = write_file_open.readlines() # Read the lines

	# Take the contents of the file and convert them into a dictionary
	keys = [] # Get the keys
	vals = [] # Get the vals
	weights = [] # Get the weights
	for i in range(len(lines_in_file)): # iterate through the entire thang
		lines_in_file[i] = lines_in_file[i].replace("\n", "") # Remove the "\n" 
		_key, _val, weight = lines_in_file[i].split() # Split the string, so you get the two strings separated by a space
		weights.append(float(weight)) # Add weight to list
		keys.append(_key) # Add key to list
		vals.append(_val) # Add value to list
	
	# Create a NetworX graph and plot the sucker
	Graph = nx.Graph() # Make the newtworkX graph
	for i in range(len(keys)): # For each key in the dictionary
		Graph.add_node(keys[i]) # Make a node for the key
		Graph.add_edge(keys[i], vals[i], weight=weights[i]) # Make an edge for the key
	Graph_layout = nx.spring_layout(Graph) # Create a graph layout with the newly plotted information (Using planar cause it looks alright)

	# Create pretty edges - SOURCE: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
	elarge = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] > 0.5] # Create a large edge to use with large weights
	esmall = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] <= 0.5] # Create a smalll edge to use for smaller weights
	nx.draw_networkx_edges(Graph, Graph_layout, edgelist=elarge, width=6) # Draw the said large edge (no color)
	nx.draw_networkx_edges(Graph, Graph_layout, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed") # Draw the said small edge
	edge_labels = nx.get_edge_attributes(Graph, "weight") # Get the weights to plot

	# Draw the graph and show it
	nx.draw(Graph, pos=Graph_layout, with_labels=True) # Draw the graph
	nx.draw_networkx_edge_labels(Graph, Graph_layout, edge_labels=edge_labels) # Draw the weights and such
	plt.show() # Plot the sucker

def oregon_trail(weighted_states=None):
	"""
	Play the classic "Oregon Trail" game, but downsized! You're goal is to get to your destination in the most optimized way possible

	Parameters
	----------
		weighted_states	: The filepath to the contiguous-usa file

	Returns
	-------
		also nada
	"""
	print("\t\t-- [ OREGON TRAIL - THE GAME (but worse) ] -- \n\n\twelcome to the Oregon trail! This is a path optimization game\n\tmeant to test the features of NetworkX, the dijkstra path finding\n\talgorithm, and your skills at surviving the wild wild west!\n\t\t\tHappy caravaning! ")
	print("\n\tHOW TO PLAY:\n\t\tFirst, start by selecting your starting state and your ending state\n\n\t\tThen, select the state you'd like to travel to first (from your starting state)\n\t\tKeep traveling to different states until you reach your goal!\n\n\t\tIf you took the shortest and easiest path (of which, there could be many)\n\t\tyou win! If you take the scenic route, your're out buster\n\n\t\tThe goal is to get to your destination using the best route (determined by RNG weights)\n\t\t\tGood Luck!! (To see this at any time, enter '-h', to exit, enter 'exit') ")
	print()
	print()

	# Start doing this
	if weighted_states == None: # Check if there is an input file, and do something
		file = "contiguous-usa_redux.dat" # If there isn't we're doing autofind, so hardcode the expected path
		if not os.path.exists(file): # Check if the path exists, if not return
			print("\n\tCannot auto-find file, [ continguous-usa.dat ] is not in the current working directory!\n\t")
			return
	else:
		file = weighted_states # locally save the file like before
		if not os.path.exists(file): # Check if it exists
			print("\n\tCannot auto-find file, [ " + weighted_states + " ] - It could not be found!\n\t")
			return

	## Do all of the stuff we did in the weights() function again 
	read_file = open(file, "r") # OPen back up the file we just made
	lines_in_file = read_file.readlines() # Read the lines

	# Take the contents of the file and convert them into a dictionary
	keys = [] # Get the keys
	vals = [] # Get the vals
	weights = [] # Get the weights
	for i in range(len(lines_in_file)): # iterate through the entire thang
		lines_in_file[i] = lines_in_file[i].replace("\n", "") # Remove the "\n" 
		_key, _val, weight = lines_in_file[i].split() # Split the string, so you get the two strings separated by a space
		weights.append(float(weight)) # Add weight to list
		keys.append(_key) # Add key to list
		vals.append(_val) # Add value to list
	
	# Create a NetworX graph and plot the sucker
	Graph = nx.Graph() # Make the newtworkX graph
	for i in range(len(keys)): # For each key in the dictionary
		Graph.add_node(keys[i]) # Make a node for the key
		Graph.add_edge(keys[i], vals[i], weight=weights[i]) # Make an edge for the key
	Graph_layout = nx.spring_layout(Graph) # Create a graph layout with the newly plotted information (Using planar cause it looks alright)

	# Create pretty edges - SOURCE: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
	elarge = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] > 0.5] # Create a large edge to use with large weights
	esmall = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] <= 0.5] # Create a smalll edge to use for smaller weights
	edge_labels = nx.get_edge_attributes(Graph, "weight") # Get the weights to plot

	plt.title("Network of US States")
	nx.draw_networkx_edges(Graph, Graph_layout, edgelist=elarge, width=6) # Draw the said large edge (no color)
	nx.draw_networkx_edges(Graph, Graph_layout, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed") # Draw the said small edge
	nx.draw_networkx_edge_labels(Graph, Graph_layout, edge_labels=edge_labels) # Draw the weights and such
	nx.draw(Graph, pos=Graph_layout, with_labels=True) # Draw the graph

	print("Available states (Please pick a starting location and destination)")
	print(set(keys + vals)) # Display all of the possible starting locations
	looper = True # looping variable
	node1 = "" # Initialize our node variables
	node2 = ""
	while(looper):
		res = input("What state are you starting in?\n\t")
		if res in (set(keys + vals)): # Check if the input is in the set
			print()
			node1 = res # Save it in our node1 variable if it is
			looper = False # Stop looping
		elif res == "exit": # If they want to exit, just exit man
			print("\tThanks for playing!")
			return
		elif res == "-h": # If they need the help statement, reprint it
			print("\t\t-- [ OREGON TRAIL - THE GAME (but worse) ] -- \n\n\twelcome to the Oregon trail! This is a path optimization game\n\tmeant to test the features of NetworkX, the dijkstra path finding\n\talgorithm, and your skills at surviving the wild wild west!\n\t\t\tHappy caravaning! ")
			print("\n\tHOW TO PLAY:\n\t\tFirst, start by selecting your starting state and your ending state\n\n\t\tThen, select the state you'd like to travel to first (from your starting state)\n\t\tKeep traveling to different states until you reach your goal!\n\n\t\tIf you took the shortest and easiest path (of which, there could be many)\n\t\tyou win! If you take the scenic route, your're out buster\n\n\t\tThe goal is to get to your destination using the best route (determined by RNG weights)\n\t\t\tGood Luck!! (To see this at any time, enter '-h', to exit, enter 'exit') ")
			print()
			print()
			print("Available states (Please pick a starting location and destination)")
			print(set(keys + vals))
		elif res not in (set(keys + vals)): # If it's not a valid input, tell them to try again!
			print("You didn't input a valid starting location, please try again!\n")
		
	# Do exactly the same thing as above, but this time we're collecting the ending location. Its EXACTLY the same, I pwomise
	looper = True # Start the looper again
	while(looper): 
		res = input("What is your destination?\n\t")
		if res in (set(keys + vals)):
			print()
			node2 = res
			looper = False
		elif res == "exit":
			print("\tThanks for playing!")
			return
		elif res == "-h":
			print("\t\t-- [ OREGON TRAIL - THE GAME (but worse) ] -- \n\n\twelcome to the Oregon trail! This is a path optimization game\n\tmeant to test the features of NetworkX, the dijkstra path finding\n\talgorithm, and your skills at surviving the wild wild west!\n\t\t\tHappy caravaning! ")
			print("\n\tHOW TO PLAY:\n\t\tFirst, start by selecting your starting state and your ending state\n\n\t\tThen, select the state you'd like to travel to first (from your starting state)\n\t\tKeep traveling to different states until you reach your goal!\n\n\t\tIf you took the shortest and easiest path (of which, there could be many)\n\t\tyou win! If you take the scenic route, your're out buster\n\n\t\tThe goal is to get to your destination using the best route (determined by RNG weights)\n\t\t\tGood Luck!! (To see this at any time, enter '-h', to exit, enter 'exit') ")
			print()
			print()
			print("Available states (Please pick a starting location and destination)")
			print(set(keys + vals))
		elif res not in (set(keys + vals)):
			print("You didn't input a valid starting location, please try again!\n")
	print("Got it, good luck on your journey from " + node1 + " to " + node2 + "!") # Tell them what their responses were
	print("And now, the journey begins... Welcome to " + node1 + "!") # Start the journey

	# Steal the code from plot_paths()
	DJ = nx.shortest_path(Graph, source=node1, target=node2, method="dijkstra") # gets the shortest path between to nodes on a graph using dijkstra's method

	# Code found from https://stackoverflow.com/questions/24024411/highlighting-the-shortest-path-in-a-networkx-graph, since no test case
	DJ_edges = list(zip(DJ,DJ[1:])) # Get a list of tuples from the shortest path we found
	plt.figure() # Create a new figure
	plt.title("Shortest Path To Your Destination")
	nx.draw(Graph, pos=Graph_layout, with_labels=True) # Draw the graph
	nx.draw_networkx_nodes(Graph, pos=Graph_layout, nodelist=DJ,node_color='r') # highlight the nodes that are on the shortest path
	nx.draw_networkx_edges(Graph, pos=Graph_layout, edgelist=DJ_edges,edge_color='r',width=5) # highlight the edges between the nodes on the shortest path

	# Get the total weight of our shortest path
	shortest_path_total_weight = 0 # initialize
	for i in range(0, len(DJ)-1): # For all of the edges along the path
		edge_data = Graph.get_edge_data(DJ[i], DJ[i+1]) # Get the edge data
		shortest_path_total_weight = shortest_path_total_weight + edge_data["weight"] # Sum the weight values

	# Start asking the user where they want to go
	looper = True # Start the looper
	counter = 0 # Create a counter so they can enjoy themselves
	current_node = node1 # locally save our node1
	player_weight = 0 # Ask the player for their weight... I mean uhhh get the edge weight of the player path (initialize)
	player_path = [] # List to store the players path
	player_path.append(current_node) # Add the first node

	# Quick check to see if we even should move
	if node1 == node2:
		looper = False # Skip everything lol
	
	# Start prompting
	while(looper):
		print("\nNumber of states travelled: " + str(counter))
		if counter > 0:
			print("Welcome to " + current_node + "!") # If we've traveled beyond our starting point state, give em a little welcome
		print("States nearby that you can travel to:")
		print("\t" + str(list(Graph.neighbors(current_node)))) # Display the neighbors of the current node that we're on
		res = input("What state would you like to travel to next? ")
		if res in list(Graph.neighbors(current_node)): # Check if the input is one of the neighbors of the current node we're on
			print("Moving to " + res) # If so, "move" to it
			edge_data = Graph.get_edge_data(current_node, res) # Get the edge data
			player_weight = player_weight + edge_data["weight"] # sum the weights
			current_node = res # get our new current node
			player_path.append(current_node) # add it to the path
			if current_node == node2: # If our current node is our desination, we're there
				looper = False
			counter = counter + 1 # count up 
		elif res == "exit": # Exit case
			print("\tThanks for playing!")
			return
		elif res == "-h": # Help case
			print("\t\t-- [ OREGON TRAIL - THE GAME (but worse) ] -- \n\n\twelcome to the Oregon trail! This is a path optimization game\n\tmeant to test the features of NetworkX, the dijkstra path finding\n\talgorithm, and your skills at surviving the wild wild west!\n\t\t\tHappy caravaning! ")
			print("\n\tHOW TO PLAY:\n\t\tFirst, start by selecting your starting state and your ending state\n\n\t\tThen, select the state you'd like to travel to first (from your starting state)\n\t\tKeep traveling to different states until you reach your goal!\n\n\t\tIf you took the shortest and easiest path (of which, there could be many)\n\t\tyou win! If you take the scenic route, your're out buster\n\n\t\tThe goal is to get to your destination using the best route (determined by RNG weights)\n\t\t\tGood Luck!! (To see this at any time, enter '-h', to exit, enter 'exit') ")
			print()
			print()
		elif res not in list(Graph.neighbors(current_node)): # Bad input case
			print("You didn't input a valid location, please try again!\n")

	# Print out the player stats, now that they've made it
	print("\n\tYou've made it to your destination! Welcome to " + node2 + "!\n")
	print("\t\t-- PLAYER STATS --")
	print("\tYou traveled through " + str(counter) + " states, nice!")
	print("\tThe path you took was:")
	print("\t" + str(player_path))
	print("\tThe total weight of your route was: " + str(player_weight))
	print("\tThe shortest path possible was:")
	print("\t" + str(DJ))
	print("\tThe weight of the shortest path was: " + str(shortest_path_total_weight))

	if player_weight <= shortest_path_total_weight: # If the players weight was less than the shortest path weight, winner winner chicken dinner
		print("\nCongrats, you won! You took the best path to your destination. Remember, the shortest path is not always the best path!\n\n")
	elif player_weight > shortest_path_total_weight: # If not, they LOST
		print("\nYou lost! Better luck next time, the Oregan Trail is a ruthless path. Remeber, the shortest path isn't always the best path!\n\n")
	
	# Create a figure for the players path
	player_edges = list(zip(player_path,player_path[1:])) # Get a list of tuples from the shortest path we found
	plt.figure() # Create a new figure
	plt.title("Your Path To Your Destination")
	nx.draw(Graph, pos=Graph_layout, with_labels=True) # Draw the graph
	nx.draw_networkx_nodes(Graph, pos=Graph_layout, nodelist=player_path,node_color='r') # highlight the nodes that are on the shortest path
	nx.draw_networkx_edges(Graph, pos=Graph_layout, edgelist=player_edges,edge_color='r',width=5) # highlight the edges between the nodes on the shortest path

	plt.show()
	print("\tThanks for playing!\n")
	







def main():
	# nodes()

	# # plot_path() with test case ##
	# g = nx.Graph()
	# g.add_node(1)
	# g.add_node(2)
	# g.add_node(3)
	# g.add_node(4)
	# g.add_node(5)
	# g.add_node(6)
	# g.add_edge(1, 2)
	# g.add_edge(2,3)
	# g.add_edge(3,4)
	# g.add_edge(4,5)
	# g.add_edge(5,6)
	# g.add_edge(1,3)
	# g.add_edge(3,5)
	# g.add_edge(2,4)
	# plot_paths(g, 1, 6)

	# weights()

	oregon_trail()


if __name__ == "__main__":
	main()