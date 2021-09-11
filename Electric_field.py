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
        def charge(color,x_0,y_0):
            if color == RED:
                dot = Dot(radius=0.2,color=PURE_RED).shift(x_0*LEFT+y_0*UP)
            elif color == BLUE:
                dot = Dot(radius=0.2,color=PURE_BLUE).shift(x_0*LEFT+y_0*UP)
            return dot
            
        #Avoid zero division error
        eps=0.000001

        #Function to calculate the vector field. The first value is the charge in Coulombs.
        function = lambda x: -200 / (4*PI) * np.array([(x[0])/(x[0]**2+x[1]**2+eps)**(3/2),\
                    (x[1])/(x[0]**2+x[1]**2+eps)**(3/2)])
        
        
        #Vector field
        vector_field = ArrowVectorField(function,color_scheme=None,min_color_scheme_value=0, max_color_scheme_value=5,color=PURE_BLUE,vector_config={"stroke_width":
        6})
        
        #Adding the grid
        self.play(Create(grid),run_time=2)
        
        #Adding the charge
        self.play(Create(charge(RED,0,0)))
        
        #Adding the vector field
        self.play(Create(vector_field))
        
        #Waiting 2 seconds        
        self.wait(2)
        
