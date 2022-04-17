from manim import *

SVGImages = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\SVGImages"
Images = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\Images"


class MainScene(Scene):
    def construct(self):
        
        ##Section 1
        self.next_section(name="Arithmetic operations", skip_animations=True)
        ArOps = MathTex(r"{{+}} {{ , ~ - }} {{ , ~ \times }} {{ , ~ \divisionsymbol }}", font_size=81)
        
        addition_equation = MathTex(r"a+b")
        subtraction_equation = MathTex(r"a-b")
        multiplication_equation = MathTex(r"a \times b")
        division_equation = MathTex(r"a \divisionsymbol b")
        ArEqs = VGroup(addition_equation, subtraction_equation, multiplication_equation, division_equation).scale(1.2).arrange(DOWN, buff=1)
        
        add_addition = addition_equation.copy()
        add_subtraction = MathTex(r"a + (-b)").scale(1.2)
        add_multiplication = VGroup(MathTex(r"a + a + \dots + a").scale(1.2))
        add_multiplication.add(BraceLabel(add_multiplication,r"b times", font_size=(36), color=RED, label_constructor=Tex))
        add_division = VGroup(MathTex(r"a + {{(-b) + (-b) + \dots + (-b)}} + r").scale(1.2))
        add_division.add(BraceLabel(add_division[0][1], r"quotient", font_size=(36), color=RED, label_constructor=Tex))
        add_division.add(BraceLabel(add_division[0][2][1], r"remainder", font_size=(36), color=RED, label_constructor=Tex, stroke_width=1))
        add_ArEqs = VGroup(
            add_addition, 
            add_subtraction,
            add_multiplication,
            add_division
        ).arrange(DOWN, buff=1)
        
        self.play(FadeIn(ArOps))
        self.wait(2)
        self.play(
            AnimationGroup(
                ReplacementTransform(ArOps[0], addition_equation),
                ReplacementTransform(VGroup(*ArOps[1:4]), subtraction_equation),
                ReplacementTransform(VGroup(*ArOps[4:7]), multiplication_equation),
                ReplacementTransform(VGroup(*ArOps[7:]), division_equation)
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                ReplacementTransform(addition_equation, add_addition),
                ReplacementTransform(subtraction_equation, add_subtraction),
                ReplacementTransform(multiplication_equation, add_multiplication),
                ReplacementTransform(division_equation, add_division)
            )
        )
        self.wait(2)
        
        self.play(
            AnimationGroup(
                VGroup(add_addition, add_subtraction, add_division).animate.set_opacity(0.5),
                Indicate(add_multiplication)
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                add_multiplication.animate.set_opacity(0.5),
                add_division.animate.set_opacity(1)
            )
        )
        self.play(Indicate(add_division))
        self.wait(2)
        self.play(
            AnimationGroup(
                add_division.animate.set_opacity(0.5),
                add_subtraction.animate.set_opacity(1)
            )
        )
        self.play(Indicate(add_subtraction))
        self.wait(2)
        self.play(VGroup(add_addition, add_multiplication, add_division).animate.set_opacity(1))
        self.wait(5)
        
        
        
        ##Section 2
        self.next_section(name="The logic behind arithmetic", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        symmetric_logic = MathTex(r"a + b \equiv b + a", font_size=64)
        self.play(Write(symmetric_logic))
        self.wait(2)
        
        operations_title = Tex(r"\textbf{Operations}", font_size=72).move_to(1.5*UP)
        operations_definition = Tex(r"``A combining process of 2 \textbf{mathematical objects}, \\ or of a mathematical object and an operator, \\ which produces a well-defined output''").move_to(DOWN)
        
        self.play(ReplacementTransform(symmetric_logic, VGroup(operations_title, operations_definition)))
        self.wait(5)
        
        
        
        ##Section 3
        self.next_section(name="The addition operation", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').scale(0.6)
        
        two_apples = VGroup(
            apple.copy().shift(0.45*LEFT),
            apple.copy().shift(0.45*RIGHT)
        ).move_to(5*LEFT)
        
        plus = MathTex(r"+",font_size=81).move_to(3.25*LEFT)
        
        three_apples = VGroup(
            apple.copy().shift(0.9*LEFT),
            apple.copy(),
            apple.copy().shift(0.9*RIGHT)
        ).shift(LEFT)
        
        equals = MathTex(r"=", font_size=81).move_to(1.5*RIGHT)
        
        five_apples = VGroup(
            apple.copy().shift(1.2*UP + 0.45*LEFT),
            apple.copy().shift(1.2*UP + 0.45*RIGHT),
            apple.copy().shift(0.9*LEFT),
            apple.copy(),
            apple.copy().shift(0.9*RIGHT)
        ).move_to(4*RIGHT)
        
        VGroup(two_apples, three_apples, five_apples).shift(0.25*UP)
        
        self.play(
            LaggedStart(
                GrowFromCenter(two_apples),
                GrowFromCenter(three_apples),
                Write(plus),
                lag_ratio=0.5
            )
        )
        self.play(
            LaggedStart(
                Write(equals),
                GrowFromCenter(five_apples),
                lag_ratio=0.3
            )
        )
        self.wait(4)
        
        two = MathTex(r"2", font_size=81).move_to(two_apples)
        three = MathTex(r"3", font_size=81).move_to(three_apples)
        five = MathTex(r"5", font_size=81).move_to(five_apples)
        
        VGroup(two, three, five).shift(0.25*DOWN)
        
        self.play(
            LaggedStart(
                ReplacementTransform(two_apples, two),
                ReplacementTransform(three_apples, three),
                ReplacementTransform(five_apples, five),
                lag_ratio=0.5
            )
        )
        
        addition = VGroup(two,plus,three,equals,five)
        
        self.play(addition.animate.arrange(RIGHT))
        self.wait(2)
        
        addition.generate_target()
        addition.target.scale(0.6).move_to(2.5*UP)
        box = SurroundingRectangle(addition.target, color=RED, buff=0.2, corner_radius=0.1, stroke_width=2)
        
        num_line = NumberLine(
            x_range=[-5,5],
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).set_z_index(0)
        
        path = VMobject(color=RED).set_z_index(1)
        dot = Dot(radius=0.1, point=num_line.number_to_point(2), color=BLUE).set_z_index(3)
        dot.generate_target()
        dot.target.move_to(num_line.number_to_point(5))
        dot_shadow = Circle(radius=0.1, color=YELLOW, stroke_width=1).move_to(dot.get_center()).set_z_index(2)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        
        self.play(
            LaggedStart(
                MoveToTarget(addition),
                Write(box),
                LaggedStart(
                    Write(num_line),
                    GrowFromCenter(dot),
                    lag_ratio=0.75
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.add(path)
        self.play(
            AnimationGroup(
                MoveToTarget(dot, run_time=1.5),
                FadeIn(dot_shadow, run_time=0.1)
            )
        )
        
        distance = BraceLabel(path, r"+3 units", brace_direction=UP, label_constructor=Tex)
        self.play(Write(distance, run_time=1.5))
        self.wait(5)
        
        
        
        ##Section 4
        self.next_section(name="The multiplication operation", skip_animations=True)
        self.play(
            AnimationGroup(
                FadeOut(path, run_time=0.4),
                ShrinkToCenter(VGroup(num_line, dot, dot_shadow, distance, addition, box))
            )
        )
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').scale(0.5)
        
        two_apples = VGroup(
            apple.copy().shift(0.375*LEFT),
            apple.copy().shift(0.375*RIGHT)
        ).shift(0.15*UP + 4.5*LEFT)
        
        times_three = MathTex(r"\times 3", font_size=64).next_to(two_apples.copy().shift(0.15*DOWN))
        
        equals = MathTex(r"=", font_size=64).next_to(times_three, RIGHT)
        
        two_apples1 = two_apples.copy().next_to(equals, RIGHT).shift(0.15*UP)
        plus1 = MathTex(r"+", font_size=64).next_to(two_apples1.copy().shift(0.15*DOWN), RIGHT)
        two_apples2 = two_apples.copy().next_to(plus1, RIGHT).shift(0.15*UP)
        plus2 = MathTex(r"+", font_size=64).next_to(two_apples2.copy().shift(0.15*DOWN), RIGHT)
        two_apples3 = two_apples.copy().next_to(plus2, RIGHT).shift(0.15*UP)
        
        apple_addition = VGroup(
            two_apples1,
            plus1,
            two_apples2,
            plus2,
            two_apples3
        )
        
        three_times = BraceLabel(apple_addition, r"3 times", label_constructor=Tex)
        
        self.play(
            LaggedStart(
                GrowFromCenter(two_apples),
                Write(times_three),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                FadeIn(equals),
                LaggedStart(
                        AnimationGroup(
                            GrowFromCenter(two_apples1),
                            GrowFromCenter(two_apples2),
                            GrowFromCenter(two_apples3)
                        ),
                        AnimationGroup(
                            Write(plus1),
                            Write(plus2)
                        ),
                        lag_ratio=1
                    ),
                 lag_ratio=0.5
            )
        )
        self.play(Write(three_times))
        self.wait(3)
        
        two_apples2.generate_target()
        two_apples2.target.move_to(2*RIGHT + 0.15*UP)
        two_apples1.generate_target()
        two_apples1.target.next_to(two_apples2.target, UP, buff=0.1)
        two_apples3.generate_target()
        two_apples3.target.next_to(two_apples2.target, DOWN, buff=0.1)
        
        RHS = VGroup(
            two_apples1.target,
            two_apples2.target,
            two_apples3.target
        )
        
        LHS = VGroup(
            two_apples,
            times_three,
            equals,
        )
        LHS.generate_target()
        LHS.target.next_to(RHS, LEFT)
        
        self.play(
            LaggedStart(
                FadeOut(three_times),
                AnimationGroup(
                    FadeOut(plus1, plus2),
                    MoveToTarget(two_apples1),
                    MoveToTarget(two_apples2),
                    MoveToTarget(two_apples3),
                    MoveToTarget(LHS)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        two = MathTex(r"2", font_size=64).next_to(times_three, LEFT, buff=0.15)
        six = MathTex(r"6", font_size=64).next_to(equals, RIGHT)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(two_apples, two),
                ReplacementTransform(
                    VGroup(
                        two_apples1,
                        two_apples2,
                        two_apples3,
                        ), 
                    six
                )
            )
        )
        self.wait(5)
        
        LHS = VGroup(two, times_three, equals)
        LHS.generate_target()
        LHS.target.shift(LEFT)
        brace_height = Line(1.5*UP, 1.5*DOWN)
        brace = Brace(brace_height, LEFT).next_to(LHS.target, RIGHT, buff=0.15)
        
        case1 = MathTex(r"2 + 2 + 2", font_size=42).move_to(1.4*UP + 1.5*RIGHT)
        case2 = MathTex(r"6", font_size=42).move_to(1.4*DOWN).align_to(case1, LEFT)
        
        self.play(
            LaggedStart(
                FadeOut(six),
                AnimationGroup(
                    MoveToTarget(LHS),
                    Write(brace)
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Write(case1))
        self.wait(3)
        self.play(Write(case2))
        self.wait(5)
        
        multiplication = VGroup(two, times_three)
        multiplication.generate_target()
        multiplication.target.scale(0.8).move_to(2.5*UP)
        box = SurroundingRectangle(multiplication.target, color=RED, buff=0.15, corner_radius=0.1, stroke_width=2)
        
        num_line = NumberLine(
            x_range=[-6,6],
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).set_z_index(0)
        
        path = VMobject(color=RED).set_z_index(1)
        dot = Dot(radius=0.1, point=num_line.number_to_point(2), color=BLUE).set_z_index(3)
        dot.generate_target()
        dot.target.move_to(num_line.number_to_point(6))
        dot_shadow = Circle(radius=0.1, color=YELLOW, stroke_width=1).move_to(dot.get_center()).set_z_index(2)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        
        path.add_updater(update_path)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(equals, brace, case1, case2),
                    MoveToTarget(multiplication)
                ),
                Write(box),
                LaggedStart(
                    Write(num_line),
                    GrowFromCenter(dot),
                    lag_ratio=0.75
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.add(path)
        self.play(
            AnimationGroup(
                MoveToTarget(dot, run_time=1.5),
                FadeIn(dot_shadow, run_time=0.1)
            )
        )
        
        distance = BraceLabel(path, r"\times 3", brace_direction=UP)
        self.play(Write(distance, run_time=1.5))
        self.wait(5)
        
        self.play(FadeOut(*self.mobjects))
        
        multiplication_operation = MathTex(r"(a,b) \mapsto c", font_size=81)
        self.play(Write(multiplication_operation))
        self.wait(2)
        
        multiplication_definition = MathTex(
            r"a \times b = \begin{cases}"
            r"a+a+\dots+a, ~\text{(b times)} \\"
            r"b+\dots+b, ~\text{(a times)} \\"
            r"ab \\"
            r"\end{cases}"
        )
        
        self.play(ReplacementTransform(multiplication_operation, multiplication_definition))
        self.wait(5)
        
        
        
        ##Section 5
        self.next_section(name="The subtraction operation", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').scale(0.6).shift(0.15*UP)
        
        six_apples = VGroup(apple.copy())
        six_apples.add(apple.copy().next_to(six_apples, LEFT, buff=0.1))
        six_apples.add(apple.copy().next_to(six_apples, RIGHT, buff=0.1))
        six_apples.add(six_apples.copy().next_to(six_apples, UP, buff=0.1))
        
        equals = MathTex(r" = ", font_size=81)
        six = MathTex(r"6", font_size=81).next_to(equals, LEFT)
        six_minus_four = MathTex(r"{{6}}-4", font_size=81).next_to(equals, LEFT)
        six_apples.next_to(equals, RIGHT).shift(0.15*UP)
        
        six.generate_target()
        six.target.move_to(six_minus_four[0])
        
        self.play(
            LaggedStart(
                Write(VGroup(six,equals)),
                GrowFromCenter(six_apples),
                lag_ratio=0.3
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                MoveToTarget(six),
                FadeIn(six_minus_four[1]),
                FadeOut(*[six_apples[x] for x in [0,2]], *[six_apples[3][y] for y in [0,2]]),
                lag_ratio=0.3
            )
        )
        self.wait(3)
        
        seven = MathTex(r"7", font_size=81).move_to(six_minus_four[1][1])
        anti_apple = SVGMobject(f'{SVGImages}\\InvertedApple.svg').scale(0.6).next_to(equals, RIGHT).shift(0.15*UP)
        question_mark = Tex(r"?", font_size=81, color=YELLOW).next_to(anti_apple, RIGHT).shift(0.15*DOWN)
        
        self.play(
            LaggedStart(
                FadeOut(six_minus_four[1][1]),
                FadeIn(seven),
                ReplacementTransform(VGroup(six_apples[3][1], six_apples[1]), anti_apple),
                lag_ratio=0.3
            )
        )
        self.play(FadeIn(question_mark))
        self.wait(2)
        
        debt = BraceLabel(anti_apple, text=r"debt", brace_direction=RIGHT, label_constructor=Tex, color=YELLOW)
        
        self.play(
            LaggedStart(
                FadeOut(question_mark),
                Write(debt),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        subtraction = MathTex(r"2{{-}}3", font_size=81).scale(0.6).move_to(2.5*UP)
        box = SurroundingRectangle(subtraction, color=RED, buff=0.2, corner_radius=0.1, stroke_width=2)
        subtraction = VGroup(subtraction, box)
        
        num_line = NumberLine(
            x_range=[-5,5],
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).set_z_index(0)
        
        dot = Dot(radius=0.1, point=num_line.number_to_point(2), color=BLUE).set_z_index(3)
        path = always_redraw(
            lambda: Line(
                num_line.number_to_point(2),
                dot,
                color=RED
            )
        ).set_z_index(1)
        
        dot.generate_target()
        dot.target.move_to(num_line.number_to_point(-1))
        dot_shadow = Circle(radius=0.1, color=YELLOW, stroke_width=1).move_to(dot.get_center()).set_z_index(2)
        
        self.play(
            LaggedStart(
                Write(subtraction),
                LaggedStart(
                    Write(num_line),
                    GrowFromCenter(dot),
                    lag_ratio=0.75
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.add(path)
        self.play(
            AnimationGroup(
                MoveToTarget(dot, run_time=1.5),
                FadeIn(dot_shadow, run_time=0.1)
            )
        )
        
        distance = BraceLabel(path, r"-3 ~ \text{units}", brace_direction=UP)
        self.play(Write(distance, run_time=1.5))
        self.wait(3)
        
        dot.target.move_to(num_line.number_to_point(5))
        plus = MathTex(r"+", font_size=81).scale(0.6).move_to(subtraction[0][1])
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(distance),
                    ReplacementTransform(subtraction[0][1], plus)    
                ),
                MoveToTarget(dot, run_time=2),
                lag_ratio=0.5
            )
        )
        
        distance = BraceLabel(path, r"+3 ~ \text{units}", brace_direction=UP)
        self.play(Write(distance, run_time=1.5))
        self.wait(5)
        
        self.play(
            Unwrite(
                VGroup(
                    subtraction,
                    plus,
                    num_line,
                    dot,
                    dot_shadow,
                    path,
                    distance
                )
            )
        )
        self.wait()
        
        commutative_label = Tex(r"\textbf{The commutative property}", font_size=64, color=YELLOW).move_to(UP)
        commutative_property = MathTex(r"A ~ \text{then} ~ B \equiv B ~ \text{then} ~ A", font_size=64).move_to(0.5*DOWN)
        
        self.play(
            LaggedStart(
                Write(commutative_label, run_time=1),
                FadeIn(commutative_property),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        subtraction_label = Tex(r"\textbf{Subtraction}", font_size=64, color=RED).move_to(UP)
        eqn = MathTex(r"a {{+}} (-b)", font_size=64).shift(0.5*DOWN + 0.4*RIGHT)
        alt_eqn = MathTex(r"(-b) {{+}} a", font_size=64).shift(0.5*DOWN + 0.45*LEFT)
        a = eqn[0].copy()
        plus = eqn[1].copy()
        minus_b = eqn[2].copy()
        alt_a = alt_eqn[2].copy()
        alt_minus_b = alt_eqn[0].copy()
        
        path_a = Line(eqn[0].get_center(), alt_eqn[2].get_center(), path_arc=-3)
        path_b = Line(eqn[2].get_center(), alt_eqn[0].get_center(), path_arc=-3)
        alt_path_a = Line(alt_eqn[2].get_center(), eqn[0].get_center(), path_arc=-3)
        alt_path_b = Line(alt_eqn[0].get_center(), eqn[2].get_center(), path_arc=-3)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(commutative_label, subtraction_label),
                FadeOut(commutative_property)
            )
        )
        self.play(Write(VGroup(a, plus, minus_b)))
        self.play(
            AnimationGroup(
                MoveAlongPath(a, path_a),
                MoveAlongPath(minus_b, path_b)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                MoveAlongPath(a, alt_path_a),
                MoveAlongPath(minus_b, alt_path_b)
            )
        )
        self.wait(2)
        
        non_commutative_subtraction = MathTex(r"a - b {{\neq}} b - a", font_size=64).move_to(0.5*DOWN)
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(a, plus, minus_b)),
                Write(non_commutative_subtraction),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        ##Section 6
        self.next_section(name="The division operation", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        addition_label = Tex(r"\textbf{Addition}", font_size=42).move_to(0.5*UP)
        addition_com = MathTex(r"a + b = b + a", font_size=42).move_to(0.5*DOWN)
        addition = VGroup(addition_label, addition_com)
        
        subtraction_label = Tex(r"\textbf{Subtraction}", font_size=42).move_to(0.5*UP)
        subtraction_com = MathTex(r"a - b = -b + a", font_size=42).move_to(0.5*DOWN)
        subtraction = VGroup(subtraction_label, subtraction_com)
        
        multiplication_label = Tex(r"\textbf{Multiplication}", font_size=42).move_to(0.5*UP)
        multiplication_com = MathTex(r"a \times b = b \times a", font_size=42).move_to(0.5*DOWN)
        multiplication = VGroup(multiplication_label, multiplication_com)
        
        division_label = Tex(r"\textbf{Division}", font_size=42).move_to(0.5*UP)
        question_mark = Tex(r"?", font_size=64, color=YELLOW).move_to(0.5*DOWN)
        
        VGroup(addition, subtraction, multiplication, VGroup(division_label, question_mark)).arrange(RIGHT, buff=0.8)
        
        dividing_lines = VGroup(
            Line(2*UP + 3.4*LEFT, 2*DOWN + 3.4*LEFT, stroke_width=2),
            Line(2*UP + 0.2*RIGHT, 2*DOWN + 0.2*RIGHT, stroke_width=2),
            Line(2*UP + 4*RIGHT, 2*DOWN + 4*RIGHT, stroke_width=2),
        )
        
        self.play(
            AnimationGroup(
                *[Write(obj) for obj in [addition_label, subtraction_label, multiplication_label, division_label]],
                FadeIn(dividing_lines)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                Write(addition_com),
                VGroup(dividing_lines[1:], subtraction_label, multiplication_label, division_label).animate.set_opacity(0.5)
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                AnimationGroup(
                    VGroup(dividing_lines[1], subtraction_label).animate.set_opacity(1),
                    addition.animate.set_opacity(0.5)
                ),
                Write(subtraction_com),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                AnimationGroup(
                    VGroup(dividing_lines[2], multiplication_label).animate.set_opacity(1),
                    VGroup(dividing_lines[0], subtraction).animate.set_opacity(0.5)
                ),
                Write(multiplication_com),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                AnimationGroup(
                    division_label.animate.set_opacity(1),
                    VGroup(dividing_lines[1], multiplication).animate.set_opacity(0.5)
                ),
                Write(question_mark),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            VGroup(addition, subtraction, multiplication, dividing_lines[:2]).animate.set_opacity(1)
        )
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        
        ncom_div = MathTex(r"a \divisionsymbol b \neq b \divisionsymbol a", font_size=81)
        com_div = MathTex(r"{{a \times {1 \over b}}} = {1 \over b} \times a" ,font_size=72)
        
        self.play(Write(ncom_div))
        self.wait(2)
        self.play(FadeOut(ncom_div))
        self.play(Write(com_div))
        self.wait(3)
        self.play(
            LaggedStart(
                FadeOut(com_div[1]),
                com_div[0].animate.move_to(ORIGIN),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        a = com_div[0][0]
        times = com_div[0][1]
        b = com_div[0][2:]
        
        a_copy = a.copy()
        b_copy = b.copy()
        
        a_left = a.get_center()
        a_right = a.copy().next_to(times, RIGHT).align_to(a, DOWN, RIGHT).get_center()
        b_right = b.get_center()
        b_left = b.copy().next_to(times, LEFT).align_to(b, DOWN, RIGHT).get_center()
        
        path_a = Line(
            a_left,
            a_right,
            path_arc=-3,
        )
        path_b = Line(
            b_right,
            b_left,
            path_arc=-3,
        )
        alt_path_a = Line(
            a_right,
            a_left,
            path_arc=-3,
        )
        alt_path_b = Line(
            b_left,
            b_right,
            path_arc=-3,
        )
        
        self.play(
            AnimationGroup(
                MoveAlongPath(a, path_a),
                MoveAlongPath(b, path_b),
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                MoveAlongPath(a, alt_path_a),
                MoveAlongPath(b, alt_path_b),
            )
        )
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        division_com = MathTex(r"a \times {1 \over b} = {1 \over b} \times a", font_size=38).next_to(division_label, DOWN, buff=0.525).shift(0.2*RIGHT)
        division_label.shift(0.2*RIGHT)
        division = VGroup(division_label, division_com)
        
        self.play(
            AnimationGroup(
                *[Write(obj) for obj in [addition, subtraction, multiplication, division]],
                FadeIn(dividing_lines)
            )
        )
        self.wait(5)
        
        self.play(
            AnimationGroup(
                Indicate(addition),
                VGroup(subtraction, multiplication, division, dividing_lines[1:]).animate.set_opacity(0.5)
            )
        )
        self.wait(2)
        
        self.play(
            LaggedStart(
                FadeOut(dividing_lines, subtraction, multiplication, division),
                addition.animate.scale(2).move_to(ORIGIN),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        self.play(FadeOut(*self.mobjects))


    
class LinAlgScene(ThreeDScene): #Use opengl rendering for this, as it looks miles better
    
    def linear_transform(self, plane, vectors, vector_colors: tuple, matrix, *added_anims):
        vectors = VGroup(*vectors)
        plane.generate_target()
        plane.target.apply_matrix(matrix)
        new_vectors = VGroup()
        for i in range(len(vectors)):
            x = vectors[i].get_end()
            new_vectors.add(Vector(matrix @ x[:2], color=vector_colors[i]))
        self.play(
            AnimationGroup(
                MoveToTarget(plane),
                *[ReplacementTransform(vectors[i], new_vectors[i]) for i in range(len(vectors))],
                *added_anims
            )
        )
        return new_vectors
            
            
    def construct(self):
        
        ##Section 1
        self.next_section(name="Cross Product", skip_animations=True)
        axes = ThreeDAxes(
            x_range=[-10,10],
            y_range=[-10,10],
            z_range=[-10,10],
            x_length=20,
            y_length=20,
            z_length=20,
        )
        axes.add(axes.get_axis_labels())
        plane = NumberPlane(
            x_range=[-10,10],   
            y_range=[-10,10],
            x_length=20,
            y_length=20,
        )
        self.set_camera_orientation(phi=0)
        
        self.play(
            AnimationGroup(
                Write(axes),
                Write(plane)
            ),
            run_time=1.2
        )
        
        v = Vector(np.array([1,2,0]), color=RED)
        v_label = MathTex(r"\vec{v}", color=v.get_color()).move_to(v.get_end() + 0.25*UL)
        w = Vector(np.array([-1,1,0]), color=GREEN)
        w_label = MathTex(r"\vec{w}", color=w.get_color()).move_to(w.get_end() + 0.25*UL)
        
        v_coord = np.array([1,2,0])
        v_norm = np.linalg.norm(v_coord)
        w_coord = np.array([-1,1,0])
        w_norm = np.linalg.norm(w_coord)
        vw_dot = np.dot(v_coord, w_coord)
        vw_angle = np.arccos(vw_dot/(v_norm*w_norm))
        
        v_point = v.get_end()+0.25*UR
        w_point = rotation_about_z(vw_angle) @ v_point
        
        clkwise = Line(start=v_point, end=w_point, path_arc=2).add_tip()
        anti_clkwise = Line(start=w_point, end=v_point, path_arc=-2).add_tip()
        
        self.play(
            LaggedStart(
                Write(VGroup(v, v_label)),
                Write(VGroup(w, w_label)),
                lag_ratio=0.5
            )
        )
        
        v_cross_w = MathTex(r"\vec{v} \times \vec{w} = \vec{u}", substrings_to_isolate=[r"\vec{v}",r"\vec{w}",r"-\vec{u}"]).move_to(3*RIGHT + 1.5*UP)
        v_cross_w.set_color_by_tex("v", RED)
        v_cross_w.set_color_by_tex("w", GREEN)
        v_cross_w.set_color_by_tex("u", GOLD)
        
        w_cross_v = MathTex(r"\vec{w} \times \vec{v} = -\vec{u}", substrings_to_isolate=[r"\vec{v}",r"\vec{w}",r"\vec{u}"]).move_to(v_cross_w)
        w_cross_v.set_color_by_tex("v", RED)
        w_cross_v.set_color_by_tex("w", GREEN)
        v_cross_w.set_color_by_tex("u", GOLD)
        
        u_end = np.cross(v.get_end(), w.get_end())
        u = Arrow3D(start=ORIGIN, end=u_end, color=GOLD, thickness=0.04, base_radius=0.1, fill_opacity=1)
        u_label = MathTex(r"\vec{u}", color=GOLD).move_to(0.5*DR)
        
        self.play(
            LaggedStart(
                Write(clkwise),
                Write(v_cross_w),
                lag_ratio=0.5
            )
        )
        self.move_camera(phi=PI/4, added_anims=[GrowFromPoint(u, ORIGIN), Write(u_label)])
        self.begin_ambient_camera_rotation(rate=0.2, about="theta")
        self.wait(2)
        
        minus_u_end = np.cross(w.get_end(), v.get_end())
        minus_u = Arrow3D(start=ORIGIN, end=minus_u_end, color=GOLD)
        minus_u_label = MathTex(r"-\vec{u}", color=GOLD).move_to(u_label)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    ReplacementTransform(clkwise, anti_clkwise),
                    ReplacementTransform(v_cross_w, w_cross_v)
                ),
                AnimationGroup(
                    ReplacementTransform(u, minus_u),
                    ReplacementTransform(u_label, minus_u_label)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.stop_ambient_camera_rotation()
        self.move_camera(
            phi=0,
            theta=-PI/2, 
            added_anims=[
                FadeOut(minus_u),
                FadeOut(anti_clkwise),
                FadeOut(w_cross_v),
                FadeOut(minus_u_label),
                FadeOut(v_label, w_label),
                FadeOut(axes)    
            ],
        )
        self.wait(5)

        ##Section 2
        self.next_section(name="Linear Transformations", skip_animations=True)
        
        #Background shadows
        background_plane = NumberPlane(
            x_range=[-10,10],
            y_range=[-10,10],
            x_length=20,
            y_length=20,
            background_line_style={
                "stroke_color": GRAY, 
                "stroke_opacity": 0.5
            }
        )
        background_v = v.copy().set_opacity(0.5)
        background_w = w.copy().set_opacity(0.5)
        self.add(background_plane, background_v, background_w)
        
        #Matrices
        A = np.array([[1, 2], [2, 1]])
        B = np.array([[0, -1], [1, 0]])

        BA = MathTex(r"B{{A}}", font_size=81, color=ORANGE).to_corner(UL)
        AB = MathTex(r"{{A}}B", font_size=81, color=WHITE).to_corner(UL)

        #Transformations
        self.play(Write(BA))
        self.play(Indicate(BA))
        self.wait()
        A_vecs = self.linear_transform(plane, [v, w], [RED, GREEN], A, BA[1].animate.set_color(YELLOW).scale(1.2))
        BA_vecs = self.linear_transform(plane, A_vecs, [RED, GREEN], B, BA[1].animate.set_color(ORANGE).scale(1/1.2), BA[0].animate.set_color(YELLOW).scale(1.2))
        self.play(BA[0].animate.set_color(ORANGE).scale(1/1.2))
        self.wait(2)
        
        BA_shadow = BA_vecs.copy().set_color(ORANGE).set_opacity(0.5)
        self.add(BA_shadow)
        vecs = self.linear_transform(plane, BA_vecs, [RED, GREEN], np.linalg.inv(B @ A), FadeOut(background_v, background_w), FadeOut(BA))
        self.wait()
        
        self.play(Write(AB))
        self.play(Indicate(AB))
        self.wait()
        B_vecs = self.linear_transform(plane, vecs, [RED, GREEN], B, AB[1].animate.set_color(YELLOW).scale(1.2))
        AB_vecs = self.linear_transform(plane, B_vecs, [RED, GREEN], A, AB[1].animate.set_color(WHITE).scale(1/1.2), AB[0].animate.set_color(YELLOW).scale(1.2))
        self.play(AB[0].animate.set_color(WHITE).scale(1/1.2))
        self.wait(2)
        
        AB_shadow = AB_vecs.copy().set_color(WHITE).set_opacity(0.5)
        self.add(AB_shadow)
        vecs = self.linear_transform(plane, AB_vecs, [RED, GREEN], np.linalg.inv(A @ B), FadeOut(AB))
        self.wait()
        
        inequal = MathTex(r"AB \neq BA", font_size=81, substrings_to_isolate=[r"AB", r"BA"]). move_to(3*RIGHT + 0.5*DOWN)
        inequal.set_color_by_tex_to_color_map({"AB": GRAY, "BA": ORANGE})
        self.play(Write(inequal))
        self.wait(5)



class LinearArithmetic(VectorScene):
    def construct(self):
        
        ##Section 1
        self.next_section(name="Vector and matrix arithmetic", skip_animations=True)
        vector_addition = MathTex(
            r"\begin{bmatrix}"
            r"a_0 \\"
            r"a_1 \\"
            r"a_2 \\"
            r"\vdots \\"
            r"a_n"
            r"\end{bmatrix}"
            r"+"
            r"\begin{bmatrix}"
            r"b_0 \\"
            r"b_1 \\"
            r"b_2 \\"
            r"\vdots \\"
            r"b_n"
            r"\end{bmatrix}"
            r"="
            r"\begin{bmatrix}"
            r"a_0 + b_0 \\" 
            r"a_1 + b_1 \\" 
            r"a_2 + b_2 \\"
            r"\vdots \\"
            r"a_n + b_n"
            r"\end{bmatrix}" 
        )
        
        self.play(Write(vector_addition))
        self.wait(2)
        self.play(FadeOut(vector_addition))
        matrix_multiplication = MathTex(
            r"\begin{bmatrix}"
            r"a_{11} & a_{12} & \cdots & a_{1p} \\"
            r"a_{21} & a_{22} & \cdots & a_{2p} \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"a_{m1} & a_{m2} & \cdots & a_{mp}"
            r"\end{bmatrix}"
            r"\times"
            r"\begin{bmatrix}"
            r"b_{11} & b_{12} & \cdots & b_{1n} \\"
            r"b_{21} & b_{22} & \cdots & b_{2n} \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"b_{p1} & b_{p2} & \cdots & b_{pn}"
            r"\end{bmatrix}"
            r"= ~ \mathbf{?}",
            substrings_to_isolate=["?"],
            font_size=DEFAULT_FONT_SIZE
        )
        matrix_multiplication.set_color_by_tex("?", YELLOW)
        self.play(Write(matrix_multiplication))
        self.wait(5)
        
        ##Section 2
        self.next_section(name="New arithmetic", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        
        plane = self.add_plane(animate=True)
        vector = self.add_vector([3,2])
        self.wait()
        self.vector_to_coords(vector)
        self.wait(2)
        
        
        ##Section 3
        self.next_section(name="A shift in perspective", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        
        arithmetic_operations = MathTex(r"+, -, \times, \divisionsymbol", font_size=81)
        interoperation = MathTex(r"a \oplus b")
        
        self.play(Write(arithmetic_operations))
        self.wait(2)
        
        self.play(
            LaggedStart(
                FadeOut(arithmetic_operations),
                Write(interoperation),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        set_a = Ellipse(3, 4, stroke_color=RED, fill_color=RED, fill_opacity=0.5).move_to(2.5*LEFT).set_z_index(0)
        set_a.add(MathTex(r"a", font_size=64, color=RED).move_to(set_a.get_corner(DR) + 0.2*UL))
        set_c = Ellipse(3, 4, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.5).move_to(2.5*RIGHT).set_z_index(0)
        set_c.add(MathTex(r"c", font_size=64, color=GREEN).move_to(set_c.get_corner(DR) + 0.2*UL))
        
        operation_map = Line(2*LEFT + 0.5*UP, 2*RIGHT + 0.5*UP, path_arc=-1).add_tip().set_z_index(1)
        operation_map.add(MathTex(r"\oplus b", font_size=64).move_to(operation_map.point_from_proportion(0.55) + 0.5*UP))
        
        self.play(
            LaggedStart(
                FadeOut(interoperation, shift=LEFT),
                GrowFromCenter(set_a),
                lag_ratio=0.2
            )
        )
        self.play(
            AnimationGroup(
                Write(operation_map),
                GrowFromCenter(set_c)
            )
        )
        self.wait(5)
        
        ##Section 4
        self.next_section(name="Addition", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        
        addition = MathTex(r"{{2}} + 3", font_size=81).scale(0.6).move_to(2.5*UP)
        addition.add(SurroundingRectangle(addition, color=RED, buff=0.2, corner_radius=0.1, stroke_width=2))
        
        num_line = NumberLine(
            x_range=[-5,5],
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).set_z_index(0)
        
        path = VMobject(color=RED).set_z_index(1)
        dot = Dot(radius=0.1, point=num_line.number_to_point(2), color=BLUE).set_z_index(3)
        dot.generate_target()
        dot.target.move_to(num_line.number_to_point(5))
        dot_shadow = Circle(radius=0.1, color=YELLOW, stroke_width=1).move_to(dot.get_center()).set_z_index(2)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        
        self.play(
            LaggedStart(
                Write(addition),
                LaggedStart(
                    Write(num_line),
                    GrowFromCenter(dot),
                    lag_ratio=0.75
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.add(path)
        self.play(
            AnimationGroup(
                MoveToTarget(dot, run_time=1.5),
                FadeIn(dot_shadow, run_time=0.1)
            )
        )
        
        distance = BraceLabel(path, r"+3 units", brace_direction=UP, label_constructor=Tex)
        self.play(Write(distance, run_time=1.5))
        self.wait(5)
        
        self.play(
            AnimationGroup(
                ShrinkToCenter(dot),
                ShrinkToCenter(dot_shadow),
                FadeOut(distance, path)
            )
        )
        self.play(Indicate(num_line, scale_factor=1.1))
        self.wait()
        
        x = MathTex(r"x").move_to(num_line.number_to_point(5) + 0.5*UP)
        x_replacement = MathTex(r"x", font_size=81).scale(0.6).move_to(addition[0][0]).align_to(addition[0], DOWN, RIGHT)
        self.play(
            AnimationGroup(
                Write(x),
                ReplacementTransform(addition[0][0], x_replacement)
            )
        )
        self.wait(2)
        
        addition = VGroup(addition[0][1:], addition[1], x_replacement, addition[-1])
        x_to_y = MathTex(r"{{x}} \mapsto y {{= x+3}}").move_to(UP + 0.4*RIGHT)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    VGroup(num_line, x).animate.shift(1.5*DOWN),
                    TransformFromCopy(x, x_to_y[0])
                ),
                Write(x_to_y[1]),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Write(x_to_y[-1]))
        self.wait(3)
        
        num_line2 = num_line.copy().next_to(num_line, UP, buff=1.5)
        
        self.play(
            LaggedStart(
                Unwrite(x_to_y),
                Write(num_line2),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Indicate(VGroup(num_line, x), scale_factor=1.1))
        self.wait()
        self.play(Indicate(VGroup(num_line2), scale_factor=1.1))
        self.wait(5)
        
        y_line = NumberLine(
            x_range=[-2, 8],
            numbers_with_elongated_ticks=[3],
            include_numbers=True,
        ).scale(1.2).move_to(num_line2)
        y = MathTex(r"y").move_to(y_line.number_to_point(8) + 0.5*UP)
        self.play(ReplacementTransform(num_line2, y_line))
        self.wait()
        self.play(Write(y))
        self.wait(2)
        
        eye = SVGMobject(f'{SVGImages}\\Eye.svg').scale(0.2)
        y_perspective = eye.copy().rotate(PI).next_to(y_line, RIGHT, buff=0.1)
        self.play(FadeIn(y_perspective))
        self.wait()
        
        x_shift_line = Line(
            num_line.number_to_point(-3) + 0.5*UP,
            num_line.number_to_point(0) + 0.5*UP,
            color=YELLOW,
            stroke_width=2
        ).add_tip()
        x_shift_text = MathTex(r"{{3}} ~ \text{units}", color=YELLOW, font_size=36).next_to(x_shift_line, UP, buff=0.1)

        x_shift = VGroup(x_shift_line, x_shift_text)
        
        self.play(GrowFromEdge(x_shift, LEFT))
        self.wait(3)
        
        x_perspective = eye.copy().next_to(num_line, RIGHT, buff=0.1)
        y_shift_line = Line(
            y_line.number_to_point(3) + 0.9*DOWN,
            y_line.number_to_point(0) + 0.9*DOWN,
            color=YELLOW
        ).add_tip()
        y_shift_line.add(Tex(r"3 units", color=YELLOW, font_size=36).next_to(y_shift_line, DOWN, buff=0.1))
        
        self.play(
            LaggedStart(
                FadeOut(x_shift),
                ReplacementTransform(y_perspective, x_perspective),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(GrowFromEdge(y_shift_line,RIGHT))
        self.wait(3)
        self.play(FadeOut(x_perspective, y_shift_line))
        self.wait(2)
        
        line_array = VGroup()
        for i in range(-5,6):
            if i != 0:
                line_array.add(
                    DashedLine(
                        start=y_line.number_to_point(i+3)+0.7*DOWN,
                        end=num_line.number_to_point(i)+0.15*UP,
                        color=YELLOW
                    )
                )
            else:
                line_array.add(
                    DashedLine(
                        start=y_line.number_to_point(i+3)+0.7*DOWN,
                        end=num_line.number_to_point(i)+0.25*UP,
                        color=YELLOW
                    )
                )
                
        self.play(Write(line_array), x.animate.shift(0.5*RIGHT))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                Circumscribe(num_line[2][7]),
                VGroup(*line_array[:7], *line_array[8:], x, y, addition[:-1]).animate.set_opacity(0.5),
                addition[-1].animate.set_stroke(opacity=0.5)
            )
        )
        self.wait(2)
        
        x_circle = Ellipse(width=0.8).move_to(num_line.number_to_point(2) + 0.3*DOWN)
        y_circle = Ellipse(width=0.8).move_to(y_line.number_to_point(5) + 0.25*DOWN)
        
        self.play(Write(x_circle))
        self.wait()
        self.play(Wiggle(line_array[7]))
        self.wait()
        self.play(Write(y_circle))
        self.wait(2)
        
        self.play(
            AnimationGroup(
                VGroup(y, addition[:-1]).animate.set_opacity(1),
                addition[-1].animate.set_stroke(opacity=1),
                FadeOut(x_circle, y_circle, line_array),
                x.animate.shift(0.5*LEFT).set_opacity(1)
            )
        )
        self.wait()
        self.play(GrowFromEdge(x_shift, LEFT))
        self.wait(2)
        
        c = MathTex(r"c", font_size=81).scale(0.6).move_to(addition[1][-1]).align_to(addition[-2], DOWN, RIGHT)
        c_units = MathTex(r"c", color=YELLOW, font_size=36).move_to(x_shift_text[0]).align_to(x_shift_text, DOWN, RIGHT)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(addition[1][-1], c),
                ReplacementTransform(x_shift_text[0], c_units)
            )
        )
        self.wait(5)
        
        ax = Axes(axis_config={"color": GRAY})
        ax_labels = ax.get_axis_labels(y_label="f(x)")
        axes = VGroup(ax, ax_labels)
        
        f = ax.plot(lambda x: 0.6*x**3 - 0.5*x, color=RED, stroke_width=4)
        point = Dot(ax.coords_to_point(0,0), color=BLUE)
        plot = VGroup(f, point)
        self.play(
            AnimationGroup(
                ReplacementTransform(VGroup(num_line, y_line), ax),
                ReplacementTransform(x, ax_labels[0]),
                ReplacementTransform(y, ax_labels[-1]),
                FadeOut(addition, c, c_units, x_shift_line, x_shift_text[-1], )
            )
        ) 
        
        self.play(
            LaggedStart(
                Write(f, run_time=2),
                GrowFromCenter(point),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        new_y_label = MathTex(r"f(x+c)", font_size=40, substrings_to_isolate=r"c").move_to(ax_labels[-1])
        new_y_label.set_color_by_tex("c", YELLOW)
        c = MathTex(r"c", font_size=36, color=YELLOW).move_to(ax.coords_to_point(-3, -0.5))
        self.play(
            LaggedStart(
                ReplacementTransform(ax_labels[-1], new_y_label),
                plot.animate.shift(ax.get_x_unit_size()*3*LEFT),
                Write(c),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.play(Circumscribe(ax_labels[-1]))
        self.wait()
        self.play(Circumscribe(ax_labels[0]))
        self.wait(5)
        
        ##Section 5
        self.next_section(name="Multiplication", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        multiplication = MathTex(r"x {{\times}} 3", font_size=49)
        box = SurroundingRectangle(multiplication, color=RED, buff=0.2, corner_radius=0.1, stroke_width=2)
        VGroup(multiplication, box).move_to(2.5*UP)
        
        x_line = NumberLine(
            x_range=[-3,3],
            length=10,
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).move_to(1.5*DOWN)
        x = MathTex(r"x").move_to(x_line.number_to_point(3) +0.5*UP)
        
        num_line2 = x_line.copy().next_to(x_line, UP, buff=1.5)
        y_line = NumberLine(
            x_range=[-9,9],
            length=10,
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).next_to(x_line, UP, buff=1.5)
        y = MathTex(r"y").move_to(y_line.number_to_point(9) +0.5*UP)
        
        self.play(
            LaggedStart(
                Write(VGroup(multiplication, box)),
                Write(VGroup(x_line, x)),
                Write(num_line2),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                ReplacementTransform(num_line2, y_line),
                Write(y),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        y_perspective = eye.copy().rotate(PI).next_to(y_line, RIGHT, buff=0.1)
        line_array = VGroup()
        for i in range(-3,4):
            if i != 0:
                line_array.add(
                    DashedLine(
                        start = y_line.number_to_point(i) + 0.7*DOWN,
                        end= x_line.number_to_point(i) + 0.15*UP,
                        color=YELLOW
                    )
                )
            else:
                line_array.add(
                    DashedLine(
                        start = y_line.number_to_point(i) + 0.7*DOWN,
                        end= x_line.number_to_point(i) + 0.25*UP,
                        color=YELLOW
                    )
                )
        x_stretch = VGroup()
        for i in [-1,1]:
            x_stretch.add(
                Line(
                    start= x_line.number_to_point(i*0.04) + 0.5*UP,
                    end = x_line.number_to_point(i) + 0.5*UP,
                    color=YELLOW
                ).add_tip()
            )
        
        self.play(Write(line_array))
        self.wait(2)
        self.play(FadeIn(y_perspective))
        self.play(
            LaggedStart(
                FadeOut(line_array),
                AnimationGroup(
                    GrowFromEdge(x_stretch[0], RIGHT),
                    GrowFromEdge(x_stretch[1], LEFT)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        ##Section 6
        self.next_section(name="Division", skip_animations=True)
        new_x_line = NumberLine(
            x_range=[-6,6],
            length=10,
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).move_to(1.5*DOWN)
        
        new_num_line2 = new_x_line.copy().next_to(new_x_line, UP, buff=1.5)
        
        self.play(
            LaggedStart(
                FadeOut(x_stretch, y_perspective),
                AnimationGroup(
                    ReplacementTransform(x_line, new_x_line),
                    ReplacementTransform(y_line, new_num_line2),
                    FadeOut(y)
                    ),
                lag_ratio=0.5
            )
        )
        self.wait()
        
        division_symbol = MathTex(r"\divisionsymbol", font_size=81).scale(0.6).move_to(multiplication[1], aligned_edge=DOWN)
        new_y_line = NumberLine(
            x_range=[-2,2],
            length=10,
            numbers_with_elongated_ticks=[0],
            include_numbers=True,
        ).scale(1.2).next_to(x_line, UP, buff=1.5)
        new_y = MathTex(r"y").move_to(new_y_line.number_to_point(2) + 0.5*UP)
        
        line_array = VGroup()
        for i in range(-2,3):
            if i != 0:
                line_array.add(
                    DashedLine(
                        start = new_y_line.number_to_point(i) + 0.7*DOWN,
                        end= new_x_line.number_to_point(i) + 0.15*UP,
                        color=YELLOW
                    )
                )
            else:
                line_array.add(
                    DashedLine(
                        start = new_y_line.number_to_point(i) + 0.7*DOWN,
                        end= new_x_line.number_to_point(i) + 0.25*UP,
                        color=YELLOW
                    )
                )
        x_squish = VGroup()
        for i in [-1,1]:
            x_squish.add(
                Line(
                    start = x_line.number_to_point(i) + 0.5*UP,
                    end= x_line.number_to_point(i*0.04) + 0.5*UP,
                    color=YELLOW
                ).add_tip()
            )
        
        self.play(
            LaggedStart(
                ReplacementTransform(multiplication[1], division_symbol),
                LaggedStart(
                    ReplacementTransform(new_num_line2, new_y_line),
                    Write(new_y),
                    lag_ratio=0.5
                ),
                lag_ratio=1
            )
        )
        self.wait()
        self.play(Write(line_array))
        self.wait(2)
        self.play(FadeIn(y_perspective))
        self.play(
            LaggedStart(
                FadeOut(line_array),
                AnimationGroup(
                    GrowFromEdge(x_squish[0], LEFT),
                    GrowFromEdge(x_squish[1], RIGHT)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
class Test(VectorScene):
    def construct(self):
        # self.add(NumberPlane())
        ################################################################Imports#################################################################################
        eye = SVGMobject(f'{SVGImages}\\Eye.svg').scale(0.2)
        ########################################################################################################################################################
        return
   


class Additions(Scene):
    def construct(self):
        
        ##Section 1
        self.next_section(name="Adder Circuit", skip_animations=False)
        adder_circuit = SVGMobject(f'{SVGImages}\\HalfAdder.svg').set_color(WHITE).scale(1.5)
        self.play(Write(adder_circuit))
        self.wait()
        
        
        