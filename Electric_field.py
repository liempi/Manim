from manim import *
import numpy as np


#Definition of electric charge and their properties in two dimensions (position, color and Q value)

class charge_2D:
    def __init__(self , x_pos, y_pos,Q,color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.Q     = Q
        self.color = color
        
#Scene configuration (Elements, animations)
        
class electric_field_2D(Scene):

    def construct(self):
    
        #Setting the grid
        grid = NumberPlane(color=BLUE , background_line_style = {"stroke_color": WHITE, "stroke_opacity": 0.1})
        
        #Adding axis labels
        grid.add(grid.get_axis_labels())
        
        #Avoid zero division error
        eps = 0.000000001
        
        #vacuum permittivity
        eps_0 = 8.8541878176e{-12}

        #Charge parameters input
        #Color can be PURE_RED(Q>0) or PURE_BLUE(Q<0), you can use other colors
        charge = charge_2D(0,0,-30,PURE_BLUE)
        
        charge_2 = charge_2D(2,2,10,PURE_RED)

        
        #Representation of charges
        dot = Dot(radius=0.05,color=charge.color).shift(RIGHT*charge.x_pos+UP*charge.y_pos)
        
        dot_2 = Dot(radius=0.05,color=charge_2.color).shift(RIGHT*charge_2.x_pos+UP*charge_2.y_pos)


        #Function to calculate the electric field for one charge
        def function(x):
            if (x[0] == charge.x_pos and x[1] == charge.y_pos):
                return [0,0]
            else:
                r = ((x[0]-charge.x_pos)**2 + (x[1]-charge.y_pos)**2)**(3/2)

                vectors = -charge.Q/(4*PI*eps_0) * np.array([(x[0]-charge.x_pos)/r, (x[1]-charge.y_pos)/r])
                return vectors
        
        #Example if you want to graph the electric field for two charges
        def function_2(x):
        #Here I exclude the arrow near to the charges.
            if (x[0] == charge.x_pos and x[1] == charge.y_pos) or (x[0] == charge_2.x_pos and x[1] == charge_2.y_pos):
            
                return [0,0]
        #In any other case we calculate the electric field
            else:
                r = ((x[0]-charge.x_pos)**2 + (x[1]-charge.y_pos)**2)**(3/2)
                
                r_2 = ((x[0]-charge_2.x_pos)**2+(x[1]-charge_2.y_pos)**2)**(3/2)
                
                vectors = charge.Q/(4*PI*eps_0)*np.array([(x[0]-charge.x_pos)/r,\
                (x[1]-charge.y_pos)/r]) +charge_2.Q/(4*PI*eps_0)*np.array([(x[0]-charge_2.x_pos)/r_2,\
                (x[1]-charge_2.y_pos)/r_2])
            
                return vectors
        #If you want to add more elecrric charges, you need to create a new charge and introduce values for position, color and charge.
        #Then,you need to add another condition in if and in else as above. Just compare function with function_2.
 
        #Vector field creation in Manim
        vector_field = ArrowVectorField(function_2,color_scheme=None,\
        color=PURE_BLUE,vector_config={"stroke_width":6, "max_tip_length_to_length_ratio":0.25})
        
        #Adding the grid
        self.play(Create(grid),run_time=2)
        
        #Adding the charge
        self.play(Create(dot))
        
        self.play(Create(dot_2))
        
        #Adding the vector field
        self.play(Create(vector_field),run_time=6)
        
        #Waiting 2 seconds        
        self.wait(5)
        
