from manimlib.imports import *
import math
import numpy as np



class Graphing(GraphScene):
    
    
    CONFIG = {
        "x_min": -7,
        "x_max": 7,
        "y_min": -7,
        "y_max": 7,
        "function_color": WHITE,
        "axes_color": BLUE,
        "y_axis_label": "$x_2$",
        "x_axis_label": "$x_1$",
        "x_labeled_nums" : [0,1,2,3,4,5,6,7],
        "y_labeled_nums" : [0,1,2,3,4,5,6,7],
        "graph_origin": ORIGIN,
        
    }

    def construct(self):
        
        Title = TextMobject("Primal Simplex Algoritmh")
        Title.set_color_by_gradient(BLUE, GREEN)
        Title.scale(1.3)
        Title.to_edge(UP,buff=1)
        text1 = TextMobject("Lets now see how the simplex algoritmh")
        text2 = TextMobject("optimized the Reddy Mikks problem through an animation.")
        
        text1.next_to(Title,DOWN,buff=.5)
        text2.next_to(text1,DOWN)
        text_group_a = VGroup(text1,text2)
        
        ReddyMikks = TextMobject("Reddy Mikks Problem")
        Problem1 = TextMobject("Maximize z = 5$x_1 + 4x_2$")
        Problem2 = TextMobject("s.t. $6x_1+4x_2\\le24$")
        Problem3 = TextMobject("       $x_1+2x_2\\le6$")
        Problem4 = TextMobject("       $-x_1+x_2\\le1$")
        Problem5 = TextMobject("            $x_2\\le2$")
        Problem6 = TextMobject("        $x_1,x_2\\ge0$")
        
        ReddyMikks.next_to(text2,DOWN,buff=.1)
        Problem1.next_to(ReddyMikks,DOWN)
        Problem2.next_to(Problem1,DOWN)
        Problem3.next_to(Problem2,DOWN)
        Problem4.next_to(Problem3,DOWN)
        Problem5.next_to(Problem4,DOWN)
        Problem6.next_to(Problem5,DOWN)
        text_group_Problem = VGroup(ReddyMikks,Problem1,Problem2,Problem3,Problem4,Problem5,Problem6)
        text_group_Problem.scale(.7)
        
        text3 = TextMobject("To do that, we first need to draw the problem's feasible region,")
        text4 = TextMobject("also known as the solution space.")       
        
        text4.next_to(text3,DOWN)
       
        
        
        text5 = TextMobject("It is the set of all possible points,")
        text6 = TextMobject("sets of values of the choise variables ","$x_1$,","$x_2$ ")
        text7 = TextMobject("that satisfy the problem's constraints.")
        
        text6.next_to(text5,DOWN)
        text7.next_to(text6,DOWN)
        text_group = VGroup(text5,text6,text7)
        
        text8 = TextMobject("Let's start with the first constraint: ", "$6x_1+4x_2\\le24$")
        text9 = TextMobject("The solution space of this constraint is one of the ")
        text10 = TextMobject("closed half-planes ",color=GOLD_B)
        text11 = TextMobject("defined by the equation: " ,"$6x_1+4x_2 = 24$")
        
        text9.next_to(text8,DOWN)
        text10.next_to(text9,DOWN)
        text11.next_to(text10,DOWN)
        
        text_group0 = VGroup(Title,text8,text9,text10,text11)
        
        self.play(FadeIn(Title))
        self.play(Write(text_group_a))
        self.wait(3)
        self.play(Write(text_group_Problem))
        self.wait(3)
        self.play(FadeOut(text_group_Problem))
        self.play(FadeOut(text_group_a))
        self.play(FadeIn(text3))
        self.wait()
        self.play(FadeIn(text4))
        self.play(FadeOut(text3))
        self.play(FadeOut(text4))
        self.play(Write(text_group))
        self.wait(3)
        self.play(FadeOut(text_group))
        self.play(FadeIn(text8))
        self.wait(2)
        self.play(FadeIn(text9))
        self.wait()
        self.play(FadeIn(text10))
        self.play(FadeIn(text11))
        self.wait(3)
        self.play(FadeOut(text_group0))
        self.wait()
        
        #Make graph
        self.setup_axes(animate=True)
        axes = self.axes
        func_graph=self.get_graph(lambda x : -1.5*x+6, x_min=-1,x_max=6,color = GOLD_A)
        graph_lab = self.get_graph_label(func_graph, label = "6x_1+4x_2 = 24")
        graph = VGroup(axes,func_graph,graph_lab)
        self.play(ShowCreation(func_graph), Write(graph_lab),runtime = 3)
        
        
        arrow0 = Arrow(np.array([0.91,1.91,0]),np.array([2.41,3.41,0]))
        arrow1 = Arrow(np.array([1.91,0.91,0]),np.array([3.41,2.41,0]))
        arrow2 = Arrow(np.array([2.91,-0.09,0]),np.array([4.41,1.41,0]))
        
        arrow4 = Arrow(np.array([0.9,1.9,0]),np.array([-1.1,-0.1,0]))
        arrow5 = Arrow(np.array([1.9,0.9,0]),np.array([-0.1,-1.1,0]))
        arrow6 = Arrow(np.array([-0.1,2.9,0]),np.array([-1.9,0.9,0]))
        arrow7 = Arrow(np.array([2.9,-0.1,0]),np.array([0.9,-2.1,0]))
        
        arrowGroup1 = VGroup(arrow4,arrow5,arrow6,arrow7)
        arrowGroup2 = VGroup(arrow0,arrow1,arrow2)
       
        self.play(GrowArrow(arrow4))
        self.play(GrowArrow(arrow5))
        self.play(GrowArrow(arrow6))
        self.play(GrowArrow(arrow7))
        
        text12 = TextMobject("Every point across and below the line ")
        text13 = TextMobject("is one of the 2 closed half-planes. ")
        text13.next_to(text12,DOWN)
        text_group_1 = VGroup(text12,text13)
        text_group_1.scale(0.5)
        text_group_1.to_corner(UP+RIGHT,buff=2)
        self.play(FadeIn(text_group_1))
        self.wait(3)
        self.play(FadeOut(text_group_1))
        self.play(FadeOut(arrowGroup1))

        self.play(GrowArrow(arrow0))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
         
        text14 = TextMobject("Every point across and above the line ")
        text15 = TextMobject("is the other one of the 2 closed half-planes. ")
        text15.next_to(text14,DOWN)
        text_group_2 = VGroup(text15,text14)
        text_group_2.scale(0.5)
        text_group_2.to_edge(LEFT+UP,buff=2)
        self.play(FadeIn(text_group_2))
        self.wait(3)
        
        self.play(FadeOut(text_group_2))
        self.play(FadeOut(arrowGroup2))
        self.wait()
        
        self.play(graph.shift, LEFT*4,
                  graph.scale, 0.65)
        
        text16 = TextMobject("An easy way to determine the half-plane")
        text17 = TextMobject("decipting the solution space of a linear inequality,")
        text18 = TextMobject("is to test whether the point (0,0) satisfies the inequality.")
        text19 = TextMobject("In case of a positive answer, the solution space")
        text20 = TextMobject("is the half-space containing the origin,")
        text21 = TextMobject("otherwise it is the other one.")
        text17.next_to(text16,DOWN)
        text18.next_to(text17,DOWN)
        text19.next_to(text18,DOWN)
        text20.next_to(text19,DOWN)
        text21.next_to(text20,DOWN)
        text_group_3 = VGroup(text16,text17,text18,text19,text20,text21)
        text_group_3.scale(0.5)
        text_group_3.to_corner(UP+RIGHT,buff=1.5)
        self.play(FadeIn(text_group_3))
        self.wait(5)
        self.play(FadeOut(text_group_3))
        
        text22 = TextMobject("We can easily notice that the point (0,0)")
        text23 = TextMobject("satisfies the inequality ", "$6x_1+4x_2\\le24$")
        text24 = TextMobject("because $0\\le24$.")
        text25 = TextMobject("This means that every point across and below the line")
        text26 = TextMobject("is inside the constraint's solution space")
        text23.next_to(text22,DOWN)
        text24.next_to(text23,DOWN)
        text25.next_to(text24,DOWN)
        text26.next_to(text25,DOWN)
        text_group_4 = VGroup(text22,text23,text24,text25,text26)
        text_group_4.scale(0.5)
        text_group_4.to_corner(UP+RIGHT,buff=1.5)
        
        text27 = TextMobject("(0,0)")
        text27.move_to(np.array([-4.2,-0.4,0]))
        text27.scale(0.6)
        dot1  = Dot(np.array([-3.63,0.1,0]),color=RED,radius=0.1)
        
        self.play(FadeIn(text_group_4))
        self.play(FadeIn(text27))
        self.play(FadeIn(dot1))
        self.wait(5)
        self.play(FadeOut(text_group_4))
       
        text27 = TextMobject("Now, if we also take into consideration the problem's")
        text28 = TextMobject("non-negativity constraints: ", "$x_1\\ge0, x_2\\ge0$")
        text29 = TextMobject("it is logical to remove the negative sections of the axes.")
        text28.next_to(text27,DOWN)
        text29.next_to(text28,DOWN)
        text_group_5 = VGroup(text27,text28,text29)
        text_group_5.scale(0.5)
        text_group_5.to_corner(UP+RIGHT,buff=1.5)
        self.play(FadeIn(text_group_5))
        self.wait(5)
