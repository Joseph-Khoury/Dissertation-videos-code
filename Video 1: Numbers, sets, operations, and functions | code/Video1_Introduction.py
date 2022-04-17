from manim import *

SVGImages = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\SVGImages"

class Scene1(Scene):
    def construct(self):
        
        ##Section 1
        self.next_section(name="Advanced Concept", skip_animations=True)
        definitions = MathTex(
            r"x &: t \mapsto x(t) \\ X &: s \mapsto X(s) \\ \mathscr{L} &: x(t) \mapsto X(s)" \
            r"\\ X(&s)=\mathscr{L}\{x(t)\}=\int_{-\infty}^{\infty} x(t) e^{-st} \,dt", 
            font_size=36
        ).to_corner(UL)
        
        axes1 = Axes(
            x_range=[0, 16, 4],
            y_range=[-4, 3.9, 1],
            x_length=4,
            y_length=3,
            tips=True
        ).to_corner(DL).shift(0.75*UP + RIGHT)
        
        axes2 = Axes(
            x_range=[0, 16, 4],
            y_range=[-4, 6, 1],
            x_length=4,
            y_length=4.5,
            tips=True
        ).to_corner(DR).shift(0.75*UP + LEFT)
        
        arrow = MathTex(r"\mapsto", font_size=60).move_to(axes1.get_right() + 1.5*RIGHT)
        
        time_domain_function = axes1.plot(
            lambda x:
                12/PI*( 
                    np.sin(3*PI*x/10)/3 +
                    np.sin(7*PI*x/10)/7 +
                    np.sin(9*PI*x/10)/9 +
                    np.sin(11*PI*x/10)/11
                )
        ).set_color(RED)
        
        s1 = Cross(Dot(axes2.coords_to_point(0, 3*PI/10)))
        s2 = Cross(Dot(axes2.coords_to_point(0, -3*PI/10)))
        s3 = Cross(Dot(axes2.coords_to_point(0, PI/5)))
        s4 = Cross(Dot(axes2.coords_to_point(0, -PI/5)))
        s5 = Cross(Dot(axes2.coords_to_point(0, 7*PI/10)))
        s6 = Cross(Dot(axes2.coords_to_point(0, -7*PI/10)))
        s7 = Cross(Dot(axes2.coords_to_point(0, 9*PI/10)))
        s8 = Cross(Dot(axes2.coords_to_point(0, -9*PI/10)))
        s9 = Cross(Dot(axes2.coords_to_point(0, 11*PI/10)))
        s10 = Cross(Dot(axes2.coords_to_point(0, -11*PI/10)))
        
        s_domain_function = VGroup(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10).set_stroke(width=2.5)
        
        self.play(
            LaggedStart(
                Write(definitions),
                Create(axes1),
                Write(time_domain_function),
                Write(arrow),
                Create(axes2),
                Write(s_domain_function, run_time=1),
                lag_ratio=0.25
            )
        )
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        ##Section 2
        self.next_section(name="Basic concept", skip_animations=True)
        apples1 = SVGMobject(f'{SVGImages}\\Apple.svg').to_edge(LEFT)
        text_1 = MathTex(r"1").next_to(apples1, DOWN)
        
        apples2 = VGroup(apples1.copy().move_to(ORIGIN).shift(2*LEFT))
        apples2 += apples1.copy().next_to(apples2[0], RIGHT, buff=0)
        text_2 = MathTex(r"2").next_to(apples2, DOWN)
        
        apples3 = VGroup(apples1.copy().to_edge(RIGHT))
        apples3 += apples1.copy().next_to(apples3[0], LEFT, buff=0)
        apples3 += apples1.copy().next_to(apples3[1], LEFT, buff=0)
        text_3 = MathTex(r"3").next_to(apples3, DOWN)
        
        all_mobjects = VGroup(apples1, apples2, apples3, text_1, text_2, text_3)
        apples_frame = SurroundingRectangle(VGroup(all_mobjects), WHITE, buff=0.2)
        
        # VGroup(all_mobjects, frame).scale(0.2)
        
        self.play(
            LaggedStart(
                GrowFromCenter(apples1),
                FadeIn(text_1),
                GrowFromCenter(apples2),
                FadeIn(text_2),
                GrowFromCenter(apples3),
                FadeIn(text_3),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(FadeIn(apples_frame))
        self.wait(2)
        
        ##Section 3
        self.next_section(name="Path to goal", skip_animations=True)
        goal_text = Text("Goal", font_size=36)
        goal_frame = SurroundingRectangle(goal_text, color=WHITE, buff=0.3)
        goal = VGroup(goal_text, goal_frame).to_corner(UR, buff=1.5)
        
        self.play(VGroup(all_mobjects, apples_frame).animate.scale(0.3).shift(DOWN).to_edge(LEFT))
        self.play(Write(goal))
        
        bp1 = Dot(apples_frame.get_right())
        bp2 = Dot(goal_frame.get_left())
        bp3 = Dot(bp1.copy().get_center() + 5*RIGHT)
        bp4 = Dot(bp2.copy().get_center() + 5*LEFT)
        
        path = CubicBezier(bp1.get_center(), bp3.get_center(), bp4.get_center(), bp2.get_center())
        
        self.play(Write(path))
        self.wait(2)
        
        ##Section 4
        self.next_section(name="New idea", skip_animations=True)
        idea_point = Dot(path.point_from_proportion(0.6), fill_opacity=0, stroke_width=2, color=GREEN,radius=0.2)
        idea_arrow = Line(
            idea_point.get_center() + 2*LEFT + UP,
            idea_point.get_center() + 0.3*LEFT + 0.2*UP,
            color=GREEN
        ).add_tip()
        idea_text = Text("New perspective", font_size=24, color=GREEN).move_to(idea_arrow.get_start()+0.5*UP + LEFT)
        
        self.play(
            LaggedStart(
                Write(idea_text, run_time=0.8),
                GrowFromEdge(idea_arrow,UL),
                GrowFromCenter(idea_point),
                lag_ratio=0.2,
            )
        )
        self.play(Flash(idea_text, flash_radius=1.5))
        self.wait(2)
        









class Test(Scene):
    def construct(self):
       return
        