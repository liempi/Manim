from manim import *
import numpy as np

class electric_field(Scene):
    def construct(self):
        #Setting the grid
        grid = NumberPlane(color=BLUE,background_line_style={
                "stroke_color": WHITE,
                "stroke_opacity": 0.1}
                )
        #Adding axis labels
        grid.add(grid.get_axis_labels())
        
        #Charge definition, if carga<0 color: BLUE  elif carga>0 color:RED
        def charge(color,x_0):
            if color == RED:
                dot = Dot(radius=0.05,color=PURE_RED).shift(np.array([x_0[0],x_0[1],x_0[2]]))
            elif color == BLUE:
                dot = Dot(radius=0.1,color=PURE_BLUE).shift(np.array([x_0[0],x_0[1],x_0[2]]))
            return dot
            
        #Coordinates of charge
        x_0 = np.array([1,0,0])

        #Avoid zero division error
        eps=0.000001

        #Function to calculate the vector field. The first value is the charge in Coulombs.
        function = lambda x: -200/(4*PI) *np.array([(x[0]-x_0[0])/((x[0]-x_0[0])**2+(x[1]-x_0[1])**2+eps)**(3/2),\
            (x[1]-x_0[1])/((x[0]-x_0[0])**2+(x[1]-x_0[1])**2+eps)**(3/2)])
        
        
        #Vector field
        vector_field = ArrowVectorField(function,color_scheme=None,min_color_scheme_value=0,\
                  max_color_scheme_value=5,color=PURE_BLUE,vector_config={"stroke_width":6})
        
        #Adding the grid
        self.play(Create(grid),run_time=2)
        
        #Adding the charge
        self.play(Create(charge(RED,x_0)))
        
        #Adding the vector field
        self.play(Create(vector_field),run_time=6)
        
        #Waiting 2 seconds        
        self.wait(2)
        
