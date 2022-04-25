# -*- coding: utf-8 -*-
"""
Assignment 1. 

Main model. 

Student no: 201578549
    
"""
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot as plt
import csv
import time
import agentframework
import wolf_framework
import numpy as np
import matplotlib.animation
import requests
import bs4




# Create a figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create some variables 
agents=[]
grass=np.full((300,300),30) # Makes a 300 wide square array of 30's to represent grass cover 

# Creating DEM environment from txt file 
reader = csv.reader(open('DEM.txt',newline=''),quoting=csv.QUOTE_NONNUMERIC)
environment=[]
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)


# Display a menu to choose parameters or use default 
Input='0'
Input=input('Menu: \n To choose starting parameters enter a. \n To use default parameters enter b. \n\n Enter here ==> ')

if Input=='a':
    num_agents=int(input('Enter number of agents: '))
    num_it=int(input('Enter number of iterations: '))
    eat_speed=int(input('Enter speed of eating sheep: '))
    run_speed=int(input('Enter speed of fleeing sheep: '))
    wolf_speed=int(input('Enter wolf speed: '))
    neighbourhood=int(input('Enter neighbourhood sharing range: '))
elif Input=='b':
    print(" Default parameters are: \n   - 150 agents \n   - 100 iterations \n   - Sheep speed is 3 \n   - Wolf speed is 6 \n   - Neighbourhood range is 50 ")
    num_agents=150
    num_it=100
    eat_speed=3
    run_speed=5
    wolf_speed=6
    neighbourhood=50


# Creating wolf as an agent on the environment, with random location
wolf=wolf_framework.wolf(random.randint(0,255),random.randint(0,255),environment,agents)  

# Display a menu to use random data or web scraped data         
Input='0'
Input=input('Menu: \n To use randomly located agents enter a. \n To use web scraped agent locations enter b. \n\n Enter here ==> ')

if Input=='a':
    for i in range(num_agents):
        x=random.randint(0,255)
        y=random.randint(0,255)
        agents.append(agentframework.Agent(i,x, y,environment,agents,grass,wolf))

elif Input=='b':
    print("Only the first 100 points are web scraped. The rest are random.")
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    for i in range(num_agents):
        if i>len(td_xs)-1:
            x=random.randint(0,100)
            y=random.randint(0,100)
        else:
            y = int(td_ys[i].text)
            x = int(td_xs[i].text)
        agents.append(agentframework.Agent(i,x, y,environment,agents,grass,wolf))

  



def update(frames):    
    """
    This function performs all of the iterative movements of the sheep and wolf.

    Parameters
    ----------
    frames : Number of iterations.

    Returns
    -------
    None.

    """
    fig.clear()  
    
# Move the agents around and eat grass 
  
    x=[]
    y=[]      
    for i in range(num_agents):
        if agents[i].status!="Dead":       # If agent is dead they stay at position (1000,1000)
            agents[i].move(eat_speed,run_speed)
            x.append(agents[i].x)
            y.append(agents[i].y)        
            agents[i].eat()
        else:
            agents[i].x=1000
            agents[i].y=1000
        
# Perform sharing 

    # Blank list to add in the share of each agent going to other agents
    total_share=[0]*num_agents 
    for i in range(num_agents):
        # List of shares going from agent[i] to other agents
        agent_share = agents[i].share_with_neighbours(neighbourhood)  
        # Add agent[i]'s contribution to the total list of shares
        total_share=np.add(total_share,agent_share) 
    # Add all sharing contributions to agent's stores 
    for i in range(num_agents):
        agents[i].store=total_share[i]

    
# Wolf hunting initiated   
    wolf.hunt(wolf_speed)
    
# Set axis limits and show environment     
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.imshow(environment)
    
    
    
# Plot agents and wolf with agents coloured according to their status
    for i in range(num_agents):
        if agents[i].status=="Hunted":
            colour="red"
        else:
            colour="white"
        plt.scatter(agents[i].x,agents[i].y,c=colour,s=2)
        #print(agents[i])
        #print(agents[i][0],agents[i][1])
    plt.scatter(wolf.x,wolf.y,c='black')
        

# Display a menu to display the animation or save it as a gif
Input='0'
Input=input('Menu: \n To display the animation using the Tkinter GUI enter a. \n To save the animation as a gif enter b.  \n\n Enter here ==> ')

if Input=='a':
    print(' To run the model again, interrupt the kernel, and run again. ')   
    # Display animation using GUI 
    
    def run():        
        animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_it)
        canvas.draw()
        
    root = tkinter.Tk()
    root.wm_title("Sheep Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    menu = tkinter.Menu(root)
    root.config(menu=menu)
    model_menu = tkinter.Menu(menu)
    menu.add_cascade(label="Model", menu=model_menu)
    model_menu.add_command(label="Run model", command=run) 
    tkinter.mainloop()

elif Input=='b':
    print("\n This may take a couple of minutes.")
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_it)
    animation.save('animation.gif', writer='pillow',fps=5)
    print('\n \n Done! :)')
    
    
