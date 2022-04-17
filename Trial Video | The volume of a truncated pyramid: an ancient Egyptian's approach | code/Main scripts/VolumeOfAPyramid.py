from manim import *
from CustomScripts.CustomShapes import *
from Introduction import *

class Scene3(ThreeDScene):
    def construct(self):
        
        ##Section 1
        self.next_section(skip_animations=False)
        self.show_section_title()
        self.wait()
        
        ##Section 2
        self.next_section(skip_animations=False)
        self.create_truncated_pyramid()
        self.wait()
        self.transform_pyramid()
        self.wait()
        self.play(FadeOut(self.labeled_pyramid))
        self.wait()
        
        ##Section 3
        self.next_section(skip_animations=False)
        self.right_triangle_area_animation()
        self.wait()
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        ##Section 4
        self.next_section(skip_animations=False)
        self.volume_of_a_pyramid_animation()
        self.wait()
    
    
    def show_section_title(self):
        
        section_title = MarkupText(f"The Volume Of A Pyramid", font_size=64, font="Times New Roman", gradient=[RED,YELLOW])
        
        self.play(FadeIn(section_title, run_time=1.5))
        self.wait()
        self.play(FadeOut(section_title, run_time=1.5))
        
    
    def create_truncated_pyramid(self):
        
        pyramid = Pyramid(2,1,3,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = YELLOW_B)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        vertices = pyramid.get_vertices()
        vertices.rotate(-PI/2,RIGHT)
        vertices.rotate(-PI/15,UP)
        vertices.rotate(PI/8,RIGHT)
        
        
        point1 = Line(*vertices[0:2]).point_from_proportion(0.4)
        
        point2 = pyramid.get_vertices()
        point2[-1].move_to([pyramid.major_base_length/2, 0, pyramid.vertical_height])
        point2.rotate(-PI/2,RIGHT)
        point2.rotate(-PI/15,UP)
        point2.rotate(PI/8,RIGHT)
        point2 = point2[-1]
        
        point3 = Line(*vertices[5:7]).point_from_proportion(0.5)
        
        

        height_arrow = Line(point1, point2, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(RED)
        dotted_line = DashedLine(height_arrow.get_end(), point3)

        base_arrow = Line(*vertices[3:5], stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
        
        top_arrow = Line(*vertices[8:10], stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(GREEN_E)
        arrow_group = VGroup(height_arrow, dotted_line, base_arrow, top_arrow)
        
        base_label = MathTex("b").move_to(base_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(rgb_to_color([0.2,0.2,1]))
        height_label = MathTex("h").move_to(height_arrow.point_from_proportion(0.5) + 0.3*UR).set_color(RED)
        top_label = MathTex("a").move_to(top_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(GREEN_E)
        label_group = VGroup(base_label, height_label, top_label)
        
        self.play(Write(pyramid))
        self.play(
            LaggedStart(
                Write(arrow_group),
                Write(label_group),
                lag_ratio=0.75
            )
        )
        
        #Instance variables
        labeled_truncated_pyramid = VGroup(pyramid, arrow_group, label_group)
        self.labeled_truncated_pyramid = labeled_truncated_pyramid
    
    
    def create_pyramid(self):
        pyramid = Pyramid(2,1,3,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = YELLOW_B, is_truncated=False)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        vertices = pyramid.get_vertices()
        vertices[-1].move_to([pyramid.major_base_length/2, 0, pyramid.vertical_height+0.1])
        vertices.rotate(-PI/2,RIGHT)
        vertices.rotate(-PI/15,UP)
        vertices.rotate(PI/8,RIGHT)
        
        point1 = Line(*vertices[0:2]).point_from_proportion(0.4)
        point2 = vertices[-1]

        height_arrow = Line(point1, point2, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(RED)

        base_arrow = Line(*vertices[3:5], stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
    
        arrow_group = VGroup(height_arrow, base_arrow)
        
        base_label = MathTex("b").move_to(base_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(rgb_to_color([0.2,0.2,1]))
        height_label = MathTex("h").move_to(height_arrow.point_from_proportion(0.5) + 0.3*UR).set_color(RED)
        label_group = VGroup(base_label, height_label)
        
        point = pyramid.get_vertices()
        point.rotate(-PI/2,RIGHT)
        point.rotate(-PI/15,UP)
        point.rotate(PI/8,RIGHT)
        point = point[-1]
        
        dotted_line = DashedLine(height_arrow.get_end(), point)
        arrow_group += dotted_line
        
        #instance variables
        labeled_pyramid = VGroup(pyramid, arrow_group, label_group)
        self.labeled_pyramid=labeled_pyramid
    
    
    def transform_pyramid(self):
        self.create_pyramid()
        
        self.play(ReplacementTransform(self.labeled_truncated_pyramid, self.labeled_pyramid))


    def right_triangle_area_animation(self):
        
        right_triangle = RightTriangle(2,1.5,stroke_color=RED, stroke_width=2.5)
        labels = right_triangle.generate_labels(
            side_labels={'base_label': "a", 'height_label': "b", 'hypotneuse_label': "c"}, 
            angle_position="both", 
            font_size=56, 
            angle_label_font_size=36
        )
        triangle_group = VGroup(right_triangle, labels).move_to(0.3*DR)
        
        triangle_duplicate = RightTriangle(-2, -1.5,stroke_color=RED, stroke_width=2.5)
        triangle_duplicate_labels = triangle_duplicate[0].generate_labels(
            side_labels={'base_label': "a", 'height_label': "b", 'hypotneuse_label': ""}, 
            angle_position="both", 
            font_size=56, 
            angle_label_font_size=36
        )
        triangle_duplicate_group = VGroup(triangle_duplicate, triangle_duplicate_labels).move_to(right_triangle.get_center() + 0.75*UL)
        
        self.play(Write(triangle_group))
        self.wait()
        self.play(ReplacementTransform(triangle_group.copy(), triangle_duplicate_group), FadeOut(right_triangle.labels[0][2], run_time=0.5))
        self.wait()
        self.play(triangle_duplicate_group.animate.shift(0.42*DR).shift(0.01*UR))
        self.wait()
        self.play(
            FadeOut(
                labels[1],
                triangle_duplicate_labels[1]
            ),
            run_time=1,
            wait_time=0.5
        )
        self.play(Circumscribe(SurroundingRectangle(VGroup(right_triangle,triangle_duplicate), buff=-0.1)))
        self.wait()
        
        rectangle_area_text = MathTex(r"{{Area_{rectangle}}}={{ab}}", font_size = 36).move_to(right_triangle.get_center() + 4*RIGHT)
        rectangle_text = rectangle_area_text[0][4:]
        rt_text = VGroup(rectangle_area_text[0][4], rectangle_area_text[0][7].copy().shift(0.275*LEFT))
        rectangle_area_text[1:].next_to(rectangle_area_text[0][0:4], RIGHT, buff=0.3)
        ab_text = rectangle_area_text[2]
        
        self.play(Write(rectangle_area_text[0]))
        self.wait()
        self.play(Transform(rectangle_text, rt_text))
        self.play(
            FadeIn(rectangle_area_text[1]),
            ReplacementTransform(
                labels.copy()[0][:-1],
                ab_text
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                FadeOut(rectangle_area_text, shift=DOWN),
                AnimationGroup(
                    FadeOut(triangle_duplicate_labels[0]),
                    Unwrite(triangle_duplicate)
                ),
                Write(labels[1]),
                lag_ratio=0.5
            )
        )
        
        triangle_area_text = MathTex(r"{{Area_{triangle}}}=\frac{1}{2}", font_size = 36).to_edge(LEFT, buff=1)
        triangle_area_text[1:].shift(0.8*LEFT)
        triangle_text = triangle_area_text[0][4:]
        tr_text = triangle_text[0:2]
        rectangle_area_text.next_to(triangle_area_text[1:], buff=0.1).shift(0.05*DOWN)
        ab_text.next_to(triangle_area_text[1:], buff=0.1).shift(0.02*UP)
        
        self.play(Write(triangle_area_text[0]))
        self.wait()
        self.play(Transform(triangle_text, tr_text))
        self.play(
            FadeIn(
                triangle_area_text[1],
                rectangle_area_text[0],
                shift=RIGHT
            )
        )
        self.wait()
        self.play(
            ReplacementTransform(
                rectangle_area_text[0],
                ab_text
            )
        )
        
        
    def volume_of_a_pyramid_animation(self):
        
        pyramid_template = Pyramid(
            is_truncated=False, 
            major_base_length=1, 
            vertical_height=0.5,
            stroke_width=1,
            stroke_color=DARK_BLUE,
            fill_color=YELLOW_B,
            fill_opacity=1,
        )
        
        pyr = pyramid_template.copy()
        
        pyr_vertices = pyr.get_vertices()
        point1 = Line(*pyr_vertices[:2]).point_from_proportion(0.5)
        point2 = pyr_vertices[-1].copy().shift(pyr.major_base_length/2*RIGHT + 0.05*IN)
        
        base_arrow = Line(*pyr_vertices[3:5]).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
        base_arrow.get_tips().rotate(13*PI/30, RIGHT)
        
        height_arrow = Line(point1, point2).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1).set_color(RED)
        height_arrow.get_tips()[0].rotate(PI/2,RIGHT).move_to(height_arrow.get_end()).shift(0.05*DOWN)
        height_arrow.rotate(PI/10,OUT)
        dotted_line = DashedLine(height_arrow.get_end(), pyr_vertices[-1])
        
        arrow_group = VGroup(base_arrow, height_arrow, dotted_line)
        
        base_label = MathTex(r"b", font_size=24).move_to(base_arrow.point_from_proportion(0.5) + 0.15*IN)\
            .rotate(13*PI/30, RIGHT).rotate(PI/10,OUT).set_color(rgb_to_color([0.2,0.2,1]))
        
        height_label = MathTex(r"h", font_size=24).move_to(height_arrow.point_from_proportion(0.5) + 0.15*RIGHT)\
            .rotate(13*PI/30, RIGHT).rotate(PI/10,OUT).set_color(RED)
            
        label_group = VGroup(base_label, height_label)
        
        pyr1 = pyramid_template.copy().next_to(pyr,RIGHT)#.rotate(-PI/2,Y_AXIS).shift(LEFT+0.25*OUT)
        pyr2 = pyramid_template.copy().next_to(pyr,LEFT).rotate(PI/2,Y_AXIS)#.shift(RIGHT+0.25*OUT)
        pyr3 = pyramid_template.copy().next_to(pyr,UP).rotate(PI/2,X_AXIS)#.shift(DOWN+0.25*OUT)
        pyr4 = pyramid_template.copy().next_to(pyr,DOWN).rotate(-PI/2,X_AXIS)#.shift(UP+0.25*OUT)
        pyr5 = pyramid_template.copy().next_to(pyr,OUT*2)#.rotate(PI,X_AXIS).shift(IN*0.25)
        
        copy_prisms = VGroup(pyr1,pyr2,pyr3,pyr4,pyr5)
        
        
        self.set_camera_orientation(13*PI/30,-2*PI/5,zoom=2)
        self.play(Write(pyr))
        self.play(
            LaggedStart(
                Write(arrow_group),
                Write(label_group),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(FadeOut(arrow_group, label_group))
        self.move_camera(zoom=1, frame_center=OUT)
        self.begin_ambient_camera_rotation(PI/5,about="theta")
        self.wait()
        
        self.play(ReplacementTransform(pyr.copy(),pyr1))
        self.play(Rotate(pyr1,-PI/2,Y_AXIS))
        self.play(pyr1.animate.shift(0.25*OUT+LEFT))
        
        self.play(ReplacementTransform(pyr.copy(),pyr2), run_time=1.5)
        self.play(pyr2.animate.shift(0.25*OUT+RIGHT))
        
        self.play(ReplacementTransform(pyr.copy(),pyr3), run_time=1.5)
        self.play(pyr3.animate.shift(0.25*OUT+DOWN))
        
        self.play(ReplacementTransform(pyr.copy(),pyr4), run_time=1.5)
        self.play(pyr4.animate.shift(0.25*OUT+UP))
        
        self.play(ReplacementTransform(pyr.copy(),pyr5), run_time=1.5)
        self.play(Rotate(pyr5, PI,X_AXIS))
        self.play(pyr5.animate.shift(0.5*IN))
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(13*PI/30,-2*PI/5, zoom=1.5)
        
        pyr_cube = VGroup(copy_prisms, pyr)
        cube_base_brace = BraceLabel(pyr_cube, "b", DOWN, buff=0.6)
        cube_base_brace[1].set_color(rgb_to_color([0.2,0.2,1])).shift(0.1*UP)
        cube_height_brace = BraceLabel(pyr_cube, r"{{2h}}", DOWN, buff=0.6)
        cube_height_brace[1].set_color(RED)
        
        cube_braces = VGroup(cube_base_brace, cube_base_brace.copy(), cube_height_brace)
        
        self.add_fixed_in_frame_mobjects(*cube_braces[:-1])
        cube_braces[0].shift(0.25*LEFT + 0.6*DOWN)
        cube_braces[0][0].scale(1.45).rotate(-PI/30)
        cube_braces[1][1].shift(0.2*UP + 0.1*RIGHT)
        cube_braces[1].shift(0.775*RIGHT + 0.35*DOWN)
        cube_braces[1][0].scale(0.45*1.4).rotate(9*PI/40)
        
        self.play(Write(VGroup(*cube_braces[:2])))
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(pyr1, shift=RIGHT),
                FadeOut(pyr2, shift=LEFT),
                FadeOut(pyr3, shift=UP),
                FadeOut(pyr4, shift=DOWN),
            )
        )
        self.wait()
        
        self.add_fixed_in_frame_mobjects(cube_braces[-1])
        cube_braces[2][0].scale(1.45).rotate(PI/2)
        cube_braces[2][1].shift(0.55*RIGHT + 0.55*UP)
        cube_braces[2].shift(1.15*RIGHT + 0.6*UP)
        
        self.play(Write(cube_braces[-1]))
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(pyr1, shift=LEFT),
                FadeIn(pyr2, shift=RIGHT),
                FadeIn(pyr3, shift=DOWN),
                FadeIn(pyr4, shift=UP),
            )
        )
        self.wait()
        
        cube_volume_text = MathTex(r"Volume_{Cube}=2b^2h")
        
        self.add_fixed_in_frame_mobjects(cube_volume_text.to_corner(UL, buff=1.5))
        self.play(Write(cube_volume_text))
        self.wait()
        self.play(
                AnimationGroup(
                    FadeOut(pyr1, shift=RIGHT),
                    FadeOut(pyr2, shift=LEFT),
                    FadeOut(pyr3, shift=UP),
                    FadeOut(pyr4, shift=DOWN),
                    FadeOut(pyr5, shift=OUT),
                    FadeOut(VGroup(pyr, *cube_braces)),
                    Unwrite(cube_volume_text, run_time=1),
                )
        )
        self.set_camera_orientation(13*PI/30,-2*PI/5,zoom=2, frame_center=ORIGIN)
        self.play(Write(pyr))
        self.play(
            LaggedStart(
                Write(arrow_group),
                Write(label_group),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        pyr_volume_text = MathTex(r"V_P={{\frac{V_C}{6}}}")
        cube_volume_equation = MathTex(r"\frac{1}{6}{{\cdot2b^2h}}")
        frac_text = MathTex(r"\frac{1}{3}")
        self.add_fixed_in_frame_mobjects(pyr_volume_text.to_corner(UL, buff=0.5))
        self.play(Write(pyr_volume_text))
        self.wait()
        self.add_fixed_in_frame_mobjects(cube_volume_equation.next_to(pyr_volume_text[0], RIGHT, buff=0.1))
        self.play(
            LaggedStart(
                ShrinkToCenter(pyr_volume_text[1]),
                GrowFromCenter(cube_volume_equation),
                lag_ratio=0.2
            )
        )
        self.wait()
        
        self.add_fixed_in_frame_mobjects(frac_text.next_to(pyr_volume_text[0], RIGHT, buff=0.1))
        self.play(
            LaggedStart(
                FadeOut(VGroup(cube_volume_equation[0], cube_volume_equation[1][:2]), shift=DOWN),
                AnimationGroup(
                FadeIn(frac_text, shift=DOWN),
                cube_volume_equation[1][2:].animate.next_to(frac_text, RIGHT, buff=0.1)
                ),
                lag_ratio=0.5
            ) 
        )
        self.wait()
        pyr_volume_group = VGroup(pyr_volume_text, frac_text, cube_volume_equation[1][2:])
        self.play(
            LaggedStart(
                Unwrite(VGroup(pyr, arrow_group, label_group)),
                pyr_volume_group.animate.shift(5*RIGHT, 3*DOWN).scale(2),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Unwrite(pyr_volume_group))
        
        

class Scene4(ThreeDScene):
    def construct(self):
        
        ##Section 1
        self.next_section(skip_animations=False)
        self.show_section_title()
        self.wait()
        
        ##Section 2
        self.next_section(skip_animations=False)
        self.create_truncated_pyramid()
        self.wait()
        self.show_missing_pyramid()
        self.wait()
        self.fade_all()
        self.wait()
        
        ##Section 3
        self.next_section(skip_animations=False)
        self.draw_2D_projection()
        self.wait()
        self.animate_2D_derivations()
        self.wait()
        
        ##Section 4
        self.next_section(skip_animations=False)
        self.create_final_scene()
        self.wait()
        
    
    def show_section_title(self):
        section_title = MarkupText(f"The Volume Of A Truncated Pyramid", font_size=64, font="Times New Roman", gradient=[RED,YELLOW])
        
        self.play(FadeIn(section_title, run_time=1.5))
        self.wait()
        self.play(FadeOut(section_title, run_time=1.5))
        
    
    def create_truncated_pyramid(self):
        
        pyramid = Pyramid(2,1,2,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = YELLOW_B)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        
        
        self.play(Write(pyramid))
        
        #Instance variables
        self.truncated_pyramid = pyramid
        
    
    def show_missing_pyramid(self):
        
        pyramid = Pyramid(1,1,2,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = ORANGE, is_truncated=False)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        pyramid.next_to(self.truncated_pyramid, UP,buff=0).shift(OUT + 0.47*DOWN)
        self.play(FadeIn(pyramid))
        self.wait()
        self.play(FadeOut(pyramid))
        
        #instance variables
        self.pyramid=pyramid
        
    
    def fade_all(self):
        self.play(FadeOut(*self.mobjects))
        
        
    def draw_2D_projection(self):
        
        truncated_pyramid_vertices = [
            2*DOWN + 2*LEFT,
            2*DOWN + 2*RIGHT,
            UP + RIGHT,
            UP + LEFT
        ]
        
        missing_pyramid_vertices = [
            truncated_pyramid_vertices[-1],
            truncated_pyramid_vertices[-2],
            3*UP
        ]
        
        truncated_pyramid_shadow = Polygon(*truncated_pyramid_vertices, fill_color=YELLOW_B, fill_opacity=1, stroke_color=DARK_BLUE, stroke_width=2.5)
        missing_pyramid_shadow = Polygon(*missing_pyramid_vertices, fill_color = ORANGE, fill_opacity=1, stroke_color=RED, stroke_width=2.5)
        
        self.play(DrawBorderThenFill(truncated_pyramid_shadow), run_time=1.5)
        self.play(DrawBorderThenFill(missing_pyramid_shadow), run_time=1.5)
        self.wait()
        self.play(
            AnimationGroup(
                truncated_pyramid_shadow.animate.set_fill(opacity=0),
                missing_pyramid_shadow.animate.set_fill(opacity=0)
            )
        )
        
        #Instance_variables
        self.truncated_pyramid_vertices=truncated_pyramid_vertices
        self.missing_pyramid_vertices=missing_pyramid_vertices
        self.truncated_pyramid_shadow=truncated_pyramid_shadow
        self.missing_pyramid_shadow=missing_pyramid_shadow
        
        
    def animate_2D_derivations(self):
        
        truncated_pyramid_base_arrow = Line(*self.truncated_pyramid_vertices[:2])\
            .add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
        truncated_pyramid_base_label = MathTex(r"b", font_size=36)\
            .move_to(truncated_pyramid_base_arrow.point_from_proportion(0.5) + 0.25*DOWN).set_color(rgb_to_color([0.2,0.2,1]))
        
        point1 = Dot(self.truncated_pyramid_vertices[2], radius=0)
        point2 = point1.copy().shift(3*DOWN)
        truncated_pyramid_height_arrow1 = DashedLine(point1, point2, stroke_width=2.5)
        
        point3 = Dot(self.truncated_pyramid_vertices[-1], radius=0)
        point4 = point3.copy().shift(3*DOWN)
        truncated_pyramid_height_arrow2 = DashedLine(point3, point4, stroke_width=2.5)
        
        truncated_pyramid_height_arrows = VGroup(
            truncated_pyramid_height_arrow1,
            truncated_pyramid_height_arrow2
        )
        
        
        tick_mark1 = Line(0.1*LEFT, 0.1*RIGHT, stroke_width=2.5).move_to(Line(point1,point2).point_from_proportion(0.5))
        tick_mark2 = tick_mark1.copy().move_to(Line(point3,point4).point_from_proportion(0.5))
        
        height_tick_marks = VGroup(tick_mark1, tick_mark2)
        
        
        missing_pyramid_base_arrow = Line(*self.missing_pyramid_vertices[:2], stroke_width=2.5)\
            .add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1).set_color(PURPLE)
        missing_pyramid_base_label = MathTex(r"a", font_size=36)\
            .move_to(missing_pyramid_base_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(PURPLE)
        
        
        point5 = Line(*self.missing_pyramid_vertices[:2]).point_from_proportion(0.5)
        point6 = self.missing_pyramid_vertices[-1]
        missing_pyramid_height_arrow = DashedLine(point5, point6, stroke_width = 2.5)
        
        truncate_pyramid_height_label = BraceLabel(self.truncated_pyramid_shadow, "h",LEFT, font_size=36)\
            .shift(0.2*RIGHT)
        truncate_pyramid_height_label[1].set_color(RED)
        
        
        missing_pyramid_height_label = BraceLabel(self.missing_pyramid_shadow, "h_t", LEFT, font_size=36)\
            .shift(0.8*LEFT)
        missing_pyramid_height_label[1].set_color(RED)
        
        
        base_tick_mark1 = VGroup(
            Line(0.1*UP, 0.1*DOWN, stroke_width=2.5).shift(0.05*LEFT),
            Line(0.1*UP, 0.1*DOWN, stroke_width=2.5).shift(0.05*RIGHT)
        ).move_to(missing_pyramid_base_arrow.point_from_proportion(0.5))
        base_tick_mark2 = base_tick_mark1.copy().move_to(Line(point2, point4).point_from_proportion(0.5))
        
        base_tick_marks = VGroup(base_tick_mark1, base_tick_mark2)
        
        
        top_sub_line = Line(point5, self.missing_pyramid_vertices[1])
        bottom_sub_line = Line(point2, self.truncated_pyramid_vertices[1])
        
        top_sub_label = BraceLabel(top_sub_line, r"\frac{a}{2}", font_size=36, buff=0)
        top_sub_label[1].shift(0.2*UP)
        bottom_sub_label = BraceLabel(bottom_sub_line, r"\frac{b}{2}-\frac{a}{2}", font_size=36, buff=0)
        bottom_sub_label[1].shift(0.2*UP)
        
        bottom_sub_label_text_replacement = MathTex(r"\frac{b-a}{2}", font_size=36).move_to(bottom_sub_label[1])
        
        self.play(
            LaggedStart(
                Write(truncated_pyramid_base_arrow),
                Write(truncated_pyramid_base_label),
                Write(missing_pyramid_base_arrow),
                Write(missing_pyramid_base_label),
                lag_ratio=0.75
            )
        )
        self.wait()
        self.play(Write(truncate_pyramid_height_label))
        self.wait()
        self.play(Write(missing_pyramid_height_label))
        self.wait()
        
        volume_expression1 = MathTex(r"{{V_{P^\dagger}}} = {{V_P}} - {{V_{P^\prime}}}")\
            .to_edge(UR, buff=1.5).shift(LEFT)
            
        full_pyramid_volume = MathTex(r"\frac{b^2(h+h_t)}{3}", font_size=36).next_to(volume_expression1[1], RIGHT, buff=0.1)
        
        self.play(Write(volume_expression1[0]))
        self.play(
            LaggedStart(
                Write(volume_expression1[1]),
                Write(volume_expression1[2]),
                lag_ratio=0.5
            )
        )
        self.play(
            LaggedStart(
                Write(volume_expression1[3]),
                Write(volume_expression1[4]),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    volume_expression1[2],
                    full_pyramid_volume
                ),
                volume_expression1[3:].animate.next_to(full_pyramid_volume, RIGHT, buff=0.1)
            )
        )
        self.wait()
        
        missing_pyramid_volume = MathTex(r"\frac{a^2h_t}{3}", font_size=36).next_to(volume_expression1[3], RIGHT, buff=0.1)
        
        self.play(
            ReplacementTransform(
                volume_expression1[4],
                missing_pyramid_volume
            )
        )
        self.wait()
        
        volume_expression2 = MathTex(r"\frac{1}{3}{{(b^2(h+h_t) - a^2h_t)}}").scale(0.75).next_to(volume_expression1[1], RIGHT, buff=0.1)
        
        self.play(
            ReplacementTransform(
                VGroup(full_pyramid_volume, volume_expression1[3], missing_pyramid_volume),
                volume_expression2
            )
        )
        self.wait()
        
        volume_expression3 = MathTex(r"{{h}} + {{b^2h_t}}").scale(0.75).next_to(volume_expression2[1][1], RIGHT, buff=0.2)
        volume_expression4 = MathTex(r"({{b^2}} - {{a^2}})").scale(0.75).next_to(volume_expression3[1], RIGHT, buff=0.1)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    volume_expression2[1][3:9],
                    volume_expression3
                ),
                volume_expression2[1][9:].animate.next_to(volume_expression3, RIGHT, buff=0.1)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(
                VGroup(volume_expression3[2], volume_expression2[1][9:-3]),
                volume_expression4
                ),
                volume_expression2[1][-3:].animate.next_to(volume_expression4, RIGHT, buff=0.1)
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                Circumscribe(volume_expression2[1][1]),
                Circumscribe(volume_expression4[1])
            )
        )
        self.wait()
        self.play(Circumscribe(volume_expression4[3]))
        self.wait()
        self.play(Circumscribe(volume_expression3[0]))
        self.wait(2)
        self.play(Circumscribe(volume_expression2[1][-2:-1], color = RED, buff=0.2))
        self.wait(5)
        
        self.play(Write(truncated_pyramid_height_arrows))
        self.play(Write(missing_pyramid_height_arrow), run_time=1)
        self.play(Write(height_tick_marks))
        self.play(Write(base_tick_marks))
        self.wait()
        
        self.play(Circumscribe(top_sub_line))
        self.wait()
        self.play(
            AnimationGroup(
                Write(top_sub_label),
                missing_pyramid_base_label.animate.shift(0.2*LEFT)
            )
        )
        self.wait(2)
        
        line1 = Line(truncated_pyramid_base_arrow.point_from_proportion(0.5), point2)
        length_expression1 = MathTex(r"\frac{b}{2}", font_size=36).next_to(line1.point_from_proportion(0.5), UP, buff = 0.2)
        
        self.play(Circumscribe(line1))
        self.wait()
        self.play(FadeIn(length_expression1))
        self.wait()
        self.play(FadeOut(length_expression1))
        self.play(Write(bottom_sub_label))
        self.wait()
        self.play(ReplacementTransform(bottom_sub_label[1], bottom_sub_label_text_replacement))
        self.wait(5)
        
        top_sub_triangle = Polygon(point5, *self.missing_pyramid_vertices[1:])
        bottom_sub_triangle = Polygon(point2.get_center(), *self.truncated_pyramid_vertices[1:3])
        
        gradient_label = BraceLabel(Line(self.truncated_pyramid_vertices[1], self.missing_pyramid_vertices[-1]), r"m", brace_direction=RIGHT, font_size=36)\
            .set_color(YELLOW).shift(0.8*LEFT + 0.2*UP)
        gradient_label[0].rotate(PI/2 - np.arctan(3)+0.1).scale(1.1)
        
        gradient_text = MathTex(r"={{\frac{rise}{run}}}",font_size=36).set_color(YELLOW).next_to(gradient_label[1], RIGHT, buff=0.1).shift(0.05*UP)
        
        grad1 = MathTex(r"\frac{h_t}{(\frac{a}{2})}", font_size=36).set_color(YELLOW).next_to(gradient_text[0], RIGHT, buff=0.1)
        grad2 = MathTex(r"={{\frac{h}{(\frac{b-a}{2})}}}", font_size=36).set_color(YELLOW).next_to(grad1, RIGHT, buff=0.1)
        grad2[0].shift(0.05*DOWN)
        
        self.play(Circumscribe(bottom_sub_triangle, buff=0, shape=Rectangle))
        self.wait()
        self.play(Circumscribe(top_sub_triangle, buff=0, shape=Rectangle))
        self.wait()
        self.play(Write(gradient_label))
        self.wait()
        self.play(Write(gradient_text))
        self.wait()
        self.play(ReplacementTransform(gradient_text[1], grad1))
        self.wait()
        self.play(Write(grad2))
        self.play(FadeOut(gradient_label, gradient_text[0]))
        self.wait()
        
        grad3 = MathTex(r"\frac{2h_t}{a}", font_size=36).set_color(YELLOW).next_to(gradient_text[0], RIGHT, buff=0.1)
        grad4 = MathTex(r"\frac{2h}{b-a}", font_size=36).set_color(YELLOW).next_to(grad2[0], RIGHT, buff=0.1).shift(0.05*UP)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(grad1, grad3),
                ReplacementTransform(grad2[1], grad4)
            )
        )
        self.wait()
        
        grad5 = MathTex(r"h_t = \frac{ah}{b-a}", font_size=36).set_color(YELLOW).next_to(gradient_text[0], RIGHT, buff=0.1)\
            .shift(UP*0.05)
        
        self.play(
            ReplacementTransform(
                VGroup(
                    grad2[0], 
                    grad3, 
                    grad4
                ),
                grad5
            )
        )
        self.wait()
        self.play(grad5.animate.to_corner(UL, buff=1.5))
        
        equation1 = VGroup(volume_expression4, volume_expression2[1][-3:-1]).copy().next_to(grad5, DOWN, buff=0.5).to_edge(LEFT, buff=0.1)\
            .set_color(GREEN).scale(28/36)
        equation2 = MathTex(r"={{(b+a)(b-a)h_t}}", font_size=28).next_to(equation1, RIGHT, buff=0.1).set_color(GREEN)
        equation3 = MathTex(r"\frac{ah}{b-a}", font_size=28).next_to(equation2[1][-3], RIGHT, buff=0.1).set_color(GREEN)
        
        self.play(
            ReplacementTransform(
                VGroup(volume_expression4, volume_expression2[1][-3:-1]).copy(), equation1
            )
        )
        self.wait()
        self.play(Write(equation2))
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    grad5.copy(),
                    equation3
                ),
                FadeOut(equation2[1][-2:], run_time=0.5)
            )
        )
        self.wait()
        
        equation4 = MathTex(r"a{{h}}", font_size=28).set_color(GREEN).next_to(equation2[1][4], RIGHT, buff=0.1)
        
        self.play(
            ReplacementTransform(
                VGroup(equation2[1][5:10], equation3),
                equation4
            )
        )
        self.wait()
        
        equation5 = MathTex(r"(ab+a^2)", font_size=28).set_color(GREEN).next_to(equation4[1], LEFT, buff=0)
        
        self.play(
            ReplacementTransform(
                VGroup(equation2[1][:5], equation4[0]),
                equation5
            )
        )
        self.wait()
        
        equation6 = MathTex(r"(ab+a^2){{h}}", font_size=36).next_to(volume_expression3[1], RIGHT, buff=0.1)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    VGroup(equation4[1], equation5).copy(),
                    equation6
                ),
                equation4[1].animate.shift(0.1*RIGHT),
                FadeOut(VGroup(volume_expression4, volume_expression2[1][-3:-1])),
                volume_expression2[1][-1].animate.next_to(equation6, RIGHT, buff=0.1)
                
            )
        )
        self.wait(2)
        
        old_expression = VGroup(
            volume_expression1[0:2], 
            volume_expression2[0], 
            volume_expression2[1][0:3],
            volume_expression3[0:2],
            equation6,
            volume_expression2[1][-1]
        )
        final_volume_expression = MathTex(r"{{V_{P^\dagger}}}=\frac{h}{3}(b^2 + ab + a^2)", font_size=36).to_corner(UR, buff=1.5)
        
        self.play(ReplacementTransform(old_expression, final_volume_expression))
        self.wait()
        
        self.fade_all()
        
        
    def create_final_scene(self):
        
        pyramid = Pyramid(2,1,3,stroke_width=1,fill_opacity=1,stroke_color=DARK_BLUE, fill_color = YELLOW_B)
        pyramid.rotate(-PI/2,RIGHT)
        pyramid.rotate(-PI/15,UP)
        pyramid.rotate(PI/8,RIGHT)
        
        vertices = pyramid.get_vertices()
        vertices.rotate(-PI/2,RIGHT)
        vertices.rotate(-PI/15,UP)
        vertices.rotate(PI/8,RIGHT)
        
        
        point1 = Line(*vertices[0:2]).point_from_proportion(0.4)
        
        point2 = pyramid.get_vertices()
        point2[-1].move_to([pyramid.major_base_length/2, 0, pyramid.vertical_height])
        point2.rotate(-PI/2,RIGHT)
        point2.rotate(-PI/15,UP)
        point2.rotate(PI/8,RIGHT)
        point2 = point2[-1]
        
        point3 = Line(*vertices[5:7]).point_from_proportion(0.5)
        
        

        height_arrow = Line(point1, point2, stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(RED)
        dotted_line = DashedLine(height_arrow.get_end(), point3)

        base_arrow = Line(*vertices[3:5], stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(rgb_to_color([0.2,0.2,1]))
        
        top_arrow = Line(*vertices[8:10], stroke_width=1.5).add_tip(tip_length=0.1, at_start=True).add_tip(tip_length=0.1).set_color(GREEN_E)
        arrow_group = VGroup(height_arrow, dotted_line, base_arrow, top_arrow)
        
        base_label = MathTex("b").move_to(base_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(rgb_to_color([0.2,0.2,1]))
        height_label = MathTex("h").move_to(height_arrow.point_from_proportion(0.5) + 0.3*UR).set_color(RED)
        top_label = MathTex("a").move_to(top_arrow.point_from_proportion(0.5) + 0.2*DOWN).set_color(GREEN_E)
        label_group = VGroup(base_label, height_label, top_label)
        
        truncated_pyramid_group = VGroup(pyramid, arrow_group, label_group).to_edge(UP, buff=1)
        
        self.play(Write(pyramid))
        self.play(
            LaggedStart(
                Write(arrow_group),
                Write(label_group),
                lag_ratio=0.75
            )
        )
        self.wait(2)
        
        volume_expression = MathTex(r"V_{P^\dagger}=\frac{h}{3}(b^2 + ab + a^2)").next_to(truncated_pyramid_group, DOWN)
        underline = Underline(volume_expression, color=YELLOW)
        underline2 = Underline(underline, color=YELLOW)
        
        self.play(Write(volume_expression))
        self.play(LaggedStart(Write(underline), Write(underline2), lag_ratio=0.5))
        self.wait(5)
        self.play(
            LaggedStart(
                Unwrite(VGroup(underline, underline2)),
                Unwrite(volume_expression),
                Unwrite(truncated_pyramid_group),
                lag_ratio=0.5
            )
        )
        


# class Conclusion(Scene):
#     def construct(self):
#         return
        
        
        
        
        
        
        
        
        
# class Test(ThreeDScene):
#     def construct(self):
        
#         text = Tex(r"The equations work for all \\ $values > 0$!!!")
        
#         self.play(Write(text))
#         self.wait(5)
        
        
        
     
        