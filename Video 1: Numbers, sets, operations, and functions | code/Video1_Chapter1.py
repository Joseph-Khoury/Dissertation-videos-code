from manim import *


SVGImages = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\SVGImages"
Images = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\Images"

def get_voltage_levels(
    axes, 
    V_min: float=0, 
    V_max: float=None, 
    dV: float=1, 
    x_max: float=None, 
    dot_radius: float=DEFAULT_DOT_RADIUS, 
    dot_color: str=WHITE, 
    line_width: float=4, 
    font_size: int=DEFAULT_FONT_SIZE, 
    buff: float=0.1, 
    include_numbers: bool=False, 
    include_delta: bool=True
):
    
    dots = VGroup()
    levels = VGroup()
    thresholds = VGroup()
    numbers = VGroup()
    result = VGroup(dots, levels, thresholds, numbers)
    
    V_range = np.arange(V_min, V_max, dV)
    colors = color_gradient([PURE_RED,PURE_GREEN], len(V_range))
    
    for V, color in zip(V_range, colors):
        d1 = Dot(radius=dot_radius, color=dot_color).move_to(axes.coords_to_point(0,V))
        d2 = Dot(radius=dot_radius, color=dot_color).move_to(axes.coords_to_point(0,V+dV))
        thresholds.add(axes.get_line_from_axis_to_point(1,axes.coords_to_point(x_max,V+dV)))
        dots.add(d1,d2)
        
        levels.add(
            Line(
                d1.get_center(),
                d2.get_center(),
                stroke_color=color,
                stroke_width=line_width
            )
        )
        
    if include_delta==True:    
        brace = BraceLabel(levels[0], r"\Delta V", RIGHT, font_size=font_size, buff=buff)
        result.add(brace)
        
    if include_numbers==True:
        for i in range(len(levels)):
            numbers.add(MathTex(f'{i}',font_size=32).next_to(levels[i], LEFT))
    
    return result


