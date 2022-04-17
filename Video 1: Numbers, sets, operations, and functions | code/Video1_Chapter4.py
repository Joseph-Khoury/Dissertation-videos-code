from manim import *

SVGImages = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\SVGImages"
Images = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\Images"

class MainScene(Scene):
    
    def create_func_machine(
        self,
        color: str = RED,
        text: str = r"f(x)",
        text_color: str = None,
        scale=0.6,
        **kwargs
    ):
        func_machine = Polygon(
            DL,
            DR,
            UR,
            UL,
            DL,
            0.5*UP + LEFT,
            0.75*(UP + 2*LEFT),
            0.75*(DOWN + 2*LEFT),
            0.5*DOWN + LEFT,
            DL,
            DR,
            0.5*UP + RIGHT,
            0.75*(UP + 2*RIGHT),
            0.75*(DOWN + 2*RIGHT),
            0.5*DOWN + RIGHT,
            DR,
            DL,
            color=color,
            **kwargs
        ).scale(scale)
        if text_color == None:
            func_machine_text = MathTex(text, color=color).move_to(func_machine.get_center())
        else:
            func_machine_text = MathTex(text, color=text_color).move_to(func_machine.get_center())
        return VGroup(func_machine, func_machine_text)
    
    def construct(self):
        
        ##Section 1
        self.next_section(name="Function machine", skip_animations=False)
        func_machine = self.create_func_machine(color=GRAY, text_color=YELLOW)
        func_left = func_machine.get_left() + 0.1*LEFT
        func_right = func_machine.get_right() + 0.1*RIGHT
        
        domain_set = VGroup(Ellipse(width=2, height=3, color=GREEN, fill_opacity=0.5).next_to(func_machine, LEFT, buff=1.2))
        domain_set.add(MathTex(r"Domain", color=GREEN).next_to(domain_set, UP, buff=0.2))
        domain_arrow = Line(
            start=func_left + LEFT,
            end=func_left,
        ).add_tip()
        
        range_set = VGroup(domain_set[0].copy().set_color(RED).next_to(func_machine, RIGHT, buff=1.2))
        range_set.add(MathTex(r"Range", color=RED).next_to(range_set, UP, buff=0.2))
        range_arrow = Line(
            start=func_right,
            end=func_right + RIGHT
        ).add_tip()

        self.play(Write(func_machine))
        self.wait(2)
        
        domain_set_dud = domain_set.copy()
        domain_arrow_dud = domain_arrow.copy()
        range_arrow_dud = range_arrow.copy()
        
        self.play(Write(VGroup(domain_set_dud[0], range_set[0])))
        self.wait(2)
        self.play(
            LaggedStart(
                Write(domain_arrow_dud),
                Write(domain_set_dud[1]),
                lag_ratio=1
            )
        )
        self.wait(2)
        self.play(
            LaggedStart(
                Write(range_arrow_dud),
                Write(range_set[1]),
                lag_ratio=1
            )
        )
        self.wait(2)
        
        func_center = Dot(func_machine.get_center(), radius=0.3, stroke_opacity=0, fill_opacity=0)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(domain_set_dud, func_center),
                FadeOut(domain_arrow_dud, shift=RIGHT)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(func_center, range_set),
                FadeOut(range_arrow_dud, shift=RIGHT)
            )
        )
        self.wait(2)
        self.play(FadeIn(domain_set, domain_arrow, range_arrow))
        self.wait(2)
        self.play(Circumscribe(func_machine))
        self.wait(2)
        self.play(Indicate(func_machine[1]))
        self.wait()
        self.play(Indicate(VGroup(domain_set, range_set)))
        self.wait(5)
        
        ##Section 2
        self.next_section(name="Function map", skip_animations=False)
        f_map = Line(
            start=domain_set[0].get_center() + 0.2*UR,
            end=range_set[0].get_center() + 0.2*UL,
            path_arc=-1
        ).add_tip()
        f_text = MathTex(r"f").move_to(f_map.point_from_proportion(0.5) + 0.5*UP)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(VGroup(domain_arrow, range_arrow, func_machine[0]), f_map),
                ReplacementTransform(func_machine[1], f_text)
            )
        )
        self.wait(5)
        
        ##Section 3
        self.next_section(name="Differences between the machine and map representations", skip_animations=False)
        self.play(FadeOut(*self.mobjects))
        
        func_machine_expression = MathTex(r"{{y}}={{f(x)}}", font_size=64)
        y = func_machine_expression[0]
        is_a_function_of = VGroup(func_machine_expression[1], func_machine_expression[2][:2], func_machine_expression[2][-1])
        x = func_machine_expression[2][2]
        self.play(Write(func_machine_expression))
        self.wait(2)
        self.play(Indicate(y))
        self.play(Indicate(is_a_function_of))
        self.play(Indicate(x))
        self.wait(2)
        
        func_map_expression = MathTex(r"{{f:}}{{x}} \mapsto {{y}}", font_size=64)
        f_is_a_map = VGroup(func_map_expression[0], func_map_expression[2])
        x = func_map_expression[1]
        y = func_map_expression[3]
        self.play(ReplacementTransform(func_machine_expression, func_map_expression))
        self.wait(2)
        self.play(Indicate(f_is_a_map))
        self.play(Indicate(x))
        self.play(Indicate(y))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(x, domain_set),
                ReplacementTransform(y, range_set),
                FadeOut(f_is_a_map[0][1], f_is_a_map[1]),
                f_is_a_map[0][0].animate.move_to(ORIGIN)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(f_is_a_map[0][0], f_text),
                FadeIn(f_map)
            )
        )
        self.wait(2)
        self.play(Indicate(f_text))
        self.wait(5)
        
        
        ##Section 4
        self.next_section(name="Function spaces", skip_animations=False)
        f_maps = VGroup(
            f_map,
            f_map.copy().next_to(f_map, UP, buff=0.1),
            Line(
                start=domain_set[0].get_center() + 0.2*DR,
                end=range_set[0].get_center() + 0.2*DL,
                path_arc=1
            ).add_tip()
        )
        f_maps.add(f_maps[-1].copy().next_to(f_maps[-1], DOWN, buff=0.1))
        f_maps.add(Line(start=domain_set[0].get_right()+0.3*LEFT, end=range_set[0].get_left()+0.3*RIGHT).add_tip())
        
        self.play(Write(f_maps[1:]), FadeOut(f_text))
        self.wait(2)
        
        f_spaces = VGroup(Ellipse(width=7, height=5, color=GOLD, fill_opacity=0.2))
        f_spaces.add(Tex(r"Function spaces", color=GOLD).move_to(f_spaces.get_corner(DR)))
        
        h_space = VGroup(Ellipse(width=4, height=2, color=PINK, fill_opacity=0.5))
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        h_space.add(MathTex(r"\mathscr{H}", tex_template=myTemplate, color=PINK).move_to(h_space.get_corner(DR) + 0.2*UL))
        h_space.add(
            MathTex(
                r"F(\omega) = R(\omega) + iG(\omega)& \\"
                r"X:R(\omega) \mapsto G(\omega)& \\"
                r"X \in \mathscr{H}&", 
                font_size=24,
                tex_template=myTemplate
            ).move_to(h_space[0].get_center())
        )
        
        self.play(
            LaggedStart(
                FadeOut(domain_set, range_set),
                ReplacementTransform(f_maps, f_spaces),
                lag_ratio=0.3
            )
        )
        self.wait(2)
        self.play(
            LaggedStart(
                Write(h_space[:-1]),
                FadeIn(h_space[-1]),
                lag_ratio=0.5
            )
        )
        self.wait(2)

        
        ##Section 5
        self.next_section(name="Successive functions", skip_animations=False)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        f_block = Square(side_length=1, color=WHITE)
        f_block.add(MathTex(r"F").move_to(f_block.get_center()))
        
        g_block = Square(side_length=1, color=WHITE)
        g_block.add(MathTex(r"G").move_to(g_block.get_center()))
        
        h_block = Square(side_length=1, color=WHITE)
        h_block.add(MathTex(r"H").move_to(h_block.get_center()))
        blocks = VGroup(f_block, g_block, h_block).arrange(RIGHT, buff=1.5)
        
        
        f_line = Line(
            start=f_block.get_left() + 1.5*LEFT,
            end=f_block.get_left()
        )
        fg_line = Line(
            start=f_block.get_right(),
            end=g_block.get_left()
        )
        gh_line = Line(
            start=g_block.get_right(),
            end=h_block.get_left()
        )
        h_line = Line(
            start=h_block.get_right(),
            end=h_block.get_right() + 1.5*RIGHT
        )
        lines = VGroup(f_line, fg_line, gh_line, h_line)
        
        W_block = Square(side_length=1, color=WHITE)
        W_block.add(MathTex(r"W").move_to(W_block.get_center()))
        W_block.scale(2)
        lW_line = Line(
            start=f_line.get_end(),
            end=W_block.get_left()
        )
        Wl_line = Line(
            start=W_block.get_right(),
            end=h_line.get_start()
        )
        W_lines = VGroup(lW_line, Wl_line)
        
        w1_block = Square(side_length=1, color=WHITE)
        w1_block.add(MathTex(r"w_1").move_to(w1_block.get_center()))
        
        w2_block = Square(side_length=1, color=WHITE)
        w2_block.add(MathTex(r"w_2").move_to(w2_block.get_center()))
        
        w3_block = Square(side_length=1, color=WHITE)
        w3_block.add(MathTex(r"w_3").move_to(w3_block.get_center()))
        w_blocks = VGroup(w1_block, w2_block, w3_block).arrange(RIGHT, buff=1.5)
        w_lines = lines[1:3].copy()
        
        self.play(Write(blocks))
        self.play(Write(lines))
        self.wait(2)
        self.play(
            ReplacementTransform(VGroup(f_block, fg_line, gh_line, h_block), W_lines),
            ReplacementTransform(g_block, W_block)
        )
        self.wait(3)
        self.play(
            ReplacementTransform(W_block, w_blocks),
            ReplacementTransform(W_lines, w_lines)
        )
        self.wait(3)
        
        ##Section 6
        self.next_section(name="Function cascade example", skip_animations=False)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        x_set = Circle(color=RED, fill_opacity=0.5)
        x_set.add(MathTex(r"x", color=RED).move_to(x_set.get_corner(DR) + 0.1*UL))
        
        y_set = Circle(color=GREEN, fill_opacity=0.5)
        y_set.add(MathTex(r"y", color=GREEN).move_to(y_set.get_corner(DR) + 0.1*UL))
        
        z_set = Circle(color=BLUE, fill_opacity=0.5)
        z_set.add(MathTex(r"z", color=BLUE).move_to(z_set.get_corner(DR) + 0.1*UL))
        sets = VGroup(x_set, y_set, z_set).arrange(RIGHT, buff=1.5)
        
        f_map = Line(
            start = x_set.get_center() + 0.2*UR,
            end = y_set.get_center() + 0.2*UL,
            path_arc = -1
        ).add_tip()
        f_text = MathTex(r"f").move_to(f_map.point_from_proportion(0.55) + 0.3*UP)
        f_func = VGroup(f_map, f_text).set_color(GOLD)
        
        g_map = Line(
            start = y_set.get_center() + 0.2*UR,
            end = z_set.get_center() + 0.2*UL,
            path_arc = -1
        ).add_tip()
        g_text = MathTex(r"g").move_to(g_map.point_from_proportion(0.55) + 0.3*UP)
        g_func = VGroup(g_map, g_text).set_color(TEAL_D)
        
        xfy_position = VGroup(x_set, y_set, f_func).get_center() 
        VGroup(x_set, y_set, f_func).move_to(ORIGIN)
        
        z_position = y_set.get_center() #
        x_position = x_set.get_center() #These are for later
        h_map = f_map.copy()            #
        
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    GrowFromCenter(x_set),
                    GrowFromCenter(y_set)
                ),
                Write(f_func),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.play(
            LaggedStart(
                VGroup(x_set, y_set, f_func).animate.move_to(xfy_position),
                Write(g_func),
                FadeIn(z_set),
                lag_ratio=0.2
            )
        )
        self.wait(3)
        
        y_brace = BraceLabel(y_set, r"{{y}}={{f(x)}}")
        y_brace[-1][0].set_color(GREEN)
        for i in [0,1,3]:
            y_brace[-1][2][i].set_color(GOLD)
        y_brace[-1][2][2].set_color(RED)
        
        f_domain = Tex(r"Domain", color=GOLD).next_to(x_set, UP)
        f_range = Tex(r"Range", color=GOLD).next_to(y_set, UP).align_to(f_domain, UP, RIGHT)
        g_domain = Tex(r"Domain", color=TEAL_D).next_to(f_range, UP)
        g_range = Tex(r"Range", color=TEAL_D).next_to(z_set, UP).align_to(f_domain, UP, RIGHT)
        
        g_expression = MathTex(r"{{g}}: {{f(x)}} \mapsto {{z}}").to_corner(UR, buff=0.8)
        g_expression[0].set_color(TEAL_D)
        for i in [0,1,3]:
            g_expression[2][i].set_color(GOLD)
        g_expression[2][2].set_color(RED)
        g_expression[4].set_color(BLUE)
        
        g_line = Line(g_text.get_corner(UR) + 0.1*UR, g_expression.get_corner(DL) + 0.1*DL, stroke_width=2).add_tip(tip_length=0.2)
        
        self.play(Write(y_brace))
        self.wait(2)
        self.play(Write(f_domain), Write(f_range))
        self.wait()
        self.play(Write(g_domain), Write(g_range))
        self.wait()
        self.play(Write(VGroup(g_line, g_expression)))
        self.wait(3)
        
        h_group = VGroup(x_set, z_set)
        h_group.generate_target()
        h_group.target.arrange(RIGHT, buff=1.5)
        
        #h_map is defined before sets x and y are moved
        h_text = MathTex(r"h").move_to(h_map.point_from_proportion(0.55) + 0.3*UP)
        h_func = VGroup(h_map, h_text).set_color(PURPLE)
        
        self.play(
            LaggedStart(
                FadeOut(f_func, f_domain, f_range, y_set, y_brace, g_func, g_expression, g_line, g_domain, g_range),
                MoveToTarget(h_group),
                Write(h_func),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        final_expression = MathTex(r"\begin{matrix} f: x \mapsto y \\ g: y \mapsto z \end{matrix} \Big \} = h: x \mapsto z")
        
        self.play(
            LaggedStart(
                FadeOut(*self.mobjects),
                Write(final_expression),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        


class Test(Scene):
    def construct(self):
        
        x_set = Circle(color=RED, fill_opacity=0.5)
        x_set.add(MathTex(r"x", color=RED).move_to(x_set.get_corner(DR) + 0.1*UL))
        
        y_set = Circle(color=GREEN, fill_opacity=0.5)
        y_set.add(MathTex(r"y", color=GREEN).move_to(y_set.get_corner(DR) + 0.1*UL))
        
        z_set = Circle(color=BLUE, fill_opacity=0.5)
        z_set.add(MathTex(r"z", color=BLUE).move_to(z_set.get_corner(DR) + 0.1*UL))
        sets = VGroup(x_set, y_set, z_set).arrange(RIGHT, buff=1.5)
        
        f_map = Line(
            start = x_set.get_center() + 0.2*UR,
            end = y_set.get_center() + 0.2*UL,
            path_arc = -1
        ).add_tip()
        f_text = MathTex(r"f").move_to(f_map.point_from_proportion(0.55) + 0.3*UP)
        f_func = VGroup(f_map, f_text).set_color(GOLD)
        
        g_map = Line(
            start = y_set.get_center() + 0.2*UR,
            end = z_set.get_center() + 0.2*UL,
            path_arc = -1
        ).add_tip()
        g_text = MathTex(r"g").move_to(g_map.point_from_proportion(0.55) + 0.3*UP)
        g_func = VGroup(g_map, g_text).set_color(TEAL_D)
        
        xfy_position = VGroup(x_set, y_set, f_func).get_center() 
        VGroup(x_set, y_set, f_func).move_to(ORIGIN)
        
        z_position = y_set.get_center() #
        x_position = x_set.get_center() #These are for later
        h_map = f_map.copy()            #
        
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    GrowFromCenter(x_set),
                    GrowFromCenter(y_set)
                ),
                Write(f_func),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.play(
            LaggedStart(
                VGroup(x_set, y_set, f_func).animate.move_to(xfy_position),
                Write(g_func),
                FadeIn(z_set),
                lag_ratio=0.2
            )
        )
        self.wait(3)
        
        y_brace = BraceLabel(y_set, r"{{y}}={{f(x)}}")
        y_brace[-1][0].set_color(GREEN)
        for i in [0,1,3]:
            y_brace[-1][2][i].set_color(GOLD)
        y_brace[-1][2][2].set_color(RED)
        
        f_domain = Tex(r"Domain", color=GOLD).next_to(x_set, UP)
        f_range = Tex(r"Range", color=GOLD).next_to(y_set, UP).align_to(f_domain, UP, RIGHT)
        g_domain = Tex(r"Domain", color=TEAL_D).next_to(f_range, UP)
        g_range = Tex(r"Range", color=TEAL_D).next_to(z_set, UP).align_to(f_domain, UP, RIGHT)
        
        g_expression = MathTex(r"{{g}}: {{f(x)}} \mapsto {{z}}").to_corner(UR, buff=0.8)
        g_expression[0].set_color(TEAL_D)
        for i in [0,1,3]:
            g_expression[2][i].set_color(GOLD)
        g_expression[2][2].set_color(RED)
        g_expression[4].set_color(BLUE)
        
        g_line = Line(g_text.get_corner(UR) + 0.1*UR, g_expression.get_corner(DL) + 0.1*DL, stroke_width=2).add_tip(tip_length=0.2)
        
        self.play(Write(y_brace))
        self.wait(2)
        self.play(Write(f_domain), Write(f_range))
        self.wait()
        self.play(Write(g_domain), Write(g_range))
        self.wait()
        self.play(Write(VGroup(g_line, g_expression)))
        self.wait(3)
        
        h_group = VGroup(x_set, z_set)
        h_group.generate_target()
        h_group.target.arrange(RIGHT, buff=1.5)
        
        #h_map is defined before sets x and y are moved
        h_text = MathTex(r"h").move_to(h_map.point_from_proportion(0.55) + 0.3*UP)
        h_func = VGroup(h_map, h_text).set_color(PURPLE)
        
        self.play(
            LaggedStart(
                FadeOut(f_func, f_domain, f_range, y_set, y_brace, g_func, g_expression, g_line, g_domain, g_range),
                MoveToTarget(h_group),
                Write(h_func),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        final_expression = MathTex(r"\begin{matrix} f: x \mapsto y \\ g: y \mapsto z \end{matrix} \Big \} = h: x \mapsto z")
        
        self.play(
            LaggedStart(
                FadeOut(*self.mobjects),
                Write(final_expression),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        