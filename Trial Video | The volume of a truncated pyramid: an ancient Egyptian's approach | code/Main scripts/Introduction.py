from manim import *
from CustomScripts.CustomShapes import Pyramid
        
#Folder addresses
Images = r'D:\Files\OneDrive - Heriot-Watt University\Manim\Images'
SVGImages = r'D:\Files\OneDrive - Heriot-Watt University\Manim\SVGImages'

class Scene1(Scene):   
    def construct(self):

        ##Section 0
        self.next_section(skip_animations=False)
        self.wait(4)
        
        ##Section 1
        self.next_section(skip_animations=False)
        
        image1 = ImageMobject(f'{Images}\\Rhind_Mathematical_Papyrus.jpg').shift(0.2*UP)
        text1 = MarkupText(f'<b>Rhind Papyrus</b>, <i> circa 1550 BCE </i>', font_size=26).next_to(image1,DOWN,buff=0.25)
        G1 = Group(image1,text1) #Grouping relevant text and images together
        
        self.play(FadeIn(image1))
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(G1,shift=DOWN))
        self.wait()
        
        ##Section 2
        self.next_section(skip_animations=False)
        
        image2 = ImageMobject(f'{Images}\\Papyrus_Sheet.png')
        image3 = SVGMobject(f'{SVGImages}\\Ancient_Egyptian_Art.svg').to_edge(DOWN).shift(2.5*LEFT+UP)
        image4 = SVGMobject(f'{SVGImages}\\World.svg').next_to(image3).shift(RIGHT)
        image5 = ImageMobject(f'{Images}\\Papyrus.png').scale(0.5)
        
        self.play(FadeIn(image2))
        self.wait()
        self.play(image2.animate.shift(2*UP).scale(0.5))
        self.play(DrawBorderThenFill(image3), run_time=1)
        self.play(Write(image4))
        self.wait()
        self.play(FadeOut(Group(image2,image3,image4)))
        
        ##Section 3
        self.next_section(skip_animations=False)
        
        image6 = ImageMobject(f'{Images}\\Paper.png').scale(0.2)
        
        self.play(FadeIn(image5))
        self.wait()
        self.play(image5.animate.shift(2.2*LEFT))
        arrow1 = Line(image5.get_right() + 0.2*RIGHT,image5.get_right() + 1.2*RIGHT).add_tip()
        self.play(LaggedStart(Write(arrow1), FadeIn(image2.next_to(arrow1,RIGHT)), lag_ratio=0.5))
        self.wait()
        self.play(FadeOut(Group(image5,arrow1), shift=DOWN), image2.animate.move_to(2*UL))
        ##Section 4
        self.next_section(skip_animations=False)
        
        lines = []
        nodes = []
        node_temp = Circle(0.5, color = DARK_BLUE, fill_opacity=1)
        
        lines.append(Line(image2.get_right(), image2.get_right() + 1.2*RIGHT)) #top horizontal line [0]
        nodes.append(node_temp.copy().set_fill(color = RED).next_to(lines[0].get_right(), buff=0))#grand parent node [0]
        
        lines.append(Line(lines[0].get_center() + 0.2*LEFT, lines[0].get_center() + 0.2*LEFT + 1.5*DOWN))#top vertical line [1]
        lines.append(Line(lines[1].get_end() + 3*LEFT, lines[1].get_end() + 3*RIGHT)) #middle horizontal line [2]
        lines.append(Line(lines[2].get_left(),lines[2].get_left() + DOWN)) #middle left vertical line [3]
        nodes.append(node_temp.copy().set_fill(color = ORANGE).next_to(lines[3].get_bottom(), DOWN, buff=0)) #parent left node [1]
        lines.append(Line(lines[2].get_right(), lines[2].get_right() + DOWN))#middle right vertical line [4]
        nodes.append(node_temp.copy().set_fill(color = ORANGE).next_to(lines[4].get_bottom(), DOWN, buff=0)) #parent right node [2]
        
        lines.append(Line(nodes[1].get_right(), nodes[1].get_right() + RIGHT)) #bottom left horizontal line [5]
        nodes.append(node_temp.copy().set_fill(color = BLUE).next_to(lines[5].get_end(), RIGHT, buff=0)) #parent left spousal node [3]
        lines.append(Line(nodes[2].get_left(), nodes[2].get_left() + LEFT)) #bottom right horizontal line [6]
        nodes.append(node_temp.copy().set_fill(color = GREEN).next_to(lines[6].get_left(), LEFT, buff=0)) # parent right spousal node [4]
        lines.append(Line(lines[5].get_center(), lines[5].get_center() + DOWN)) #bottom left vertical line [7]
        lines.append(Line(lines[6].get_center(), lines[6].get_center() + DOWN)) #bottom right vertical line [8]
        
        nodes.append(node_temp.copy().set_fill(color = PURPLE).next_to(lines[7].get_end(), DOWN, buff=0)) #child left node [5]
        nodes.append(node_temp.copy().set_fill(color = YELLOW).next_to(lines[8].get_end(), DOWN, buff=0)) #child right node [6]
        lines.append(Line(nodes[6].get_right(), nodes[6].get_right() + RIGHT)) #floor right horizontal line [9]
        image6.next_to(lines[9].get_end(), RIGHT, buff=0)
    
        self.play(LaggedStart(
            Write(lines[0]),
            DrawBorderThenFill(nodes[0]),
            Write(VGroup(*lines[1:5])),
            DrawBorderThenFill(VGroup(*nodes[1:3])),
            Write(VGroup(*lines[5:7])),
            Write(VGroup(*nodes[3:5])),
            Write(VGroup(*lines[7:9])),
            Write(VGroup(*nodes[5:7])),
            Write(lines[9]),
            FadeIn(image6),
            lag_ratio=0.5,
            run_time=4
        )
                  )
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        ##Section 5
        self.next_section(skip_animations=False)
        papyrus_text = Text(r'Papyrus', font_size=34)
        self.play(Write(papyrus_text))
        self.play(papyrus_text.animate.shift(1.2*LEFT))
        arrow2 = Line(papyrus_text.get_right()+0.2*RIGHT, papyrus_text.get_right() + 1.2*RIGHT).add_tip()
        paper_text = Text(r'Paper', font_size=34).next_to(arrow2,RIGHT,buff=0.2)
        dummy = papyrus_text.copy().move_to(paper_text)
        self.play(LaggedStart(Write(arrow2, run_time=0.75), ReplacementTransform(papyrus_text.copy(),dummy), lag_ratio=0.5))
        self.play(ReplacementTransform(dummy,paper_text))
        self.wait()
        self.play(Unwrite(VGroup(papyrus_text,arrow2,paper_text)))
        self.wait()
        
        ##Section 6
        self.next_section(skip_animations=False)
        
        text1 = MarkupText(f'<b>Papyri</b>', font_size=42, font="Poppins").shift(1.5*UP + 3*LEFT)
        text2 = Text(u'(pəˈpaɪəraɪ)',font_size=28, slant=ITALIC, color=GRAY).next_to(text1, 2*RIGHT)
        text3 = MarkupText(f'<span fgcolor = "{RED}" font="Times New Roman">PLURAL NOUN</span>', font_size=30).move_to(text1.get_left() + DOWN, LEFT)
        text4 = MarkupText(f'Plural of <span fgcolor="{YELLOW}"><i>Papyrus</i></span>', font_size=28, font="Poppins").move_to(text3.get_left() + 1.2*DOWN, LEFT)
        papyri_text = VGroup(text1,text2,text3,text4)
        
        self.play(Write(papyri_text))
        self.wait()
        self.play(Unwrite(papyri_text))
        self.wait()
        
        ##Section 7
        self.next_section(skip_animations=False)
        
        cloth_image = SVGMobject(f'{SVGImages}\\Textiles.svg')
        rope_image = SVGMobject(f'{SVGImages}\\Rope.svg').set_fill(color=YELLOW_B)
        hieroglyph_image = SVGMobject(f'{SVGImages}\\egyptian_lorem_ipsem.svg').scale(2)
        
        self.play(Write(cloth_image))
        self.play(ReplacementTransform(cloth_image,rope_image))
        self.wait(0.5)
        self.play(ReplacementTransform(rope_image,hieroglyph_image))
        self.wait()
        self.play(Unwrite(hieroglyph_image))
        
        ##Section 8
        self.next_section(skip_animations=False)
        
        henry_rhind_portrait = ImageMobject(f'{Images}\\Alexander_Rhind_Portrait.png').scale(0.6).to_edge(LEFT, buff=1.75)
        portrait_text = Text(f'Portrait of Alexander Henry Rhind of Sibster, \noil on canvas, \nby Alexander S. Mackay, 1874', font_size=16).next_to(henry_rhind_portrait, DOWN)
        
        self.play(FadeIn(G1))
        self.wait()
        self.play(G1.animate.to_edge(RIGHT).scale(0.75))
        self.play(FadeIn(henry_rhind_portrait))
        self.play(Write(portrait_text))
        self.wait(2)
        self.play(LaggedStart(Unwrite(portrait_text), FadeOut(G1, henry_rhind_portrait), lag_ratio=0.6))
        
        ##Section 9
        self.next_section(skip_animations=False)
        
        s9_text1 = Tex(f'$84$ Problems $+$ solutions', font_size=52)
        s9_text2 = Tex(f'Problem $n$: ').to_edge(UL,buff=1.5).shift(0.5*UP)
        
        vertices = [
            LEFT,
            RIGHT,
            RIGHT + 8/3*UP
        ]
        
        pythag_triangle = Polygon(*vertices, stroke_color=WHITE)
        
        lines = {                                         #  
            'base': Line(vertices[0], vertices[1]),       #
            'height': Line(vertices[1], vertices[2]),     # Lines for reference; will not be plotted
            'hypotneuse': Line(vertices[0], vertices[2])  #
        }                                                 #
        
        side_labels = VGroup(
            MathTex("3").move_to(pythag_triangle.get_bottom() + 0.4*DOWN),
            MathTex("4").move_to(pythag_triangle.get_right() + 0.4*RIGHT),
            MathTex("x").move_to(lines['hypotneuse'].point_from_proportion(0.5) + 0.4/np.sqrt(2)*UL)
        )
        
        right_angle_indicator = RightAngle(lines['base'],lines['height'], length=(8/3)/10, quadrant=(-1,1))
        angle_indicator = Angle(lines['base'],lines['hypotneuse'], radius=(2)/6)
        angle_label = MathTex(r'\theta', font_size=38).move_to(Angle(lines['base'],lines['hypotneuse'], radius=(2)/6 + 0.3).point_from_proportion(0.5))
        angle_indicators = VGroup(right_angle_indicator, angle_indicator, angle_label)
        
        pythag_triangle_group = VGroup(pythag_triangle,side_labels, angle_indicators).shift(0.5*DOWN)
        
        
        self.play(Write(s9_text1))
        self.wait(0.5)
        self.play(ReplacementTransform(s9_text1, s9_text2))
        self.wait(0.3)
        self.play(LaggedStart(*[Write(pythag_triangle_group[x]) for x in range(len(pythag_triangle_group))], lag_ratio=0.5))
        self.wait(0.2)
        
        equations = VGroup(
            side_labels[2].copy().next_to(pythag_triangle_group, 0.5*DOWN, buff=1.5).shift(0.5*LEFT),
        )
        equations += MathTex("=").next_to(equations[0],RIGHT,buff=0.1)
        equations += MathTex("5").next_to(equations[1],RIGHT,buff=0.1)
        
        self.play(ReplacementTransform(side_labels[2].copy(),equations[0], run_time=0.8))
        self.play(ReplacementTransform(equations[0].copy(), VGroup(equations[1],equations[2]), run_time=1))
        self.play(
            LaggedStart(
                FadeOut(VGroup(*equations[0:2]), shift=DOWN),
                AnimationGroup(FadeOut(side_labels[2]), equations[2].animate.move_to(side_labels[2])),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Unwrite(VGroup(pythag_triangle, *side_labels[0:2], *angle_indicators, equations[2], s9_text2)))
        self.wait()
 
 
 
 
        
class Scene2(ThreeDScene):
    def construct(self):
        
        ##Section1
        self.next_section(skip_animations=False)
        
        self.write_text()
        self.create_pyramid()
        self.wait(1.5)
        self.label_pyramid()
        self.play(AnimationGroup(self.pyramid.animate.to_edge(LEFT,buff=2), self.arrow_group.animate.to_edge(LEFT, buff=1.9).shift(0.02*DOWN)))
        
        ##section 2
        self.next_section(skip_animations=False)
        
        self.animate_calculation()
        self.wait(6)
        self.play(Unwrite(self.truncated_pyramid_volume))
        self.wait()
        
        ##Section 3
        self.next_section(skip_animations=False)
        
        self.animate_algebraic_expression()
        self.wait(1.5)
        self.questioning()
        self.wait(1.5)
        
        ##Section 4
        self.next_section(skip_animations=False)
        
        self.animate_pythagorean_theorem()
        self.wait()
        self.animate_cartesian_coordinates()
        self.wait()
        
        ##Section 5
        self.next_section(skip_animations=False)
        
        self.clean_up_and_focus_on_pyramid()
        self.wait()
        self.limit_toolset_animation()
        self.wait()
        self.pyramid_to_video_toolset()
        self.wait(5)
        self.fade_to_black()
        self.wait()
        
        
    ##Class methods  
    def write_text(self):
           
        problem_text = Tex(f'Translation: “If you are told: A truncated pyramid of 6 for the vertical height \n\
                           by 4 on the base by 2 on the top. You are to square this 4, result 16. \n\
                           You are to double 4, result 8. You are to square 2, result 4.\n\
                           You are to add the 16, the 8, and the 4, result 28. You are to take a third of 6, result 2. \n\
                            You are to take 28 twice, result 56. See, it is 56. You will find it right.”', font_size=36).to_edge(UP, buff=1)
        
        self.play(GrowFromCenter(problem_text, run_time=1.5))
        
        #Instance variables
        self.problem_text=problem_text
        
        
        
    def create_pyramid(self):
        pyramid = Pyramid(4,2,6,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = YELLOW_B).scale(0.25).shift(DOWN*0.75)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        self.play(Write(pyramid))
        
        #Instance variables
        self.pyramid=pyramid
        
        
    
    def calculate_rotation_matrices(self):
        rotation = np.matmul(
            rotation_matrix(PI/8,RIGHT),
            np.matmul(rotation_matrix(-PI/15, UP), rotation_matrix(-PI/2, RIGHT))
        )
        
        height_arrow_vertices = [
            np.matmul(rotation, np.array([[2],[0],[0]])/4).reshape(1,3),
            np.matmul(rotation, np.array([[1],[0.75],[6]])/4).reshape(1,3)
        ]
        
        major_base_arrow_vertices = [
            np.matmul(rotation, np.array([[-2],[-2],[0]])/4).reshape(1,3),
            np.matmul(rotation, np.array([[2],[-2],[0]])/4).reshape(1,3)
        ]
        
        minor_base_arrow_vertices = [
            np.matmul(rotation, np.array([[-1],[-1],[6]])/4).reshape(1,3),
            np.matmul(rotation, np.array([[1],[-1],[6]])/4).reshape(1,3)
        ]
        
        #Instance variables
        self.height_arrow_vertices=height_arrow_vertices
        self.major_base_arrow_vertices=major_base_arrow_vertices
        self.minor_base_arrow_vertices=minor_base_arrow_vertices
        
        
        
    def label_pyramid(self):
        self.calculate_rotation_matrices()
        
        height_arrow = Line(*self.height_arrow_vertices, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(RED)

        major_base_arrow = Line(*self.major_base_arrow_vertices, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
        
        minor_base_arrow = Line(*self.minor_base_arrow_vertices, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(GREEN_E)
        
        arrows = VGroup(height_arrow, major_base_arrow, minor_base_arrow).move_to(self.pyramid.get_edge_center(DL), DL).shift(DOWN*0.05)
        
        height_label = MathTex("6", font_size = 18).move_to(height_arrow.point_from_proportion(0.5) + RIGHT*0.1 + UP*0.05).set_color(RED)
        major_base_label = MathTex("4", font_size = 18).move_to(major_base_arrow.point_from_proportion(0.5) + DOWN*0.1).set_color(rgb_to_color([0.2,0.2,1]))
        minor_base_label = MathTex("2", font_size = 18).move_to(minor_base_arrow.point_from_proportion(0.5) + DOWN*0.1).set_color(GREEN_E)
         
        labels = VGroup(height_label, major_base_label, minor_base_label)
        arrow_group = VGroup(*arrows, *labels)
        
        self.play(
            LaggedStart(
                Write(height_arrow),
                Write(height_label),
                lag_ratio=0.75
            )
        )
        self.wait(0.25)
        self.play(
            LaggedStart(
                Write(major_base_arrow),
                Write(major_base_label),
                lag_ratio=0.75
            )
        )
        self.wait(0.25)
        self.play(
            LaggedStart(
                Write(minor_base_arrow),
                Write(minor_base_label),
                lag_ratio=0.75
            )
        )
        
        #Instance variables
        self.height_arrow=height_arrow
        self.major_base_arrow=major_base_arrow
        self.minor_base_arrow=minor_base_arrow
        self.arrows=arrows
        self.height_label=height_label
        self.major_base_label=major_base_label
        self.minor_base_label=minor_base_label
        self.labels=labels
        self.arrow_group=arrow_group
        
        
        
    def animate_calculation(self):
        
        base_tex = self.major_base_label.copy().move_to(0.75*DOWN + 1.25*LEFT).scale(DEFAULT_FONT_SIZE/18)
        top_tex = self.minor_base_label.copy().move_to(0.75*DOWN).scale(DEFAULT_FONT_SIZE/18)
        height_tex = self.height_label.copy().move_to(0.75*DOWN + 1.75*LEFT).scale(DEFAULT_FONT_SIZE/18)
        
        square1 = MathTex(f'^2').next_to(base_tex, UR, buff=0.05).shift(0.05*DOWN)
        term1 = VGroup(base_tex, square1)
        result1 = MathTex("16").move_to(term1.get_bottom(), DOWN)
        
        term2 = VGroup(top_tex.copy().shift(0.25*LEFT), MathTex("\cdot").shift(0.75*DOWN), base_tex.copy().move_to(top_tex.shift(0.25*RIGHT)))
        result2 = MathTex("8").move_to(0.75*DOWN)
        
        term3 = VGroup(top_tex.copy().shift(0.85*RIGHT))
        term3 += MathTex("^2").next_to(term3[0], UR, buff=0.05).shift(0.05*DOWN)
        result3 = MathTex("4").move_to(term3.get_bottom(), DOWN)
        
        additions = VGroup(MathTex("+").move_to(top_tex.copy()).shift(0.8*LEFT))
        additions += MathTex("+").move_to(top_tex.copy()).shift(0.35*RIGHT)
        
        addition_result = MathTex("28").move_to(top_tex)
        
        term4_placeholder = height_tex.copy().next_to(addition_result,LEFT,buff=0.5).align_to(addition_result,DOWN)
        term4 = VGroup(MathTex(f'\\frac{"6"}{"3"}').move_to(term4_placeholder))
        result4 = MathTex("2").next_to(addition_result,LEFT,buff=0.5)
        
        multiplication_dot = MathTex(f'\cdot').next_to(addition_result, LEFT, buff=0.25)
        
        volume_tex = VGroup(MathTex("56").move_to(top_tex))
        volume_tex += MathTex(f'V_{"P"}=').next_to(volume_tex,LEFT, buff=0.1)
        
        box = SurroundingRectangle(volume_tex, PURPLE)
        
        truncated_pyramid_volume = VGroup(volume_tex,box)
        
        self.play(
            LaggedStart(
                ReplacementTransform(
                self.major_base_label.copy(),
                base_tex
                ),
                Write(square1),
                lag_ratio=0.75
            )
        )
        self.play(
            ReplacementTransform(
                term1, 
                result1
                )
            )
        
        self.play(
                ReplacementTransform(
                VGroup(self.major_base_label.copy(), self.minor_base_label.copy()),
                term2,
                run_time=1.5
                )
        )
        self.play(ReplacementTransform(term2, result2))
        
        self.play(
            LaggedStart(
                ReplacementTransform(
                self.minor_base_label.copy(),
                term3[0]
                ),
                Write(term3[1]),
                lag_ratio=0.75
            )
        )
        self.play(
            ReplacementTransform(
                term3, 
                result3
            )
        )
        
        self.play(
            LaggedStart(*[Write(additions[x]) for x in range(len(additions))], lag_ratio=0.5)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(
                VGroup(result1,result2,result3,additions),
                addition_result
            )
        )
        self.wait(0.25)
        
        self.play(
            ReplacementTransform(
                self.height_label.copy(),
                term4_placeholder
            )
        )
        self.play(
            ReplacementTransform(
                term4_placeholder,
                term4
            )
        )
        self.wait(0.1)
        self.play(
            ReplacementTransform(
                term4,
                result4
            )
        )
        self.play(GrowFromCenter(multiplication_dot))
        self.wait(0.4)
        self.play(
            ReplacementTransform(
                VGroup(result4,multiplication_dot, addition_result),
                volume_tex[0]
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                Write(volume_tex[1]),
                Write(box),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Circumscribe(volume_tex))
        
        
        #Instance variables
        self.truncated_pyramid_volume=truncated_pyramid_volume
        
    
    
    def animate_algebraic_expression(self):
            
        top_label_algebraic = MathTex("a").move_to(self.minor_base_label).scale(18/DEFAULT_FONT_SIZE).set_color(GREEN_E)
        base_label_algebraic = MathTex("b").move_to(self.major_base_label).scale(18/DEFAULT_FONT_SIZE).set_color(rgb_to_color([0.2,0.2,1]))
        height_label_algebraic = MathTex("h").move_to(self.height_label).scale(18/DEFAULT_FONT_SIZE).set_color(RED)
        
        algebraic_labels = VGroup(height_label_algebraic, base_label_algebraic, top_label_algebraic)
        
        base_tex_algebraic = base_label_algebraic.copy().move_to(0.7*DOWN + 1.25*LEFT).scale(DEFAULT_FONT_SIZE/18)
        square1 = MathTex(f'^2').next_to(base_tex_algebraic, UR, buff=0.05).shift(0.05*DOWN)
        term1_algebraic = VGroup(base_tex_algebraic, square1)
        
        top_tex_algebraic = top_label_algebraic.copy().scale(DEFAULT_FONT_SIZE/18).move_to(0.75*DOWN + 0.1*LEFT)
        term2_algebraic = VGroup(
            base_tex_algebraic.copy().move_to(0.7*DOWN + 0.15*RIGHT),
            top_tex_algebraic
        )
        additions = VGroup(MathTex("+").next_to(term1_algebraic, RIGHT, buff=0.15)).shift(0.125*DOWN)
        additions += MathTex("+").next_to(term2_algebraic, RIGHT, buff=0.15)
        
        term3_algebraic = VGroup(top_tex_algebraic.copy().next_to(additions[1], RIGHT, buff=0.2).align_to(top_tex_algebraic, DOWN))
        term3_algebraic += MathTex(f'^2').next_to(term3_algebraic[0], UR, buff=0.05).align_to(square1, DOWN)
        
        brackets = VGroup(MathTex("(").scale(1.2).next_to(term1_algebraic, LEFT, buff=0.05))
        brackets += MathTex(")").scale(1.2).next_to(term3_algebraic, RIGHT, buff=0.1)
        brackets.shift(0.1*DOWN)
        
        height_tex_algebraic = height_label_algebraic.copy().scale(DEFAULT_FONT_SIZE/18).next_to(brackets[0], LEFT,buff=0.1)
        term4_algebraic = VGroup(MathTex(r"\frac{h}{3}").move_to(height_tex_algebraic))
        term4_algebraic += height_tex_algebraic.move_to(term4_algebraic[0].get_top(), UP)
        
        self.play(
            ReplacementTransform(
                self.labels,
                algebraic_labels
            )
        )
        self.play(Indicate(algebraic_labels, scale_factor=2), run_time=1.5)
        self.wait(2)
        
        self.play(
            LaggedStart(
                ReplacementTransform(
                    base_label_algebraic.copy(),
                    base_tex_algebraic
                ),
                Write(square1),
                lag_ratio=1
            )
        )
        self.wait(0.5)
        self.play(
            LaggedStart(
                Write(additions[0]),
                ReplacementTransform(
                    VGroup(base_label_algebraic.copy(), top_label_algebraic.copy()),
                    term2_algebraic,
                    run_time=1.5
                ),
                lag_ratio=0.5
            )
        )
        self.wait(0.5)
        self.play(
            LaggedStart(
                Write(additions[1]),
                ReplacementTransform(
                    top_label_algebraic.copy(),
                    term3_algebraic[0]
                ),
                Write(term3_algebraic[1]),
                lag_ratio=1
            )
        )
        self.wait(0.5)
        self.play(Write(brackets))
        self.play(
            ReplacementTransform(
                height_label_algebraic.copy(),
                term4_algebraic
            )
        )
        self.wait()
        
        label_group = VGroup(self.arrows, algebraic_labels)
        
        self.play(
            LaggedStart(
                Unwrite(self.problem_text, run_time=1),
                AnimationGroup(
                    self.pyramid.animate.move_to(ORIGIN).to_edge(UP,buff=1.2),
                    label_group.animate.move_to(ORIGIN).to_edge(UP,buff=1.25).shift(0.05*LEFT)
                ),
                lag_ratio=0.5
            )
        )
        
        expression = VGroup(term1_algebraic,term1_algebraic,term2_algebraic,term3_algebraic, additions,brackets,term4_algebraic)
        volume_tex = MathTex(r"V_{P^{{\dagger}}}=").next_to(expression,LEFT,buff=0).shift(0.4*RIGHT)
        
        self.play(
            AnimationGroup(
                expression.animate.shift(0.6*RIGHT),
                Write(volume_tex)
            )
        )
        self.wait(2)
        
        self.play(Indicate(volume_tex.submobjects[1], 2), run_time=1.5)
        
        pyramid_group = VGroup(self.pyramid, self.arrows, algebraic_labels)
        truncated_pyramid_volume_expression = VGroup(volume_tex, expression)
        
        #Instance variables
        self.pyramid_group = pyramid_group
        self.truncated_pyramid_volume_expression = truncated_pyramid_volume_expression
        
    
    
    def questioning(self):
        
        question_marks = Text("??", color=YELLOW, font_size=50).next_to(self.truncated_pyramid_volume_expression, DOWN)
        self.play(Write(question_marks))
        
        self.question_marks=question_marks
    
     
    def animate_pythagorean_theorem(self):
        
        self.generate_right_triangle(
            2, 
            1, 
            {
                'base_label': "a", 
                'height_label': "b", 
                'hypotneuse_label': "c"
            }, 
            angle_position="both", 
            stroke_width=1.5, 
            label_font_size=32
        )
        
        base_square = Square(
            self.side_lengths['base_length'] + 0.03, 
            stroke_color=PURE_BLUE, 
            stroke_width=1.5, 
            fill_color=BLUE, 
            fill_opacity=0.3
        ).move_to(
            self.triangle.get_bottom() + 0.01*DOWN, UP
        )
        
        height_square = Square(
            self.side_lengths['height_length'], 
            stroke_color=PURE_RED, 
            stroke_width=1.5, 
            fill_color=RED, 
            fill_opacity=0.3
        ).move_to(
            self.triangle.get_right() + 0.01*RIGHT, LEFT
        )
        
        hypotneuse_square = Square(
            self.side_lengths['hypotneuse_length'] + 0.03, 
            stroke_color=PURPLE_E, 
            stroke_width=1.5, 
            fill_color=PURPLE_A, 
            fill_opacity=0.3
        ).align_to(
            base_square.get_corner(UL), DL
        ).rotate(
            self.angle[0], 
            about_point=self.lines['hypotneuse'].get_start()
        ).shift(0.03/np.sqrt(2)*UL)
        
        
        triangle_group = VGroup(
            self.right_triangle,
            base_square,
            height_square,
            hypotneuse_square
        ).to_edge(UL, buff=0.5)


        self.play(
            AnimationGroup(
                Write(self.right_triangle, run_time=1.5),
                VGroup(self.truncated_pyramid_volume_expression, self.question_marks).animate.shift(DOWN)
            )
        )
        self.play(
            LaggedStart(
                AnimationGroup(
                    DrawBorderThenFill(base_square),
                    self.side_labels[0].animate.move_to(base_square.get_center())
                ),
                AnimationGroup(
                    DrawBorderThenFill(height_square),
                    self.side_labels[1].animate.move_to(height_square.get_center())
                ),
                AnimationGroup(
                    DrawBorderThenFill(hypotneuse_square),
                    self.side_labels[2].animate.move_to(hypotneuse_square.get_center())
                ),
                lag_ratio=0.4
            )
        )
        
        no_sign = SVGMobject(f'{SVGImages}\\No_sign.svg').scale(2).move_to(self.right_triangle.get_center())
        
        self.play(DrawBorderThenFill(no_sign))
        
        pythagorean_group = VGroup(triangle_group, no_sign)
        sign_copy = no_sign.copy()
        
        #Variable to be made public
        self.pythagorean_group=pythagorean_group
        self.no_sign=sign_copy
        
        
        
    def generate_right_triangle(
        self,
        base_length: float=3,
        height_length: float=4,
        side_labels: dict={
            'base_label': "",
            'height_label': "",
            'hypotneuse_label': ""
        },
        add_angle_indicators: bool=True,
        angle_position: str=["bottom", "top", "both"],
        add_angle_label: bool=True,
        accurate_angle_label: bool=False,
        label_font_size: str=DEFAULT_FONT_SIZE,
        stroke_color: str=WHITE,
        indicator_stroke_color: str=WHITE,
        stroke_width: float=DEFAULT_STROKE_WIDTH,
        fill_color: str=BLUE,
        fill_opacity: float=0.0,
        ):

        vertices = [
            height_length/2*DOWN + base_length/2*LEFT,
            height_length/2*DOWN + base_length/2*RIGHT,
            height_length/2*UP + base_length/2*RIGHT
        ]
        
        triangle = Polygon(*vertices, stroke_color=stroke_color, stroke_width=stroke_width, fill_color=fill_color, fill_opacity=fill_opacity)
        right_triangle = VGroup(triangle)
        
        lines = {                                           # 
            "base_line": Line(vertices[0], vertices[1]),    #
            "height_line": Line(vertices[1], vertices[2]),  # this dictionary is for reference and will not be plotted
            "hypotneuse": Line(vertices[0], vertices[2])    #
        }                                                   #
        
        side_label_group = VGroup(
            MathTex(side_labels['base_label'], font_size=label_font_size).next_to(lines['base_line'], DOWN, buff=0.2),
            MathTex(side_labels['height_label'], font_size=label_font_size).next_to(lines['height_line'], RIGHT, buff=0.2),
            MathTex(side_labels['hypotneuse_label'], font_size=label_font_size).next_to(ORIGIN, UL, buff=0.2/np.sqrt(2))  #0.5/sqrt(2) is to get a diagonal distance of 0.3 
                                                                                                            #Because the vertices are shifted down by half of the height and shift left and right by half the base-length, 
                                                                                                            #the mid-point of the hypotneuse is at the origin.
        )
        right_triangle += side_label_group
        
        if add_angle_indicators == True:
            
            right_angle_indicator = RightAngle(lines['base_line'],lines['height_line'], length = height_length/8, quadrant=(-1,1), stroke_width=stroke_width, stroke_color=indicator_stroke_color)
            
            if angle_position == "bottom":
                
                angle = round(np.arctan(height_length/base_length),3)
                angle_indicator = Angle(lines['base_line'], lines['hypotneuse'], radius = base_length/6, stroke_width=stroke_width, stroke_color=indicator_stroke_color)
                
                if add_angle_label == True:
                    angle_label_position = Angle(lines['base_line'], lines['hypotneuse'], radius = base_length/6 + angle_indicator.get_arc_length()).point_from_proportion(0.5)
                    
                    if accurate_angle_label == True:
                        angle_label = MathTex(str(angle)).move_to(angle_label_position).scale_to_fit_height(angle_indicator.get_arc_length())
                    else:
                        angle_label = MathTex(r'\theta').move_to(angle_label_position).scale_to_fit_height(angle_indicator.get_arc_length())
                        
                    angle_indicators = VGroup(right_angle_indicator, angle_indicator, angle_label)
                    right_triangle += angle_indicators
                else:
                    angle_indicators = VGroup(right_angle_indicator, angle_indicator)
                    right_triangle += angle_indicators
                    
            elif angle_position == "top":
                
                angle = round(np.arctan(base_length,height_length),3)
                angle_indicator = Angle(lines['hypotneuse'], lines['height_line'], radius = height_length/6, quadrant=(-1,-1), stroke_width=stroke_width, stroke_color=indicator_stroke_color)
                
                if add_angle_label == True:
                    angle_label_position = Angle(lines['hypotneuse'], lines['height_line'], radius = height_length/6 + angle_indicator.get_arc_length(), quadrant=(-1,-1)).point_from_proportion(0.5)
                    
                    if accurate_angle_label == True:
                        angle_label = MathTex(str(angle)).move_to(angle_label_position).scale_to_fit_height(angle_indicator.get_arc_length())
                    else:
                        angle_label = MathTex(r'\theta').move_to(angle_label_position).scale_to_fit_height(angle_indicator.get_arc_length())
                        
                    angle_indicators = VGroup(right_angle_indicator, angle_indicator, angle_label)
                    right_triangle += angle_indicators
                else:
                    angle_indicators = VGroup(right_angle_indicator, angle_indicator)
                    right_triangle += angle_indicators
            
            elif angle_position == "both":
                
                angle = [
                    round(np.arctan(height_length/base_length),3),
                    round(np.arctan(base_length/height_length),3)
                ]
                angle_indicator = [
                    Angle(lines['base_line'], lines['hypotneuse'], radius = base_length/6, stroke_width=stroke_width, stroke_color=indicator_stroke_color),
                    Angle(lines['hypotneuse'], lines['height_line'], radius = height_length/6, quadrant=(-1,-1), stroke_width=stroke_width, stroke_color=indicator_stroke_color)
                ]
                
                if add_angle_label == True:
                    angle_label_position = [
                        Angle(lines['base_line'], lines['hypotneuse'], radius = base_length/6 + angle_indicator[0].get_arc_length()).point_from_proportion(0.5),
                        Angle(lines['hypotneuse'], lines['height_line'], radius = height_length/6 + angle_indicator[1].get_arc_length(), quadrant=(-1,-1)).point_from_proportion(0.5)
                    ]
                    
                    if accurate_angle_label == True:
                        angle_label = [
                            MathTex(str(angle[0])).move_to(angle_label_position[0]).scale_to_fit_height(angle_indicator[0].get_arc_length()),
                            MathTex(str(angle[1])).move_to(angle_label_position[1]).scale_to_fit_height(angle_indicator[1].get_arc_length())
                        ]
                    else:
                        angle_label = [
                            MathTex(r'\theta').move_to(angle_label_position[0]).scale_to_fit_height(angle_indicator[0].get_arc_length()),
                            MathTex(r'\varphi').move_to(angle_label_position[1]).scale_to_fit_height(angle_indicator[1].get_arc_length())
                        ]
                    
                    angle_indicators = VGroup(right_angle_indicator, *angle_indicator, *angle_label)
                    right_triangle += angle_indicators
                else:
                    angle_indicators = VGroup(right_angle_indicator, *angle_indicator)
                    right_triangle += angle_indicators
            
        hypotneuse_length = np.sqrt(base_length**2 + height_length**2)
        side_lengths = {'base_length': base_length, 'height_length': height_length, 'hypotneuse_length': hypotneuse_length}
        
        #Instance variables   
        self.right_triangle = right_triangle #includes all submobjects of function
        self.triangle=triangle #Just the triangle
        self.side_labels=side_label_group
        self.angle_indicators=angle_indicators
        self.side_lengths = side_lengths
        self.angle=angle
        self.lines=lines
        self.vertices=vertices
        
        
        
    def animate_cartesian_coordinates(self):
        
        axes = Axes(
            x_range=[-3,3], 
            y_range=[-2,2],
            x_length=4,
            y_length=4,
            axis_config={'include_numbers': True},
        )
        axes.to_edge(UR,buff=0.75).shift(DOWN*0.45)
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")
        
        circle = Circle(radius = 0.5, color=GREEN, stroke_width=2.5)
        circle_center = axes.coords_to_point(1,0.5,0)
        circle_center_dot = Dot(circle_center, radius=0.05)
        circle.move_to(circle_center)
        
        radial_line = Line(circle_center, circle_center + 0.5*np.cos(PI/4)*RIGHT + 0.5*np.sin(PI/4)*UP, color=GREEN, stroke_width=1.5)
        radius_label = MathTex("r", color=GREEN, font_size=32).move_to(radial_line.point_from_proportion(0.5) + 0.1/np.sqrt(2)*UL)
        
        circle_equation = MathTex(r"(x-a)^2 + (y-b)^2 = r^2", font_size=32, color=GREEN).move_to(axes.get_top() + 3.1*DOWN)
        circle_equation.add_to_back(
            SurroundingRectangle(
                circle_equation, 
                color=DARK_GRAY, 
                corner_radius=0.1, 
                fill_opacity=1, 
                fill_color=DARK_GRAY
            )
        )
        
        no_sign = self.no_sign.move_to(axes.get_center())
        
        cartesian_group = VGroup(
            axes,
            axes_labels,
            circle,
            circle_center_dot,
            radial_line,
            radius_label,
            circle_equation,
            no_sign
        )
        
        
        self.play(
            LaggedStart(
                Write(axes),
                Write(axes_labels),
                Create(circle_center_dot),
                Write(circle),
                Write(radial_line),
                Write(radius_label),
                Write(circle_equation),
                lag_ratio=0.5
            )
        )
        self.play(DrawBorderThenFill(no_sign))
        
        #Instance variables
        self.cartesian_group=cartesian_group
        
    
    
    def clean_up_and_focus_on_pyramid(self):
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(self.pythagorean_group, self.cartesian_group)),
                Unwrite(VGroup(self.question_marks, self.truncated_pyramid_volume_expression)),
                self.pyramid_group.animate.move_to(ORIGIN).scale(2),
                lag_ratio=0.5
            )
        )
        
        
        
    def limit_toolset_animation(self):
        
        red_x = SVGMobject(f"{SVGImages}\\Red_X.svg").scale(1.5)
        red_x = VGroup(red_x.copy(), red_x.copy())
        
        trig_title = Tex(r"\large \underline{Trigonometry}").scale(0.75)
        trig_unit_circle = SVGMobject(f"{SVGImages}\\Unit_circle_trigonometry.svg").scale(2).next_to(trig_title, DOWN,buff=0).shift(0.5*RIGHT + 0.5*UP)
        trig = VGroup(
            trig_title,
            trig_unit_circle
        ).to_corner(UL).shift(0.5*DOWN)
        red_x[0].move_to(trig_title)
        
        calc_title = Tex(r"\large \underline{Calculus}").scale(0.75)
        calc_tex = MathTex(
            r"&\cdot f^\prime(x) = \lim_{dx \to 0} \frac{f(x+dx) - f(x)}{dx} \\\\"\
                r"&\cdot\iiint_V f(u,v,w) \,du\,dv\,dw"
        ).next_to(calc_title, DOWN, buff =0).scale(0.6).shift(0.4*UP)
        calc = VGroup(
            calc_title,
            calc_tex
        ).to_corner(UR).shift(0.5*DOWN)
        red_x[1].move_to(calc)
        red_x[0].align_to(red_x[1], DOWN)
        
        limit_toolset_group = VGroup(trig, calc, red_x)
        
        self.play(
            AnimationGroup(
                Write(trig_title),
                Create(trig_unit_circle)
            ),
            run_time=1.5
        )
        self.play(
            AnimationGroup(
                Write(calc_title),
                Create(calc_tex)
            ),
            run_time=1.5
        )
        self.wait()
        self.play(Create(red_x))
        self.wait()
        self.play(Unwrite(limit_toolset_group))
        
        
        
    def pyramid_to_video_toolset(self):
        
        title = Tex(r"\Large \underline{Toolset}")
        toolset_list = Tex(
            r"\begin{itemize}"\
                r"\item Natural numbers: $\mathbb{N}_1 = \{1,2,\ldots,\infty\}$"\
                    r"\item Natural numbers plus zero: $\mathbb{N}_0 = \{0,1,\ldots,\infty\}$"\
                        r"\item Rational fractions: $\mathbb{Q^+}$"
                        r"\item geometry"\
                            r"\item Arithmetic [e.g., $\pm, \times,\divisionsymbol, \ldots$]"\
                                r"\item Basic algebra"\
                                    r"\end{itemize}"                           
        ).next_to(title, DOWN, buff=0.5)
        
        toolset_group = VGroup(title, toolset_list)
        toolset_group += SurroundingRectangle(toolset_group, RED, buff=MED_SMALL_BUFF, corner_radius=0.2)
        toolset_group.move_to(ORIGIN)
        
        self.play(
            ShrinkToCenter(self.pyramid_group)
        )
        self.play(GrowFromCenter(toolset_group))
        self.wait()
        
        #Variable to be made public
        self.toolset_group=toolset_group
        
        
        
    def fade_to_black(self):
        
        self.play(FadeOut(self.toolset_group))

        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