class Scene1(Scene):
    def construct(self):
        
        ##Section 1
        self.next_section(name="Thinking about numbers", skip_animations=True)
        stick_man = SVGMobject(f'{SVGImages}\\ThinkingStickman.svg').set_color(WHITE).set_stroke(width=3).shift(DL + LEFT)
        thought_bubble = SVGMobject(f'{SVGImages}\\ThoughtCloud.svg').set_color(WHITE).shift(1.5*UR)
        small_bubble = Circle(radius=0.1, color=WHITE).move_to(1.3*LEFT)
        large_bubble = Circle(radius = 0.25, color=WHITE).move_to(0.5*LEFT + 0.4*UP)
        thought_text = MathTex(r"1,2,3,4,...").move_to(thought_bubble.get_center())
        
        thought = VGroup(small_bubble,large_bubble,thought_bubble)
        VGroup(stick_man,thought,thought_text).move_to(ORIGIN)
        self.play(Write(stick_man))
        self.play(GrowFromEdge(thought, DL))
        self.play(Write(thought_text))
        self.wait(2)
        
        
        
        ##Section 2
        self.next_section(name="Bunch of apples", skip_animations=True)
        self.play(ShrinkToCenter(VGroup(stick_man,thought, thought_text), run_time=0.75))
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').shift(UP)
        apples = VGroup(
            apple.copy(),
            apple.copy().next_to(apple, LEFT),
            apple.copy().next_to(apple, RIGHT),
            apple.copy().next_to(apple, DL),
            apple.copy().next_to(apple,DOWN),
            apple.copy().next_to(apple,DR),
        )
        
        self.play(GrowFromCenter(apples))
        self.wait(2)
        
        
        
        ##Section 3
        self.next_section(name="Counting apples", skip_animations=True)
        self.play(FadeOut(apples))
        self.wait()
        
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').scale(0.5)
        row_of_apples = VGroup(
            apple.copy().shift(0.75*LEFT),
            apple.copy(),
            apple.copy().shift(0.75*RIGHT)
        )
        apples = VGroup(
            apple.copy().to_edge(UP),
            VGroup(
                apple.copy().shift(0.35*LEFT + 1.75*UP),
                apple.copy().shift(0.35*RIGHT + 1.75*UP)
            ),
            row_of_apples.copy().shift(0.5*UP),
            VGroup(
                row_of_apples.copy().shift(2.5*UP),
                row_of_apples.copy().shift(1.25*UP),
                row_of_apples.copy()
            ).scale(0.5).to_edge(DOWN)
            
        )
        apples_text = VGroup(
            MathTex("1").next_to(apples[0], RIGHT),
            MathTex("2").next_to(apples[1], RIGHT),
            MathTex("3").next_to(apples[2], RIGHT),
            MathTex(r"\vdots", font_size=78).shift(0.25*LEFT + 0.85*DOWN),
            MathTex("9").next_to(apples[3], RIGHT).shift(0.5*RIGHT)
        ).shift(0.25*RIGHT)
        
        for i in range(0,3):
            self.play(
                LaggedStart(
                    GrowFromCenter(apples[i]),
                    Write(apples_text[i]),
                    lag_ratio=0.5
                )
            )
            self.wait()
        
        self.play(
            LaggedStart(
                Write(apples_text[3]),
                GrowFromCenter(apples[-1]),
                Write(apples_text[-1]),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        
        
        ##Section 4
        self.next_section(name="No extra digits", skip_animations=True)
        self.play(FadeOut(VGroup(apples,apples_text)))
        
        digits = MathTex(r"{{0,1,2,3,4,5,6,7,8,9}},{{\kappa,\lambda,\mu,\nu,\dots}}")
        ellipse = Ellipse(3).move_to(digits[2].get_center() + 0.1*RIGHT)
        cross_line = Line(ellipse.get_corner(UR) + 0.05*DOWN + 0.8*LEFT, ellipse.get_corner(DL) + 0.05*UP + 0.8*RIGHT, stroke_width=5)
        cross = VGroup(ellipse, cross_line).set_color(rgb_to_color([1,0,0]))
        
        self.play(Write(digits))
        self.wait()
        self.play(Create(cross))
        self.wait(2)
        
        
        
        ##Section 5
        self.next_section(name="Base 10 System", skip_animations=True)
        self.play(
            LaggedStart(
                AnimationGroup(
                    ShrinkToCenter(VGroup(digits[2],cross)),
                    FadeOut(digits[1])
                ),
                digits[0].animate.move_to(ORIGIN),
                lag_ratio=0.5
            )
        )
        digits[1].next_to(digits[0], RIGHT, buff=0.05).align_to(digits[0], DOWN, RIGHT)
        self.wait(2)
        
        single_digits = VGroup(*[digits[i] for i in range(0,2)])
        self.play(
            AnimationGroup(
                FadeIn(digits[1]),
                single_digits.animate.to_edge(UP)
            )
        )
        self.wait()
        
        multi_digits = MathTex(
                         r"&{{10,11,12,13,\dots,19,}} \\ &{{20,21,22,\dots,}} \\"  
                         r"&{{\dots,104,\dots,}} \\ &{{\dots,3709,\dots,}} \\" 
                         r"&{{\dots,69419,\dots,}} \\ &~~~~~~~~~\vdots"
        ).next_to(single_digits, DOWN).align_to(single_digits, LEFT)
        
        self.play(
            LaggedStart(
                *[Write(multi_digits[i]) for i in range(0,len(multi_digits))],
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        
        
        ##Section 6
        self.next_section(name="Counting apples", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').scale(0.75)
        single_digit = MathTex(r"{{1}}=").move_to(2.5*UP + 0.75*LEFT)
        single_apple = apple.copy().next_to(single_digit,RIGHT).shift(0.2*UP)
        single_multiplier = MathTex(r"\times 1").next_to(single_apple,RIGHT).align_to(single_digit, DOWN, RIGHT)
        single_row = VGroup(single_digit, single_apple, single_multiplier)
        
        self.play(Write(single_digit[0]))
        self.play(
            LaggedStart(
                FadeIn(single_digit[1]),
                GrowFromCenter(single_apple),
                Write(single_multiplier),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        double_digit = MathTex(r"{{20}}=").next_to(single_digit, DOWN, buff=1.5)
        double_apple = VGroup(
            apple.copy(),
            apple.copy().next_to(apple, RIGHT, buff=0) 
        ).next_to(double_digit, RIGHT).shift(0.2*UP)
        double_multiplier = MathTex(r"\times 10").next_to(double_apple, RIGHT).align_to(double_digit, DOWN, RIGHT)
        double_row = VGroup(double_digit, double_apple, double_multiplier)
        
        self.play(Write(double_digit[0]))
        self.play(
            LaggedStart(
                FadeIn(double_digit[1]),
                GrowFromCenter(double_apple),
                Write(double_multiplier),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        triple_digit = MathTex(r"{{300}}=").next_to(double_digit, DOWN, buff=1.5)
        triple_apple = VGroup(
            apple.copy().next_to(apple, LEFT, buff=0),
            apple.copy(),
            apple.copy().next_to(apple,RIGHT, buff=0),
        ).next_to(triple_digit, RIGHT).shift(0.2*UP)
        triple_multiplier = MathTex(r"\times 100").next_to(triple_apple, RIGHT).align_to(triple_digit, DOWN, RIGHT)
        triple_row = VGroup(triple_digit, triple_apple, triple_multiplier)
        
        self.play(Write(triple_digit[0]))
        self.play(
            LaggedStart(
                FadeIn(triple_digit[1]),
                GrowFromCenter(triple_apple),
                Write(triple_multiplier),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        so_on = MathTex(r"\vdots", font_size=80).next_to(triple_row, DOWN)
        self.play(Write(so_on))
        self.wait()
        
        ten_zero = MathTex(r"\times 10^0").move_to(single_multiplier).align_to(single_multiplier, LEFT)
        ten_one = MathTex(r"\times 10^1").move_to(double_multiplier).align_to(double_multiplier, LEFT)
        ten_two = MathTex(r"\times 10^2").move_to(triple_multiplier).align_to(triple_multiplier, LEFT)
        
        self.play(
            ReplacementTransform(
                VGroup(single_multiplier, double_multiplier, triple_multiplier),
                VGroup(ten_zero, ten_one, ten_two)
            )
        )
        
        self.wait(2)
        
        
        
        ##Section 7
        self.next_section(name="Natural number system", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        natural_text = Text('"Natural Number System"').move_to(2*UP)
        hands = SVGMobject(f'{SVGImages}\\Hands.svg').set_color(BLUE_E).to_edge(DOWN).scale(2)
        finger_numbers = VGroup(
            MathTex("1").move_to(DOWN + 3.3*LEFT),
            MathTex("2").move_to(0.4*DOWN + 2.4*LEFT),
            MathTex("3").move_to(0.2*DOWN + 1.5*LEFT),
            MathTex("4").move_to(0.5*DOWN + 0.9*LEFT),
            MathTex("5").move_to(1.8*DOWN + 0.4*LEFT),
            MathTex("6").move_to(1.9*DOWN + 0.5*RIGHT),
            MathTex("7").move_to(0.4*DOWN + 0.8*RIGHT),
            MathTex("8").move_to(0.2*DOWN + 1.6*RIGHT),
            MathTex("9").move_to(0.5*DOWN + 2.5*RIGHT),
            MathTex("10").move_to(1.2*DOWN + 3.4*RIGHT)
        )
        
        self.play(Write(natural_text))
        self.wait()
        self.play(FadeIn(hands, shift=UP))
        self.play(
            LaggedStart(
                *[FadeIn(finger_numbers[i]) for i in range(0,len(finger_numbers))],
                lag_ratio=0.2
            )
        )
        self.wait(2)
        
        digits_text = Text("Digits").move_to(natural_text)
        
        self.play(ReplacementTransform(natural_text, digits_text))
        self.wait(2)
        
        
        
        ##Section 8 
        self.next_section(name="Other number systems", skip_animations=True)
        self.play(
            LaggedStart(
                FadeOut(finger_numbers),
                Unwrite(digits_text),
                lag_ratio=0.5
            )
        )
        self.play(FadeOut(hands, shift=DOWN))
        self.wait(2)
        
        binary_name = MathTex("Binary")
        octal_name = MathTex("Octal").next_to(binary_name, DOWN, buff=1)
        hex_name = MathTex("Hexadecimal").next_to(octal_name, DOWN, buff=1)
        base_names = VGroup(binary_name, octal_name, hex_name).move_to(ORIGIN)
        
        binary_base = MathTex(r"\to base~2").next_to(binary_name, RIGHT).align_to(binary_name, UP, RIGHT)
        octal_base = MathTex(r"\to base~8").next_to(octal_name, RIGHT).align_to(octal_name, UP, RIGHT)
        hex_base = MathTex(r"\to base~16").next_to(hex_name, RIGHT).align_to(hex_name, UP, RIGHT)
        
        binary_row = VGroup(binary_name, binary_base)
        octal_row = VGroup(octal_name, octal_base)
        hex_row = VGroup(hex_name, hex_base)
        
        num_bases = VGroup(binary_row, octal_row, hex_row).move_to(ORIGIN)
        
        self.play(Write(binary_row))
        self.wait()
        self.play(Write(octal_row))
        self.wait()
        self.play(Write(hex_row))
        self.wait(2)
        self.play(
            AnimationGroup(
            Circumscribe(binary_row),
            VGroup(octal_row,hex_row).animate.set_opacity(0.5)
            )
        )
        self.wait(2)
        
        
        
        ##Section 9
        self.next_section(name="Binary digits", skip_animations=True)
        binary_digits = MathTex(r"0,1", font_size=200).shift(0.5*DOWN)
        underline = Underline(binary_name)
        binary_title = VGroup(binary_name, underline)
        self.play(
            AnimationGroup(
                LaggedStart(
                    FadeOut(binary_base),
                    binary_title.animate.next_to(binary_digits, UP, buff=0.5).scale(80/DEFAULT_FONT_SIZE),
                    Write(underline.shift(1.2*RIGHT + 0.05*DOWN).scale(2).set_stroke(width=2)),
                    lag_ratio=0.5
                ),
                LaggedStart(
                    FadeOut(octal_row, hex_row),
                    Write(binary_digits),
                    lag_ratio=0.5
                )
            )
        )
        self.wait(2)
        
        
        
        ##Section 10
        self.next_section(name="Binary apples", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
        
        single_multiplier = MathTex(r"\times 1").next_to(single_apple,RIGHT).align_to(single_digit, DOWN, RIGHT)
        single_row = VGroup(single_digit, single_apple, single_multiplier)
        double_multiplier = MathTex(r"\times 10").next_to(double_apple, RIGHT).align_to(double_digit, DOWN, RIGHT)
        double_row = VGroup(double_digit, double_apple, double_multiplier)
        triple_multiplier = MathTex(r"\times 100").next_to(triple_apple, RIGHT).align_to(triple_digit, DOWN, RIGHT)
        triple_row = VGroup(triple_digit, triple_apple, triple_multiplier)
        
        decimal_single_multiplier = MathTex(r"\times 10^0").next_to(single_apple,RIGHT).align_to(single_digit, DOWN, RIGHT)
        decimal_double_multiplier = MathTex(r"\times 10^1").next_to(double_apple, RIGHT).align_to(double_digit, DOWN, RIGHT)
        decimal_triple_multiplier = MathTex(r"\times 10^2").next_to(triple_apple, RIGHT).align_to(triple_digit, DOWN, RIGHT)
        
        decimal_text = Text("Decimal", font_size=60).next_to(double_digit, LEFT, buff=1.5)
        
        self.play(
            FadeIn(
                VGroup(
                    single_row,
                    double_row,
                    triple_row,
                    so_on,
                    decimal_text
                )
            )
        )
        self.wait()
        self.play(
            ReplacementTransform(
                VGroup(
                    single_multiplier,
                    double_multiplier,
                    triple_multiplier
                ),
                VGroup(
                    decimal_single_multiplier,
                    decimal_double_multiplier,
                    decimal_triple_multiplier
                )
            )
        )
        self.wait(2)
        
        binary_single_multiplier = MathTex(r"\times 2^0").next_to(single_apple,RIGHT).align_to(single_digit, DOWN, RIGHT)
        binary_single_row = VGroup(single_digit, single_apple, binary_single_multiplier)
        binary_double_digit = MathTex("10=").next_to(single_digit, DOWN, buff=1.5)
        binary_double_apple = apple.copy().next_to(binary_double_digit, RIGHT).shift(0.2*UP)
        binary_double_multiplier = MathTex(r"\times 2^1").next_to(binary_double_apple, RIGHT).align_to(binary_double_digit, DOWN, RIGHT)
        binary_double_row = VGroup(binary_double_digit, binary_double_apple, binary_double_multiplier).align_to(binary_single_row, RIGHT)
        
        binary_triple_digit = MathTex("100=").next_to(binary_double_digit, DOWN, buff=1.5)
        binary_triple_apple = apple.copy().next_to(binary_triple_digit, RIGHT).shift(0.2*UP)
        binary_triple_multiplier = MathTex(r"\times 2^2").next_to(binary_triple_apple, RIGHT).align_to(binary_triple_digit, DOWN, RIGHT)
        binary_triple_row = VGroup(binary_triple_digit, binary_triple_apple, binary_triple_multiplier).align_to(binary_single_row, RIGHT)
        
        binary_multipliers = VGroup(binary_single_multiplier,binary_double_multiplier,binary_triple_multiplier)
        binary_expanded_multipliers = VGroup(
            MathTex(r"\times 1").next_to(single_apple,RIGHT).align_to(single_digit, DOWN, RIGHT),
            MathTex(r"\times 2").next_to(binary_double_apple, RIGHT).align_to(binary_double_digit, DOWN, RIGHT),
            MathTex(r"\times 4").next_to(binary_triple_apple, RIGHT).align_to(binary_triple_digit, DOWN, RIGHT)
        )
        
        binary_text = Text("Binary", font_size=60).move_to(decimal_text)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(decimal_single_multiplier,binary_single_multiplier),
                ReplacementTransform(VGroup(double_row, decimal_double_multiplier), binary_double_row),
                ReplacementTransform(VGroup(triple_row, decimal_triple_multiplier), binary_triple_row),
                ReplacementTransform(decimal_text, binary_text),
                so_on.animate.next_to(binary_triple_row, DOWN)
            )
        )
        self.wait(2)
        self.play(
            ReplacementTransform(binary_multipliers, binary_expanded_multipliers)
        )
        self.wait(4)
        
        
        
        ##Section 11
        self.next_section(name="binary abbreviations", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        octal_label = MathTex(r"\mathbf{Octal \to base}~{{8}}").to_edge(UP)
        octal_digits = MathTex(r"0,1,2,3,4,5,6,7").next_to(octal_label, DOWN)
        octal_text = VGroup(octal_label, octal_digits).scale(0.8)
        
        hex_label = MathTex(r"\mathbf{Hexadecimal \to base}~{{16}}").next_to(octal_digits, DOWN, buff=2*DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        hex_digits = MathTex(r"0,1,2,3,4,5,6,7,8,9,{{A,B,C,D,E,F}}").next_to(hex_label, DOWN)
        hex_text = VGroup(hex_label, hex_digits).scale(0.8)

        self.play(
            AnimationGroup(
                Write(octal_text),
                Write(hex_text)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                Indicate(octal_digits, rate_func=there_and_back_with_pause, run_time=2),
                VGroup(octal_label, hex_text).animate.set_opacity(0.5)
            )
        )
        self.play(VGroup(octal_label, hex_text).animate.set_opacity(1))
        self.wait()
        self.play(
            AnimationGroup(
                Indicate(hex_digits[0][:-1], rate_func=there_and_back_with_pause, run_time=2),
                VGroup(octal_text, hex_label, hex_digits[0][-1], hex_digits[1]).animate.set_opacity(0.5)
            )
        )
        self.wait()
        self.play(hex_digits.animate.set_opacity(1))
        self.play(
            AnimationGroup(
                Indicate(hex_digits[1], rate_func=there_and_back_with_pause, run_time=2),
                VGroup(*hex_digits[0]).animate.set_opacity(0.5)
            )
        )
        self.play(VGroup(octal_text, hex_text).animate.set_opacity(1))
        self.wait(2)
        
        decimal_num = MathTex(r"69419_{10}").next_to(hex_text, DOWN, buff=0.8)
        equiv1 = MathTex(r"=").next_to(decimal_num, DOWN)
        binary_num = MathTex(r"10000111100101011_2").next_to(equiv1, DOWN)
        equiv2 = equiv1.copy().next_to(binary_num, DOWN)
        octal_num = MathTex(r"207453_8").next_to(equiv2, DOWN)
        equiv3 = equiv1.copy().next_to(octal_num, DOWN)
        hex_num = MathTex(r"10F2B_{16}").next_to(equiv3, DOWN)
        
        num_equivs = VGroup(
            decimal_num,
            equiv1,
            binary_num,
            equiv2,
            octal_num,
            equiv3,
            hex_num
        ).scale(0.8)
        num_frame = SurroundingRectangle(num_equivs, RED, 2*SMALL_BUFF, 0.2)
        
        self.play(
            AnimationGroup(
                VGroup(octal_text, hex_text).animate.set_opacity(0.5),
                LaggedStart(
                    Write(num_equivs),
                    Create(num_frame),
                    lag_ratio=0.8
                )
            )
        )
        self.wait()
        self.play(VGroup(octal_text, hex_text).animate.set_opacity(1))
        self.wait(5)
        
        self.play(
            AnimationGroup(
                octal_label[1].animate.move_to(LEFT).scale(2),
                hex_label[1].animate.move_to(RIGHT).scale(2),
                FadeOut(
                    VGroup(octal_label[0], hex_label[0], octal_digits, hex_digits, num_equivs, num_frame)
                )
            )
        )
        self.wait(2)
        
        eight = MathTex(r"2^3").move_to(octal_label[1]).scale(2)
        sixteen = MathTex(r"2^4").move_to(hex_label[1]).scale(2)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(octal_label[1], eight),
                ReplacementTransform(hex_label[1], sixteen)
            )
        )
        self.wait(2)
        self.play(FadeOut(VGroup(eight, sixteen)))
        self.wait()
        
        abc = MathTex(r"abc_2").scale(2)
        abc_expanded = MathTex(r"{{a\cdot 2^2}} + {{b\cdot 2^1}} + {{c\cdot 2^0}}")
        
        abc_condition = Tex(r"Where, a,b,c can either be \textbf{0} or \textbf{1}").move_to(2*DOWN)
        
        self.play(
            LaggedStart(
                Write(abc),
                Write(abc_condition),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(ReplacementTransform(abc, abc_expanded))
        self.wait(2)
        
        one = MathTex(r"1")
        ones = VGroup()
        for i in range(3):
            ones.add(one.copy().move_to(abc_expanded[2*i][0]).align_to(abc_expanded[2*i],DOWN, RIGHT))
        
        self.play(
            AnimationGroup(
                *[ReplacementTransform(abc_expanded[2*i][0], ones[i]) for i in range(3)]
            )
        )
        self.wait(2)
        
        seven = MathTex(r"=7{{_8}}").next_to(abc_expanded, RIGHT, buff=0.1).shift(0.05*DOWN)
        
        self.play(Write(seven[0]))
        self.wait()
        self.play(
            AnimationGroup(
                VGroup(seven[0][1]).animate.move_to(ORIGIN).scale(2),
                FadeOut(ones, abc_expanded, abc_condition, seven[0][0])
            )
        )
        self.wait(2)
        self.play(FadeIn(seven[1].scale(2).next_to(seven[0][1],DR,buff=-0.1)))
        self.wait(2)
        
        binary_triplet = MathTex(r"{{abc_2}}=A_8").scale(1.5).shift(UP)
        binary_triplet_conditions = MathTex(r"Where~a,b,c &\in \{0,1\}, \\"
                                                      r"A &\in \{0,1,2,3,4,5,6,7\}"
        ).next_to(binary_triplet, DOWN, buff=1.5)
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(seven[0][1],seven[1])),
                Write(binary_triplet),
                Write(binary_triplet_conditions),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        binary_num = MathTex(r"{{010}}{{000}}{{111}}{{100}}{{101}}{{011}}_2")
        
        self.play(
            AnimationGroup(
                ReplacementTransform(binary_triplet[0], binary_num),
                FadeOut(VGroup(binary_triplet[1], binary_triplet_conditions))
            )
        )
        self.wait(2)
        
        mod_arithmetic = MathTex(r"abc_2\equiv A\pmod{8}").move_to(2*DOWN)
        cross = VGroup()
        cross.add(Ellipse(width=4.5, height=2, stroke_width=6, stroke_color=PURE_RED).move_to(mod_arithmetic.get_center()))
        cross.add(Line(cross[0].get_corner(UR) + 0.5*DOWN + 0.275*LEFT, cross[0].get_corner(DL) + 0.5*UP + 0.275*RIGHT, stroke_width=6, stroke_color=PURE_RED))
        
        self.play(Write(mod_arithmetic, run_time=1.5))
        self.play(Create(cross, run_time=1.5))
        self.wait()
        self.play(FadeOut(VGroup(mod_arithmetic, cross)))
        self.wait(2)
        
        binary_num_groups = binary_num[:-1].copy().arrange(RIGHT, buff=1).shift(UP)
        
        for i in range(6):
            binary_num[i].generate_target()
            binary_num[i].target.move_to(binary_num_groups[i])
    
        self.play(
            LaggedStart(
                FadeOut(binary_num[-1]),
                *[MoveToTarget(binary_num[5-i]) for i in range(6)],
                lag_ratio=0.5
            )
        )
        
        bases = VGroup()
        for i in range(6):
            bases.add(MathTex(r"2").scale(0.75).next_to(binary_num[i], DR, buff=0.05).shift(0.05*UP))
        
        self.play(FadeIn(bases))
        self.wait(2)
        
        octal_digits = VGroup(
            MathTex(r"2").move_to(binary_num[0]),
            MathTex(r"0").move_to(binary_num[1]),
            MathTex(r"7").move_to(binary_num[2]),
            MathTex(r"4").move_to(binary_num[3]),   
            MathTex(r"5").move_to(binary_num[4]),
            MathTex(r"3").move_to(binary_num[5]),
        )
        
        self.play(
            LaggedStart(
                *[ReplacementTransform(VGroup(binary_num[5-i], bases[5-i]), octal_digits[5-i]) for i in range(6)],
                lag_ratio=1
            )
        )
        self.wait()
        self.play(octal_digits.animate.arrange(RIGHT, buff=0.05))
        
        octal_base = MathTex(r"8").scale(0.75).next_to(octal_digits, DR, buff=0.05).shift(0.05*UP)
        self.play(FadeIn(octal_base))
        self.wait(5)
        
        hex_text = MathTex(r"Hexadecimal:~{{16}}")
        hex_power_of_two = MathTex(r"2^4").move_to(hex_text[1]).align_to(hex_text[0],DOWN,RIGHT)
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(octal_digits, octal_base)),
                Write(hex_text),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(ReplacementTransform(hex_text[1], hex_power_of_two))
        self.wait()
        
        abcd = MathTex(r"abcd_2")
        abcd_expanded = MathTex(r"{{a\cdot 2^3}} + {{b\cdot 2^2}} + {{c\cdot 2^1}} + {{d\cdot 2^0}}")
        abcd_condition = MathTex(r"Where~a,b,c,d \in {0,1}").move_to(2*DOWN)
        ones = VGroup()
        for i in range(4):
            ones.add(one.copy().move_to(abcd_expanded[2*i][0]).align_to(abcd_expanded[2*i],DOWN,RIGHT))
        fifteen = MathTex(r"={{15_{10}}}").next_to(abcd_expanded, RIGHT, buff=0.1).shift(0.05*DOWN)
        sixteen_minus_one = MathTex(r"(16_{10}-1)").scale(2)
        F_text = MathTex(r"F_{16}").scale(2)
        
        fifteen[1].generate_target()
        fifteen[1].target.move_to(ORIGIN).scale(2)
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(hex_text, hex_power_of_two)),
                Write(abcd),
                lag_ratio=1
            )
        )
        self.wait(2)
        self.play(
            LaggedStart(
                ReplacementTransform(abcd, abcd_expanded),
                FadeIn(abcd_condition),
                lag_ratio=1
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                *[ReplacementTransform(abcd_expanded[2*i][0], ones[i]) for i in range(4)],
                FadeOut(abcd_condition)
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                FadeIn(fifteen, shift=RIGHT),
                VGroup(abcd_expanded,ones).animate.set_opacity(0.5)
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                MoveToTarget(fifteen[1]),
                FadeOut(VGroup(abcd_expanded,ones,fifteen[0]))
            )
        )
        self.wait(2)
        self.play(ReplacementTransform(fifteen[1],sixteen_minus_one))
        self.wait(2)
        self.play(ReplacementTransform(sixteen_minus_one, F_text))
        self.wait(5)
        self.play(ShrinkToCenter(F_text))
        
        binary_num = MathTex(r"{{0001}}{{0000}}{{1111}}{{0010}}{{1011}}_2")
        binary_num_groups = binary_num[:-1].copy().arrange(RIGHT, buff=1).shift(UP)
        for i in range(5):
            binary_num[i].generate_target()
            binary_num[i].target.move_to(binary_num_groups[i])
            
        bases = VGroup()
        for i in range(5):
            bases.add(MathTex(r"2").scale(0.75).next_to(binary_num_groups[i], DR, buff=0.05).shift(0.05*UP))
        hex_digits = VGroup(
            MathTex(r"1").move_to(binary_num_groups[0]),
            MathTex(r"0").move_to(binary_num_groups[1]),
            MathTex(r"F").move_to(binary_num_groups[2]),
            MathTex(r"2").move_to(binary_num_groups[3]),
            MathTex(r"B").move_to(binary_num_groups[4]),
        )
        
        self.play(GrowFromCenter(binary_num))
        self.wait(2)
        self.play(
            LaggedStart(
                FadeOut(binary_num[-1]),
                *[MoveToTarget(binary_num[4-i]) for i in range(5)],
                lag_ratio=0.5
            )
        )
        self.play(FadeIn(bases))
        self.wait(2)
        self.play(
            LaggedStart(
                *[ReplacementTransform(VGroup(binary_num[4-i], bases[4-i]), hex_digits[4-i]) for i in range(5)],
                lag_ratio=1
            )
        )
        self.wait()
        self.play(hex_digits.animate.arrange(RIGHT, buff=0.05))
        hex_base = MathTex(r"16").scale(0.75).next_to(hex_digits, DR, buff=0.05).shift(0.05*UP)
        self.play(FadeIn(hex_base))
        self.wait(5)
        
        self.play(FadeOut(*self.mobjects))
        
        
        #Section 12
        self.next_section(name="Why binary?", skip_animations=True)
        
        
        why_binary = Text("Why Binary?")
        
        self.play(Write(why_binary))
        self.play(Indicate(why_binary, rate_func=there_and_back_with_pause, run_time=1.5))
        self.wait(5)
        
        
        
        ##Section 13
        self.next_section(name="Binary in digital electronics", skip_animations=True)
        self.play(FadeOut(why_binary))
        self.wait()
        
        ax = Axes(
            x_range=[0,2*PI],
            y_range=[0,6],
            axis_config={'include_numbers': False},
            x_length=13,
            y_length=7
        )
        ax_labels = ax.get_axis_labels(MathTex(r"t"),MathTex(r"V(t)"))
        
        analogue_signal = ax.plot(
            lambda x: 3.3+1/3*np.sin(x)+1/10*np.sin(7*x)+1/14*np.sin(14*x)+1/2*np.log(x+1)*1/6*np.cos(21*x),
            color=RED
        )
        self.play(
            LaggedStart(
                Write(VGroup(ax, ax_labels)),
                Create(analogue_signal),
                lag_ratio=1
            )
        )
        self.wait(2)
        
        ideal_signal = ax.plot(lambda x: 3.3, color=RED)
        ideal_text = Text("Ideal", font_size=32, color=YELLOW).move_to(ax.coords_to_point(PI/6,3.6))
        actual_signal = analogue_signal.copy()
        actual_text = Text("Actual", font_size=32, color=YELLOW).move_to(ax.coords_to_point(PI/6,4))
        
        self.play(
            LaggedStart(
                ReplacementTransform(analogue_signal, ideal_signal),
                Write(ideal_text),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.play(
            LaggedStart(
                FadeOut(ideal_text),
                ReplacementTransform(ideal_signal, actual_signal),
                Write(actual_text),
                lag_ratio=1
            )
        )   
        self.wait()
        self.play(FadeOut(actual_text)),
        self.wait(2)
        
        self.add(ax, ax_labels, actual_signal)
        
        dV_tracker = ValueTracker(6)
        
        voltage_levels_infinite = always_redraw(
            lambda: get_voltage_levels(
                axes=ax,
                V_min=0,
                V_max=6,
                dV=dV_tracker.get_value(),
                x_max=2*PI,
                dot_radius=0.08/6*dV_tracker.get_value(),
                font_size=DEFAULT_FONT_SIZE
            )
        )
        
        self.play(Write(voltage_levels_infinite))
        self.wait()
        self.play(dV_tracker.animate.set_value(0.1), run_time=5)
        self.wait(5)
        
        self.play(FadeOut(voltage_levels_infinite))
        self.wait(5)
        
        voltage_levels_infinite.clear_updaters()
        dV_tracker.set_value(0.6)
        
        voltage_levels_decimal = always_redraw(
            lambda: get_voltage_levels(
                axes=ax,
                V_min=0,
                V_max=6,
                dV=dV_tracker.get_value(),
                x_max=2*PI,
                dot_radius=0.08/6*dV_tracker.get_value(),
                font_size=DEFAULT_FONT_SIZE,
                include_numbers=True,
                include_delta = False
            )
        )
        
        self.play(Write(voltage_levels_decimal))
        self.wait(5)
        
        desired_voltage_levels = Rectangle(height=2,width=13, fill_opacity=0.5, stroke_opacity=0.5, color=YELLOW).move_to(ax.coords_to_point(PI,3.3)).align_to(UP)
        
        self.play(Create(desired_voltage_levels))
        self.play(FadeOut(desired_voltage_levels))
        self.wait(2)
        
        filtered_signal = ax.plot(
            lambda x: 3.3 + 1/10*np.sin(7*x)+1/14*np.sin(14*x)+ 1/12*np.cos(21*x),
            color=RED
        )
        filtered_signal_text = Text("Filtered signal", font_size=24, color=YELLOW).move_to(ax.coords_to_point(PI/4,3.8))
        
        actual_signal1 = actual_signal.copy().shift(0.5*UP)
        
        desired_voltage_level = Rectangle(height=0.6,width=13, fill_opacity=0.5, stroke_opacity=0.5, color=YELLOW).move_to(ax.coords_to_point(PI,3.3)).align_to(UP)
        
        self.play(ReplacementTransform(actual_signal, filtered_signal))
        self.play(Write(filtered_signal_text))
        self.wait()
        self.play(Create(desired_voltage_level))
        self.play(FadeOut(desired_voltage_level))
        self.wait(5)
        
        self.play(
            AnimationGroup(
                FadeOut(filtered_signal_text),
                ReplacementTransform(filtered_signal, actual_signal1)
            )
        )
        self.wait()
        
        self.play(dV_tracker.animate.set_value(3))
        self.wait(2)
        
        high_text = Text("High").move_to(2*UP)
        high_level = Rectangle(YELLOW,3.4,13,fill_opacity=0.5, stroke_opacity=0.5).move_to(ax.coords_to_point(PI, 4.5)).align_to(UP)
        low_text = Text("Low").move_to(ax.coords_to_point(PI, 1.3))
        low_level = Rectangle(YELLOW,3.4,13,fill_opacity=0.5, stroke_opacity=0.5).move_to(ax.coords_to_point(PI, 1.5)).align_to(UP)
        
        self.play(Create(high_level))
        self.play(FadeOut(high_level))
        self.play(FadeIn(high_text))
        self.wait(3)
        self.play(Create(low_level))
        self.play(FadeOut(low_level))
        self.play(FadeIn(low_text))
        self.wait(5)
        
        
        
        ##Section 14
        self.next_section(name="Device voltage", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
        
        device = SVGMobject(f'{SVGImages}\\Transistor.svg')
        data_sheet = ImageMobject(f'{Images}\\DataSheet.jpg').add_to_back()
        
        self.play(Write(device))
        self.wait()
        self.play(
            LaggedStart(
                device.animate.shift(2*LEFT),
                FadeIn(data_sheet.move_to(RIGHT), shift=LEFT)
            )
        )
        self.wait()
        
        data_sheet_box = Rectangle(YELLOW, height=0.5, width=1.1).move_to(RIGHT+0.44*UP)
        
        self.play(Circumscribe(data_sheet_box, buff=0))
        self.wait()

        
        
        ##Section 15
        self.next_section(name="TTL", skip_animations=True)
        self.play(FadeOut(device, data_sheet, shift=UP))
        self.wait()
        
        transistor_text = Text("Transistor-Transistor-Logic")
        TTL = MathTex(r"{{TTL}}\begin{cases}"
                      r"3.3V \\ 5V"
                      r"\end{cases}")
        self.play(Write(transistor_text))
        self.wait(2)
        self.play(ReplacementTransform(transistor_text, TTL[0].move_to(ORIGIN)))
        self.wait(2)
        self.play(
            AnimationGroup(
                TTL[0].animate.next_to(TTL[1], LEFT, buff=0.1),
                FadeIn(TTL[1])
            )
        )
        self.wait(2)
        
        
        
        ##Section 16
        self.next_section(name="TTL thresholds", skip_animations=True)
        self.play(Unwrite(TTL))
        self.wait()
        
        num_line = NumberLine(
            x_range = [0,5,0.1],
            length=7,
            include_numbers=False,
            include_ticks=False,
            rotation=PI/2,
            label_direction=RIGHT
        )
        
        ticks = VGroup()
        ticks.add(num_line.get_tick(0, 0.4)) #0
        ticks.add(num_line.get_tick(5,0.4)) #5
        
        numbers = VGroup()
        numbers.add(num_line.add_labels({0: MathTex("0V"), 5:MathTex("5V")}, font_size=45, direction=RIGHT, buff=0.6)) #end numbers
        
        ticks.add(num_line.get_tick(0.8, 0.2)) #0.8
        ticks.add(num_line.get_tick(2, 0.2)) #2
        
        low_height = Line(
            start=num_line.number_to_point(0),
            end=num_line.number_to_point(0.8),
            color=YELLOW
        )
        low_region = Rectangle(color=PURE_RED, height=low_height.get_length(), width=0.5, fill_opacity=0.7, stroke_width=0)\
            .move_to(num_line.number_to_point(0+(0.8-0)/2))
        low_text = Text("LOW", font_size=35, color = PURE_RED).next_to(low_region, LEFT)
        
        ind_height = Line(
            start=num_line.number_to_point(0.8),
            end=num_line.number_to_point(2),
            color=YELLOW
        )
        ind_region = Rectangle(color=ORANGE, height=ind_height.get_length(), width=0.5, fill_opacity=0.7, stroke_width=0)\
            .move_to(num_line.number_to_point(0.8+(2-0.8)/2))
        indeterminate_text = Text("indeterminate", font_size=35, color=ORANGE).next_to(ind_region, LEFT)
        ind_text = Text("ind.", font_size=35, color=ORANGE).next_to(ind_region, LEFT)
        
        high_height = Line(
            start=num_line.number_to_point(2),
            end=num_line.number_to_point(5),
            color=YELLOW
        )
        high_region = Rectangle(color=PURE_GREEN, height=high_height.get_length(), width=0.5, fill_opacity=0.7, stroke_width=0)\
            .move_to(num_line.number_to_point(2+(5-2)/2))
        high_text = Text("HIGH", font_size=35, color=PURE_GREEN).next_to(high_region, LEFT)
        
        self.play(Write(VGroup(num_line, *ticks[:2], numbers)))
        self.wait(2)
        self.play(
            AnimationGroup(
                Write(ticks[2]),
                num_line.animate.add_labels({0.8: MathTex("0.8V")}, font_size=35, direction=RIGHT, buff=0.4),
                ShowPassingFlash(low_height, time_width=1)
            )
        )
        self.play(GrowFromEdge(low_region,DOWN))
        self.play(FadeIn(low_text))
        self.wait(2)
        
        self.play(
            AnimationGroup(
                Write(ticks[3]),
                num_line.animate.add_labels({2: MathTex("2V")}, font_size=35, direction=RIGHT, buff=0.4),
                ShowPassingFlash(high_height, time_width=1)
            )
        )
        self.play(GrowFromEdge(high_region,DOWN))
        self.play(FadeIn(high_text))
        self.wait(2)
        
        self.play(ShowPassingFlash(ind_height, time_width=1))
        self.play(GrowFromCenter(ind_region))
        self.play(FadeIn(indeterminate_text))
        self.wait()
        self.play(ReplacementTransform(indeterminate_text, ind_text))
        self.wait(2)




class Test(Scene):
    def construct(self):
        # self.add(NumberPlane())
        
        eight = MathTex(r"8").scale(1.6).move_to(LEFT)
        sixteen = MathTex(r"16").scale(1.6).move_to(RIGHT)
        
        two_3 = MathTex(r"2^3").scale(1.6).move_to(LEFT).align_to(eight, DOWN, RIGHT) 
        two_4 = MathTex(r"2^4").scale(1.6).move_to(RIGHT).align_to(sixteen ,DOWN, RIGHT)
        
        self.add(eight, sixteen)
        self.wait(2)
        self.play(ReplacementTransform(eight,two_3))
        self.wait(2)
        self.play(ReplacementTransform(sixteen,two_4))
        self.wait(2)
        
        