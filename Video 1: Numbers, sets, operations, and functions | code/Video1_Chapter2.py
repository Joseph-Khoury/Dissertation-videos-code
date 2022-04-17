from manim import *

SVGImages = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\SVGImages"
Images = r"D:\Files\OneDrive - Heriot-Watt University\Uni work\Yr 4\Dissertation\Videos\1 - Numbers, sets, infinities, and functions\Images"

class Scene1(Scene):
    def construct(self):
        #Section 1
        self.next_section(name="Questioning cardinal numbers", skip_animations=True)
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
            MathTex(r"\vdots").next_to(apples[2], DOWN).shift(0.25*LEFT),
            MathTex("9"),
            MathTex(r"\vdots").shift(0.25*LEFT)
        ).shift(0.25*RIGHT)
        
        apples[-1].next_to(apples_text[3], DOWN)
        apples_text[-2].next_to(apples[3], RIGHT).shift(0.75*RIGHT)
        apples_text[-1].next_to(apples[-1], DOWN)
        
        cardinal_numbers_image = VGroup(apples,apples_text).copy()
        
        stickman = SVGMobject(f'{SVGImages}\\ThinkingStickman.svg').set_stroke(color=WHITE, width=3).to_corner(DL, buff=1).shift(RIGHT)
        
        question_marks = Text("??", font_size=70, color=YELLOW).next_to(stickman, UR, buff=0)
        
        self.play(
            FadeIn(
                VGroup(
                    apples, 
                    apples_text
                )
            )
        )
        self.wait(5)
        
        self.play(
            LaggedStart(
                Write(stickman),
                GrowFromEdge(question_marks, DL),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        #Section 2
        self.next_section(name="number concepts", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        num_line = NumberLine(
            x_range=[-5,6],
            include_ticks=True,
            include_numbers=True,
            numbers_to_exclude=[-6,6],
            numbers_with_elongated_ticks=[0],
            include_tip=True,
            font_size=36,
            line_to_number_buff=MED_SMALL_BUFF
        )

        nums = num_line.submobjects[2]
        num_line.submobjects.remove(num_line.submobjects[2])

        init_line = VGroup(num_line, nums[6:]) 
        zero = nums[5]
        neg_nums = nums[4::-1]

        UP_BUFF = 0.38
        FRAC_UP_BUFF = 0.55
        LEFT_BUFF = 0.15

        half = VGroup(num_line.get_tick(1/2, 0.05))
        half.add(MathTex(r"\frac{1}{2}",font_size=36).move_to(num_line.number_to_point(0.5)+FRAC_UP_BUFF*UP))

        neg_5_over_3 = VGroup(num_line.get_tick(-5/3,0.05))
        neg_5_over_3.add(MathTex(r"-\frac{5}{3}",font_size=36).move_to(num_line.number_to_point(-5/3)+FRAC_UP_BUFF*UP+LEFT_BUFF*LEFT))

        sqrt_2 = VGroup(num_line.get_tick(np.sqrt(2),0.05))
        sqrt_2.add(MathTex(r"\sqrt{2}",font_size=36).move_to(num_line.number_to_point(np.sqrt(2))+UP_BUFF*UP))

        pi = VGroup(num_line.get_tick(PI,0.05))
        pi.add(MathTex(r"\pi",font_size=36).move_to(num_line.number_to_point(PI)+UP_BUFF*UP))

        self.play(Write(init_line))
        self.wait()
        self.play(Write(zero))
        self.wait()
        self.play(Write(neg_nums))
        self.wait()
        self.play(
            LaggedStart(
                Write(half),
                Write(neg_5_over_3),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                Write(sqrt_2),
                Write(pi),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        ##Section 3
        self.next_section(name="Pythagorean controversy",skip_animations=True)
        pythagoras_image = ImageMobject(f'{Images}\\SchoolOfAthens.jpg').scale(0.4).to_corner(UR, buff=0.5)
        self.play(FadeIn(pythagoras_image))
        self.wait(2)
        
        ##Section 4
        self.next_section(name="Quantify zero",skip_animations=True)
        zero_text = MathTex(r"=0")
        question_mark = Text("?", color=YELLOW).next_to(zero_text,RIGHT)
        point = Dot(radius=0).next_to(zero_text, LEFT, buff=1)
        self.play(
            FadeOut(VGroup(init_line,zero,neg_nums,half,neg_5_over_3,sqrt_2,pi)),
            FadeOut(pythagoras_image)
        )
        self.wait()
        self.play(Flash(point, flash_radius=0.5))
        self.wait()
        self.play(FadeIn(zero_text,shift=RIGHT))
        self.wait()
        self.play(Write(question_mark))
        self.wait(2)
        
        ##Section 5 
        self.next_section(name="Negative numbers",skip_animations=True)
        inv_apple = SVGMobject(f'{SVGImages}\\InvertedApple.svg').scale(0.5)
        row_of_inv_apples = VGroup(
            inv_apple.copy().shift(0.75*LEFT),
            inv_apple.copy(),
            inv_apple.copy().shift(0.75*RIGHT)
        )
        inv_apples = VGroup(
            inv_apple.copy().to_edge(UP),
            VGroup(
                inv_apple.copy().shift(0.35*LEFT + 1.75*UP),
                inv_apple.copy().shift(0.35*RIGHT + 1.75*UP)
            ),
            row_of_inv_apples.copy().shift(0.5*UP),
            VGroup(
                row_of_inv_apples.copy().shift(2.5*UP),
                row_of_inv_apples.copy().shift(1.25*UP),
                row_of_inv_apples.copy()
            ).scale(0.5).to_edge(DOWN)
            
        )
        inv_apples_text = VGroup(
            MathTex("-1").next_to(inv_apples[0], RIGHT),
            MathTex("-2").next_to(inv_apples[1], RIGHT),
            MathTex("-3").next_to(inv_apples[2], RIGHT),
            MathTex(r"\vdots").next_to(inv_apples[2], DOWN).shift(0.25*LEFT),
            MathTex("-9"),
            MathTex(r"\vdots").shift(0.25*LEFT)
        ).shift(0.25*RIGHT)
        
        inv_apples[-1].next_to(inv_apples_text[3], DOWN)
        inv_apples_text[-2].next_to(inv_apples[3], RIGHT).shift(0.75*RIGHT)
        inv_apples_text[-1].next_to(inv_apples[-1], DOWN)
        
        question_marks = VGroup(
            MathTex(r"?", font_size=150, color=YELLOW).next_to(VGroup(inv_apples,inv_apples_text),RIGHT,buff=1.8),
            MathTex(r"?", font_size=150, color=YELLOW).next_to(VGroup(inv_apples,inv_apples_text),LEFT,buff=2)
        )
        self.play(
            LaggedStart(
                FadeOut(VGroup(zero_text, question_mark)),
                FadeIn(VGroup(inv_apples,inv_apples_text)),
                lag_ratio=1
            )
        )
        self.play(Write(question_marks))
        self.wait(5)        
        
        ##Section 6
        self.next_section(name="Sqrt(-1) apples",skip_animations=True)
        sqrt_neg_1 = MathTex(r"\sqrt{-1}=").shift(LEFT)
        imaginary_apple = VGroup(apple.copy().next_to(sqrt_neg_1, RIGHT, buff=0.3)).shift(0.1*UP)
        imaginary_apple.add(MathTex(r"\times ??").next_to(imaginary_apple, RIGHT).shift(0.1*DOWN))
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(inv_apples,inv_apples_text,question_marks)),
                Write(VGroup(sqrt_neg_1,imaginary_apple),run_time=2),
                lag_ratio=1
            )
        )
        self.wait(5)
        
        ##Section 7
        self.next_section(name="Questions about numbers",skip_animations=True)
        question1 = VGroup(point,zero_text,question_mark)
        question1.add(SurroundingRectangle(question1,color=WHITE)).to_edge(UP)
        question2 = VGroup(inv_apples,inv_apples_text,question_marks)
        question2.add(SurroundingRectangle(question2,color=WHITE)).scale(0.65).next_to(question1,DOWN)
        question3 = VGroup(sqrt_neg_1,imaginary_apple)
        question3.add(SurroundingRectangle(question3,color=WHITE))
        
        self.play(
            LaggedStart(
                Write(question3[-1]),
                question3.animate.next_to(question2,DOWN),
                lag_ratio=0.5
            )
        )
        self.play(FadeIn(VGroup(question1,question2)))
        self.wait(5)
        
        ##Section 8 
        self.next_section(name="Abstracting numbers",skip_animations=True)
        cardinal_numbers = VGroup(apples,apples_text).scale(0.7).to_corner(DL,buff=1).shift(RIGHT)
        
        self.play(
            LaggedStart(
                FadeOut(VGroup(question1,question3,question2[-1],question2[-2])),
                ReplacementTransform(question2[:-2],cardinal_numbers),
                lag_ratio=0.5
            )
        )
        self.wait()
        thought_bubble = SVGMobject(f'{SVGImages}\\ThoughtCloud.svg').set_color(WHITE).scale(1.2).to_edge(RIGHT,buff=1.5).shift(0.1*DOWN)
        large_bubble = Circle(radius = 0.25, color=WHITE).next_to(thought_bubble,DL,buff=0.8)
        thought_text = MathTex(r"ax^2+bx+c=0").move_to(thought_bubble).scale(0.8)
        thought = VGroup(thought_bubble,thought_text)
        
        arrow = Line(
            cardinal_numbers.get_right() + 0.5*RIGHT + 0.3*UP,
            thought.get_left() + 0.5*LEFT + 0.2*DOWN,
            stroke_width=2
        ).add_tip(tip_length=0.3)
        
        self.play(
            LaggedStart(
                GrowFromEdge(arrow,LEFT),
                FadeIn(thought),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        self.play(
            AnimationGroup(
                FadeOut(VGroup(cardinal_numbers, arrow), shift=LEFT, run_time=0.5),
                thought.animate.move_to(ORIGIN).scale(2)
            )
        )
        self.wait(2)
        self.play(ShowPassingFlash(thought_bubble.copy().set_color(YELLOW), time_width=0.5), run_time=2)
        self.wait(2)
        self.play(FadeOut(thought))
        self.wait()
        
        ##Section 9
        self.next_section(name="Set Introduction",skip_animations=True)
        apple = SVGMobject(f'{SVGImages}\\Apple.svg').shift(0.5*UP)
        orange = SVGMobject(f'{SVGImages}\\Orange.svg').scale(0.7)
        
        apple1 = apple.copy()
        apple2 = apple.copy().next_to(apple1, LEFT).align_to(apple,ORIGIN)
        orange1 = orange.copy().next_to(apple1, RIGHT).align_to(apple,DOWN, RIGHT)
        
        apple_text = Tex(r"Apple").next_to(apple, DOWN, buff=1)
        added_s = Tex("s").next_to(apple_text,RIGHT,buff=0.05).shift(0.02*DOWN)
        apples_text = VGroup(apple_text,added_s)
        one = MathTex("1").next_to(apple_text, LEFT).shift(0.035*UP)
        two = MathTex("2").move_to(one)
        three = MathTex("3").move_to(two) 
        cross = MathTex(r"\times",font_size=250,color=PURE_RED).move_to(VGroup(three,apples_text))
        question_mark = Tex("?",color=YELLOW).next_to(apples_text,RIGHT).align_to(three,DOWN,RIGHT)
        
        self.play(GrowFromCenter(apple1))
        self.wait(2)
        self.play(Write(VGroup(one,apple_text)))
        self.wait(4)
        self.play(
            AnimationGroup(
                GrowFromCenter(apple2),
                ReplacementTransform(one,two),
                FadeIn(added_s)
            )
        )
        self.wait(4)
        self.play(GrowFromCenter(orange1))
        self.play(
            AnimationGroup(
                ReplacementTransform(two,three),
                FadeIn(question_mark),
                lag_ratio=1
            )
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                GrowFromCenter(cross,run_time=0.5),
                FadeOut(question_mark,run_time=0.5)
            )
        )
        self.wait(5)
        
        ##Section 10
        self.next_section(name="apples are not oranges",skip_animations=True)
        neq = MathTex(r"\neq",font_size=150)
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(VGroup(apples_text,three,cross,apple2),run_time=0.5),
                    apple1.animate.move_to(2*LEFT).align_to(0.5*DOWN,DOWN,RIGHT),
                    orange1.animate.move_to(2*RIGHT).align_to(0.5*DOWN,DOWN,RIGHT)
                ),
                Write(neq.move_to(0.2*UP)),
                lag_ratio=1
            )
        )
        self.wait(5)
        
        ##Section 11
        self.next_section(name="2 apples and 1 orange",skip_animations=True)
        apple1.generate_target()
        apple1.target.shift(2*LEFT)
        apple2.next_to(apple1.target, RIGHT)
        apples_text = Tex(r"2 Apples").next_to(VGroup(apple1.target,apple2),DOWN,buff=0.5)
        and_text = Tex("\&",font_size=100).move_to(neq)
        orange1.generate_target()
        orange1.target.shift(RIGHT)
        orange_text = Tex(r"1 Orange").next_to(orange1.target,DOWN,buff=0.5)
        
        self.play(
            LaggedStart(
                LaggedStart(
                    AnimationGroup(
                        MoveToTarget(apple1),
                        FadeOut(neq,run_time=0.5),
                        MoveToTarget(orange1)
                    ),
                    FadeIn(apple2),
                    lag_ratio=0.5   
                ),
            FadeIn(VGroup(apples_text,orange_text)),
            FadeIn(and_text),
            lag_ratio=1
            )
        )
        self.wait(5)
        
        ##Section 12
        self.next_section(name="Categorizing",skip_animations=True)
        eye_original = SVGMobject(f'{SVGImages}\\Eye.svg').scale(0.5)
        eye = eye_original.copy()
        timeline = NumberLine(
            x_range=[0,1],
            length=6,
            include_ticks=True, 
            tick_size=0.3,
            )
        start_point = timeline.number_to_point(0)
        end_point = timeline.number_to_point(1)
        eye.move_to(start_point + 2*DOWN)
        
        line_of_sight = DashedLine(
            eye.get_top() + SMALL_BUFF*UP,
            start_point + (MED_SMALL_BUFF + 0.15)*DOWN,
            color=YELLOW
        )
        
        start_group = VGroup(apple.copy())
        start_group.add(apple.copy().next_to(start_group[0],LEFT).align_to(apple,ORIGIN))
        start_group.add(orange.copy().next_to(start_group[0],RIGHT).align_to(apple,DOWN,RIGHT))
        start_group.scale(0.4)\
            .move_to(start_point + (0.5+MED_SMALL_BUFF)*UP)
        
        end_group = VGroup(apple1,apple2,orange1,apples_text,and_text,orange_text)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    end_group.animate.scale(0.3).move_to(end_point + (0.5+MED_SMALL_BUFF)*UP),
                    Write(timeline)
                ),
                FadeIn(start_group),
                FadeIn(eye),
                Write(line_of_sight),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        categorizing_tick = timeline.get_tick(0.5,0.15)
        
        apple3 = apple.copy().shift(1.5*LEFT).scale(0.7)
        apple4 = apple3.copy().shift(1.5*UP)
        apple_set = VGroup(apple3,apple4)
        orange2 = orange.copy().next_to(apple3,RIGHT,buff=1.5).align_to(apple,DOWN,RIGHT)
        orange_set = VGroup(orange2)
        apple_braces = VGroup(
                Brace(apple_set,LEFT),
                Brace(apple_set,RIGHT)
            )
        orange_braces = VGroup(
                Brace(orange2,LEFT),
                Brace(orange2,RIGHT)
            )
        apple_set.add(apple_braces).align_to(apple,DOWN,RIGHT)
        orange_set.add(orange_braces).align_to(apple,DOWN,RIGHT)
        
        sets = VGroup(apple_set,orange_set).scale(0.4).move_to(timeline.number_to_point(0.5) + UP)
        eye1 = eye.copy()
        
        self.play(
            AnimationGroup(
                VGroup(start_group,end_group,timeline).animate.set_opacity(0.5),
                FadeOut(eye,line_of_sight),
                Write(categorizing_tick),
                FadeIn(VGroup(apple3,apple4,orange2))
            )
        )
        self.wait(2)
        self.play(FadeIn(VGroup(apple_braces,orange_braces)))
        self.wait(2)
        self.play(
            AnimationGroup(
                VGroup(start_group,end_group,timeline).animate.set_opacity(1),
                FadeIn(eye1,line_of_sight)
            )
        )
        self.wait(5)
        
        ##Section 13
        self.next_section(name="Types of objects",skip_animations=True)
        self.play(
            AnimationGroup(
                FadeOut(
                    timeline,
                    eye1,line_of_sight,
                    start_group,
                    apple_set,
                    orange_set,
                    categorizing_tick,
                    apples_text, 
                    and_text,
                    orange1,
                    orange_text
                ),
                VGroup(apple1,apple2).animate.scale(3).move_to(ORIGIN)
            )
        ),
        self.wait(3)
        
        apple_positions = [apple1.get_center(),apple2.get_center()]
        equality = MathTex(r"=",font_size=150)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    apple1.animate.next_to(equality,LEFT,buff=0.5).shift(0.3*UP),
                    apple2.animate.next_to(equality,RIGHT,buff=0.5).shift(0.3*UP)
                ),
                Write(equality),
                lag_ratio=0.7
            )
        )
        self.wait(2)
        
        self.play(
            AnimationGroup(
                FadeOut(equality),
                apple1.animate.move_to(apple_positions[0]),
                apple2.animate.move_to(apple_positions[1])
            )
        )
        self.wait()
        
        apple_braces = VGroup(
            Brace(apple1,LEFT),
            Brace(apple2,RIGHT)
        )
        apples_text = Tex(r"2 Apples").next_to(VGroup(apple1,apple2,apple_braces),DOWN,buff=1)
        
        self.play(
            AnimationGroup(
                FadeIn(apple_braces),
                Write(apples_text)
            )
        )
        self.wait(5)
        
        apples = VGroup(apple1,apple2)
        apples.generate_target()
        apples.target.shift(LEFT)
        orange1.scale(3).next_to(apples.target, RIGHT).align_to(apples.target,DOWN, RIGHT)
        
        self.play(
            LaggedStart(
                FadeOut(apple_braces,apples_text),
                AnimationGroup(
                    MoveToTarget(apples),
                    FadeIn(orange1,shift=LEFT)
                ),
                lag_ratio=1
            )
        )
        self.wait(3)
        
        fruit_positions = [apple1.get_center(),orange1.get_center()]
        neq = MathTex(r"\neq",font_size=150)
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(apple2,shift=DOWN,run_time=0.5),
                    apple1.animate.next_to(neq,LEFT,buff=0.5).shift(0.3*UP),
                    orange1.animate.next_to(neq, RIGHT,buff=0.5)
                ),
                Write(neq),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        self.play(
            AnimationGroup(
                FadeOut(neq),
                apple1.animate.move_to(fruit_positions[0]),
                orange1.animate.move_to(fruit_positions[1]),
                FadeIn(apple2,shift=UP)
            )
        )
        self.wait(3)
        
        apples.target.shift(LEFT)
        orange1.generate_target()
        orange1.target.shift(RIGHT)
        apple_braces = apple_braces.move_to(apples.target)
        orange_braces = VGroup(
            Brace(orange1.target,LEFT),
            Brace(orange1.target,RIGHT)
        )
        apples_text = apples_text.next_to(apples.target,DOWN,buff=1)
        orange_text = Tex(r"1 Orange").next_to(orange1.target,DOWN,buff=1)
        
        fruit_braces = VGroup(apple_braces,orange_braces)
        fruit_text = VGroup(apples_text,orange_text)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    MoveToTarget(apples),
                    MoveToTarget(orange1)
                ),
                AnimationGroup(
                    FadeIn(fruit_braces),
                    Write(fruit_text)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        types_of_objects = Tex(r'"Types of objects"').to_edge(UP,buff=2)
        equality.scale(0.5)
        sets_text = Tex(r'"Sets"').to_edge(DOWN,buff=2)
        
        self.play(
            LaggedStart(
                FadeOut(apples,orange1,fruit_braces,fruit_text),
                Write(types_of_objects),
                lag_ratio=1
            )
        )
        self.wait(2)
        self.play(Write(VGroup(equality,sets_text)))
        self.wait(3)
        
        self.play(Circumscribe(sets_text)),
        self.wait(5)
        
        ##Section 14
        self.next_section(name="Sets",skip_animations=True)
        set_word = Tex("Set").move_to(4*LEFT + 1.5*UP)
        set_pronunciation = Tex(r"\textit{\slash S$\varepsilon$t\slash}",font_size=36,color=GRAY).next_to(set_word,RIGHT,buff=0.5)
        Tex.set_default(font_size=32)
        noun = Tex("NOUN",color=RED).next_to(set_word,DOWN,buff=0.5).align_to(set_word,LEFT)
        set_category = Tex(r"Mathematics:",color=YELLOW).next_to(noun,DOWN,buff=0.75).align_to(noun,LEFT)
        set_definition = Tex(r"A collection of ").next_to(set_category,RIGHT,buff=0.2).align_to(set_category,DOWN,RIGHT)
        elements = Tex(r"elements").next_to(set_definition, RIGHT, aligned_edge=DOWN, buff=0.1)
        numbers = Tex(r"numbers").next_to(set_definition, RIGHT, aligned_edge=DOWN, buff=0.1)
        objects = Tex(r"objects").next_to(set_definition, RIGHT, aligned_edge=UP, buff=0.1)
        actions = Tex(r"actions").next_to(set_definition, RIGHT, aligned_edge=DOWN, buff=0.1)
        things = Tex(r"things").next_to(set_definition, RIGHT, aligned_edge=UP, buff=0.1)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(types_of_objects,shift=UP),
                    FadeOut(equality),
                    FadeOut(sets_text,shift=DOWN) 
                ),
                Write(
                    VGroup(
                        set_word,
                        set_pronunciation,
                        noun,
                        set_category,
                        set_definition,
                        elements
                    )
                ),
                lag_ratio=1
            )
        )
        self.wait(5)
        self.play(ReplacementTransform(elements,numbers))
        self.wait(2)
        self.play(ReplacementTransform(numbers,objects))
        self.wait(2)
        self.play(ReplacementTransform(objects,actions))
        self.wait(2)
        self.play(ReplacementTransform(actions,things))
        self.wait(5)
        
        ##Section 15
        self.next_section(name="Graphical representation of sets",skip_animations=True)
        self.play(ShrinkToCenter(VGroup(set_word,set_pronunciation,noun,set_category,set_definition,things)))
        self.wait()
        diagram = Ellipse(width=3,height=4,fill_opacity=0.2)#.shift(0.5*UP)
        elements = VGroup(
            MathTex(r"1"),
            MathTex(r"2"),
            MathTex(r"3"),
            MathTex(r"4"),
            MathTex(r"5"),
            MathTex(r"6")
        )
        elements[0].move_to(diagram.get_center()+1.2*UP +0.3*RIGHT)
        elements[1].move_to(diagram.get_center()+0.7*UP + 0.5*LEFT)
        elements[2].move_to(diagram.get_center()+0.6*RIGHT)
        elements[3].move_to(diagram.get_center()+0.4*DOWN + 0.8*LEFT)
        elements[4].move_to(diagram.get_center()+0.8*DOWN+0.7*RIGHT)
        elements[5].move_to(diagram.get_center()+1.3*DOWN + 0.3*LEFT)
        set_label = MathTex(r"A", color = RED, font_size=64).move_to(diagram.get_corner(DR) + 0.1*UL)

        self.play(
            LaggedStart(
                DrawBorderThenFill(diagram),
                Write(elements),
                Write(set_label),
                lag_ratio=0.8
            )
        )
        self.wait(5)
        
        set_diagram_group = VGroup(diagram,elements,set_label)
        set_diagram_copy = set_diagram_group.copy()
        set_diagram_group.generate_target()
        set_diagram_group.target.shift(UP)
        
        set_notation = MathTex(r"= \{1,2,3,4,5,6\}").next_to(set_diagram_group.target,DOWN,buff=1).shift(0.5*RIGHT)
        A = set_label.copy().next_to(set_notation,LEFT,buff=0.2)
        
        self.play(
            AnimationGroup(
                MoveToTarget(set_diagram_group),
                Write(VGroup(A,set_notation)),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        ##Section 16
        self.next_section(name="Previous example in the language of sets",skip_animations=True)
        apple1 = apple.copy()
        apple2 = apple.copy().next_to(apple1, LEFT).align_to(apple,ORIGIN)
        orange1 = orange.copy().next_to(apple1, RIGHT).align_to(apple,DOWN, RIGHT)
        
        self.play(FadeOut(*self.mobjects))
        self.wait()
        apples = VGroup(apple1,apple2)
        self.play(GrowFromCenter(VGroup(apples,orange1)))
        self.wait(2)
        
        apples.generate_target()
        apples.target.shift(1.5*LEFT)
        
        apples_set = VGroup()
        apples_set.add(Ellipse(width=4,height=3.5).move_to(apples.target.get_center() + 0.1*DOWN))
        apples_set.add(MathTex(r"A",color=RED,font_size=64).move_to(apples_set.get_corner(DR) + 0.3*UL))
        
        self.play(
            AnimationGroup(
                MoveToTarget(apples),
                Write(apples_set),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(Indicate(apples))
        self.wait(5)
        
        orange_set = VGroup()
        orange_set.add(Ellipse(width=3,height=2.75,color=ORANGE).move_to(orange1))
        orange_set.add(MathTex(r"O",color=ORANGE,font_size=64).move_to(orange_set.get_corner(DR) + 0.1*UL))
        
        self.play(
            AnimationGroup(
                VGroup(apples, apples_set[1]).animate.set_opacity(0.5),
                apples_set[0].animate.set_stroke(opacity=0.5),
                Write(orange_set)
            )
        )
        self.wait()
        self.play(Indicate(orange1))
        self.play(
            AnimationGroup(
                VGroup(apples, apples_set[1]).animate.set_opacity(1),
                apples_set[0].animate.set_stroke(opacity=1)
            )
        )
        self.wait(3)
        
        S = VGroup()
        S.add(Ellipse(width=10,height=5.5,color=YELLOW).shift(0.2*UP + 0.5*LEFT))
        S.add(MathTex(r"S",font_size=64,color=YELLOW).move_to(S.get_corner(DR) + 0.7*UL))
        
        self.play(Write(S,run_time=1.5))
        self.wait(5)
        
        F = VGroup()
        F.add(Ellipse(width=12,height=7.5,color=GREEN).move_to(S.get_center() + 0.2*DOWN))
        F.add(MathTex(r"F",font_size=64,color=GREEN).move_to(F.get_corner(DR) + 0.8*UL))
        banana = SVGMobject(f'{SVGImages}\\Banana.svg').scale(0.4).next_to(S,DOWN,buff=0.3).set_stroke(width=1)
        strawberry = SVGMobject(f'{SVGImages}\\Strawberry.svg').scale(1.2).next_to(banana,LEFT).shift(0.7*DOWN).set_stroke(width=1)
        ellipsis = MathTex(r"\dots",font_size=64).next_to(banana,RIGHT,buff=0.5)
        fruits = VGroup(strawberry,banana)
        
        self.play(
            LaggedStart(
                Write(F,run_time=1.5),
                LaggedStart(
                    Write(fruits),
                    Write(ellipsis),
                    lag_ratio=0.8
                ),
                lag_ratio=1
            )
        )
        self.wait(5)
        
        self.play(
            AnimationGroup(
                VGroup(S[0],F[0]).animate.set_stroke(opacity=0.1),
                VGroup(S[1],F[1],fruits,ellipsis).animate.set_opacity(0.1)
            )
        )
        self.play(Indicate(VGroup(apples_set[1],orange_set[1])))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                F[0].animate.set_stroke(opacity=1),
                VGroup(F[1],fruits,ellipsis).animate.set_opacity(1),
                orange_set[0].animate.set_stroke(opacity=0.1),
                VGroup(orange_set[1],orange1).animate.set_opacity(0.1)
            )
        )
        self.play(Indicate(VGroup(apples_set[1],F[1])))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                VGroup(orange_set[0],S[0]).animate.set_stroke(opacity=1),
                VGroup(orange_set[1],orange1,S[1]).animate.set_opacity(1),
                VGroup(apples_set[0],F[0]).animate.set_stroke(opacity=0.1),
                VGroup(apples_set[1],apples,F[1],fruits,ellipsis).animate.set_opacity(0.1)
            )
        )
        self.play(Indicate(VGroup(orange_set[1],S[1])))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                VGroup(apples_set[0],F[0]).animate.set_stroke(opacity=1),
                VGroup(apples_set[1],apples,fruits,ellipsis).animate.set_opacity(1),
                F[1].animate.set_opacity(1),
                S[0].animate.set_stroke(opacity=0.1),
                S[1].animate.set_opacity(0.1)
            )
        )
        self.play(Indicate(VGroup(apples_set[1],orange_set[1],F[1])))
        self.wait(3)
        
        self.play(
            AnimationGroup(
                S[0].animate.set_stroke(opacity=1),
                S[1].animate.set_opacity(1),
                F[0].animate.set_stroke(opacity=0.1),
                VGroup(F[1],fruits,ellipsis).animate.set_opacity(0.1)
            )
        )
        self.play(Indicate(VGroup(apples_set[1],orange_set[1],S[1])))
        self.wait(5)
        
        
        ##Section 17 
        self.next_section(name="Sets as an extension of our logic",skip_animations=True)
        stickman = SVGMobject(f'{SVGImages}\\ThinkingStickman.svg').set_stroke(color=WHITE, width=3).to_corner(DL,buff=2).shift(2*RIGHT)
        thought_cloud = SVGMobject(f'{SVGImages}\\ThoughtCloud.svg').set_stroke(color=WHITE, width=3).scale(2).move_to(2*UP + 3*RIGHT)
        thought_bubbles = VGroup()
        thought_bubbles.add(Circle(radius = 0.1, color=WHITE, stroke_width=3).move_to(0.1*DOWN + 2*LEFT))
        thought_bubbles.add(Circle(radius = 0.25, color=WHITE, stroke_width=3).move_to(0.3*UP + 1.1*LEFT))
        thought_bubbles.shift(0.1*UR)
        
        sets_example = VGroup(apples,apples_set,orange1,orange_set,S,F,fruits,ellipsis)
        
        self.play(
            AnimationGroup(
                F[0].animate.set_stroke(opacity=1),
                VGroup(F[1],fruits,ellipsis).animate.set_opacity(1)
            )
        )
        self.play(
            AnimationGroup(
                sets_example.animate.scale(0.35).move_to(thought_cloud).shift(0.2*DL + 0.1*DOWN),
                FadeIn(stickman,thought_bubbles,thought_cloud)
            )
        )
        self.wait(5)
        
        self.play(sets_example.animate.scale(1/5))
        self.wait(2)
        self.play(sets_example.animate.scale(5))
        self.wait(2)
        
        self.play(
            AnimationGroup(
                stickman.animate.move_to(5*LEFT),
                FadeOut(thought_bubbles,thought_cloud,sets_example)
            )
        )
        self.wait()

        lines_of_sight = VGroup(
            DashedLine(
                start = stickman.get_right() + 0.75*UP + 0.1*RIGHT,
                end = cardinal_numbers_image[0][0].get_top(),
                color=YELLOW,
                stroke_width=3
            ),
            DashedLine(
                start = stickman.get_right() + 0.7*UP + 0.1*RIGHT,
                end = cardinal_numbers_image[1][-1].get_bottom() + 0.1*DOWN,
                color=YELLOW,
                stroke_width=3
            )
        )

        self.play(
            LaggedStart(
                FadeIn(cardinal_numbers_image),
                AnimationGroup(*[Write(lines_of_sight[i]) for i in range(len(lines_of_sight))], run_time=1.2),
                lag_ratio=0.5
            )
        )
        self.wait(3)

        lines_of_sight_new = VGroup(
            DashedLine(
                start = stickman.get_right() + 0.75*UP + 0.1*RIGHT,
                end = 2.05*UP,
                color=YELLOW,
                stroke_width=3
            ),
            DashedLine(
                start = stickman.get_right() + 0.7*UP + 0.1*RIGHT,
                end = 2*DOWN + 0.4*LEFT,
                color=YELLOW,
                stroke_width=3
            )
        )
        
        self.play(
            LaggedStart(
                ShrinkToCenter(cardinal_numbers_image),
                AnimationGroup(
                    GrowFromCenter(set_diagram_copy),
                    ReplacementTransform(lines_of_sight,lines_of_sight_new)
                ),
                lag_ratio=0.5
            )
        )
        self.wait(3)
        
        ##Section 18
        self.next_section(name="Natural Numbers", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        
        cardinal_numbers_text = Tex(r"The Cardinal Numbers")
        counting_numbers = Tex(r'The Counting Numbers')
        
        cardinal_set = MathTex(r"\{ {{1,2,3,4,\dots\} }}", font_size=64).move_to(0.5*DOWN)
        
        self.play(Write(cardinal_numbers_text))
        self.wait(2)
        self.play(ReplacementTransform(cardinal_numbers_text, counting_numbers))
        self.wait(2)
        self.play(
            LaggedStart(
                counting_numbers.animate.move_to(UP),
                Write(cardinal_set),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        natural_numbers_label = Tex(r"The Natural Numbers").move_to(UP)
        zero_addition = MathTex(r"\{ {{ 0, }}", font_size=64)
        
        cardinal_set[1].generate_target()
        cardinal_set[1].target.shift(0.2*RIGHT)
        zero_addition.next_to(cardinal_set[1].target,LEFT,buff=0.15)
        
        self.play(
            LaggedStart(
                FadeOut(cardinal_set[0]),
                AnimationGroup(
                    MoveToTarget(cardinal_set[1]),
                    FadeIn(zero_addition,shift=RIGHT),
                ),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(ReplacementTransform(counting_numbers,natural_numbers_label))
        self.wait(3)
        
        N = MathTex(r"\to {{ \mathbb{N} }}").next_to(natural_numbers_label,RIGHT)
        
        cardinal_set = VGroup(zero_addition[1],cardinal_set[1])
        
        self.play(Write(N))
        self.play(Indicate(N[1]))
        self.wait(3)
        
        zero_box = SurroundingRectangle(zero_addition[1][0],color=PURE_RED,buff=0.1,corner_radius=0.01)
        
        self.play(Write(zero_box))
        self.wait(4)
        self.play(FadeOut(zero_box))
        self.wait(2)
        
        ##Section 19
        self.next_section(name="Integer Numbers", skip_animations=True)
        natural_numbers = MathTex(r"\mathbb{N} = \{0,1,2,3,4,\dots\}", font_size=36, fill_opacity=0.5).to_corner(UL)
        
        integer_label = Tex(r"Integer Numbers").move_to(UP)
        cardinal_set.generate_target()
        cardinal_set.target.shift(2*RIGHT)
        negatives = MathTex(r"\{ {{\dots,-2,-1,}}", font_size=64).next_to(cardinal_set.target,LEFT,buff=0.15)
        
        self.play(TransformFromCopy(VGroup(zero_addition[0],cardinal_set,N[1]), natural_numbers))
        self.wait()
        self.play(
            AnimationGroup(
                LaggedStart(
                    FadeOut(zero_addition[0]),
                    AnimationGroup(
                        MoveToTarget(cardinal_set),
                        FadeIn(negatives, shift=RIGHT)
                    ),
                    lag_ratio=0.5
                ),
                ReplacementTransform(VGroup(natural_numbers_label,N),integer_label),
                lag_ratio=0.5
            )
        )
        self.wait(4)
        
        Z = MathTex(r"\to {{ \mathbb{Z} }}").next_to(integer_label)
        
        self.play(Write(Z))
        self.play(Indicate(Z[1]))
        self.wait(5)
        
        integers = MathTex(r"{{\mathbb{Z}}} =\{\dots,-2,-1,0,1,2,\dots\}", font_size=36, fill_opacity=0.5).next_to(natural_numbers,DOWN, aligned_edge=LEFT)
        
        integer_set = VGroup()
        integer_set.add(Ellipse(6,6,color=WHITE))
        integer_set.add(MathTex(r"\mathbb{Z}", font_size=56).move_to(integer_set.get_corner(DR) + 1.2*UL))
        
        natural_numbers_set = VGroup()
        natural_numbers_set.add(Ellipse(3,3,color=WHITE))
        natural_numbers_set.add(MathTex(r"\mathbb{N}", font_size=56).move_to(natural_numbers_set.get_corner(DR) + 0.7*UL))
        
        self.play(FadeOut(*self.mobjects))
        self.play(Write(integer_set))
        self.wait(2)
        self.play(Write(natural_numbers_set))
        self.wait(2)
        
        ##Section 19
        self.next_section(name="Rational Numbers", skip_animations=True)
        rational_numbers_label = Tex(r"Rational Numbers").move_to(UP)
        rational_numbers = MathTex(r"\bigg\{ \dots,0,\frac{1}{1},\frac{1}{2},\frac{2}{1},\frac{1}{3},\dots \bigg\}").next_to(rational_numbers_label, DOWN, buff=1)
        
        self.play(
            LaggedStart(
                Unwrite(VGroup(natural_numbers_set, integer_set[0])),
                LaggedStart(
                    AnimationGroup(
                        ReplacementTransform(integer_set[1], integers[0]),
                        Write(natural_numbers)
                    ),
                    AnimationGroup(
                        Write(integers[1]),
                        Write(rational_numbers_label),
                        lag_ratio=0.5
                    ),
                    lag_ratio=0.5
                ),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(Write(rational_numbers))
        self.wait(5)
        
        Q = MathTex(r"\to {{\mathbb{Q}}").next_to(rational_numbers_label)
        
        self.play(Write(Q))
        self.play(Indicate(Q[1]))
        self.wait(5)
        
        rational_set = VGroup()
        rational_set.add(Ellipse(7,7,color=WHITE))
        rational_set.add(MathTex(r"\mathbb{Q}", font_size=56*5/6).move_to(rational_set.get_corner(DR) + 1.3*UL))
        
        integer_set = VGroup()
        integer_set.add(Ellipse(6,6,color=WHITE))
        integer_set.add(MathTex(r"\mathbb{Z}", font_size=56).move_to(integer_set.get_corner(DR) + 1.2*UL))
        
        natural_numbers_set = VGroup()
        natural_numbers_set.add(Ellipse(3,3,color=WHITE))
        natural_numbers_set.add(MathTex(r"\mathbb{N}", font_size=56).move_to(natural_numbers_set.get_corner(DR) + 0.7*UL))
        
        self.play(FadeOut(natural_numbers, integers, rational_numbers_label, Q, rational_numbers))
        self.wait()
        self.play(Write(VGroup(integer_set, natural_numbers_set)))
        self.wait(2)
        self.play(
            LaggedStart(
                VGroup(integer_set, natural_numbers_set).animate.scale(5/6),
                Write(rational_set),
                lag_ratio=0.5
            )
        )
        self.wait(5)
        
        
        ##Section 20
        self.next_section(name="Irrational Numbers", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        irrational_number = MathTex(r"{{N}} \neq \frac{a}{b}", font_size=56)
        irrational_text = Tex(r"$N$ has infinite solutions").next_to(irrational_number, DOWN, buff=1)
        
        self.play(Write(irrational_number))
        self.wait()
        self.play(Write(irrational_text, run_time=1))
        self.wait(5)
        
        pi = MathTex(r"\pi", font_size=56).move_to(irrational_number[0]).align_to(irrational_number[0], DOWN, RIGHT)
        
        self.play(
            LaggedStart(
                FadeOut(irrational_text),
                ReplacementTransform(irrational_number[0], pi),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        circle = Circle(2).shift(2*LEFT)
        circle_group = VGroup()
        circle_group.add(circle)
        circle_center = Dot(circle.get_center())
        circle_group.add(circle_center)
        diameter = Line(circle.get_left(),circle.get_right())
        diameter_label = MathTex(r"d").next_to(circle_center, UR, buff=0.1)
        circle_group.add(diameter, diameter_label)
        
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(irrational_number[1]),
                    pi.animate.next_to(circle,RIGHT, buff=1.5)
                ),
                Write(circle_group),
                lag_ratio=0.5
            )
        )
        self.wait(2)
        
        pi_RHS = MathTex(r"= {{\frac{circumference}{diameter}}}", font_size=56).next_to(pi, RIGHT, buff=0.1).shift(0.05*UP)
        circumference_copy = circle.copy().set_color(YELLOW)
        diameter_copy = diameter.copy().set_color(YELLOW)
        
        
        self.play(
            AnimationGroup(
                Write(pi_RHS[0]),
                ReplacementTransform(VGroup(circumference_copy.copy(),diameter_copy.copy()), pi_RHS[1]),
                circle.animate.set_stroke(opacity=0.5),
                VGroup(circle_center, diameter, diameter_label).animate.set_opacity(0.5)
            )
        )
        self.wait(2)
        
        not_rational = Tex(r"Circumference $\cap$ diameter $\notin \mathbb{Z}$ \\ $\therefore \pi \notin \mathbb{Q}$", font_size=36).next_to(VGroup(pi,pi_RHS), DOWN, buff=1)
        
        self.play(
            AnimationGroup(
                Write(not_rational, run_time=1),
                VGroup(pi,pi_RHS).animate.set_opacity(0.5)
            )
        )
        self.wait(3)
        self.play(
            AnimationGroup(
                circle.animate.set_stroke(opacity=1),
                VGroup(circle_center, diameter, diameter_label, pi, pi_RHS).animate.set_opacity(1)
            )
        )
        self.wait(2)
        
        radius = Line(circle[0].get_center(), circle.point_at_angle(PI/4), color=WHITE)
        radius_label = MathTex(r"r").next_to(radius.point_from_proportion(0.4) + 0.3*UL)
        tau = MathTex(r"\tau", font_size=56).move_to(pi)
        tau_RHS = MathTex(r"= {{\frac{circumference}{radius}}}", font_size=56).next_to(tau, RIGHT, buff=0.1).shift(0.05*UP)
        tau_eqn = MathTex(r"\frac{2\pi r}{r}", font_size=56).next_to(tau_RHS[0], RIGHT, buff=0.1)
        pi2 = MathTex(r"2\pi", font_size=56).next_to(tau_RHS[0], RIGHT, buff=0.1).align_to(tau, DOWN, RIGHT)
        
        self.play(
            AnimationGroup(
                FadeOut(pi_RHS, not_rational),
                ReplacementTransform(VGroup(diameter, diameter_label), VGroup(radius, radius_label)),
                ReplacementTransform(pi, tau)
            )
        )
        self.wait(2)
        
        radius_copy = radius.copy().set_color(YELLOW)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(VGroup(circumference_copy.copy(), radius_copy.copy()), tau_RHS),
                circle.animate.set_stroke(opacity=0.5),
                VGroup(circle_center, radius, radius_label).animate.set_opacity(0.5)
            )
        )
        self.wait(2)
        self.play(ReplacementTransform(tau_RHS[1], tau_eqn))
        self.wait(2)
        self.play(ReplacementTransform(tau_eqn, pi2))
        self.wait(3)
        self.play(
            AnimationGroup(
                circle.animate.set_stroke(opacity=1),
                VGroup(circle_center, radius, radius_label).animate.set_opacity(1)
            )
        )
        self.wait(2)
        
        Euler = ImageMobject(f'{Images}\\Leonhard_Euler.jpg').scale(0.5). to_corner(DR)
        
        self.play(FadeIn(Euler, shift=LEFT))
        self.wait(3)
        
        radius1 = Line(circle.get_center(), circle.point_at_angle(0), stroke_width=2)
        label1 = MathTex(r"0").next_to(radius1, RIGHT)
        radius2 = Line(circle.get_center(), circle.point_at_angle(TAU/4), stroke_width=2)
        label2 = MathTex(r"\frac{\tau}{4}").next_to(radius2, UP, buff=0.3)
        label2_pi = MathTex(r"\frac{\pi}{2}").next_to(radius2, UP, buff=0.3)
        radius3 = Line(circle.get_center(), circle.point_at_angle(2*TAU/4), stroke_width=2)
        label3 = MathTex(r"\frac{\tau}{2}").next_to(radius3, LEFT, buff=0.5)
        label3_pi = MathTex(r"\pi").next_to(radius3, LEFT, buff=0.5)
        radius4 = Line(circle.get_center(), circle.point_at_angle(3*TAU/4), stroke_width=2)
        label4 = MathTex(r"\frac{3\tau}{4}").next_to(radius4, DOWN, buff=0.3)
        label4_pi = MathTex(r"\frac{3\pi}{2}").next_to(radius4, DOWN, buff=0.3)
        
        radii = VGroup(
            radius1,
            label1,
            radius2,
            radius3,
            radius4,
        ).shift(2*RIGHT)
        
        radii_labels = VGroup(
            label2,
            label3,
            label4
        ).shift(2*RIGHT)
        
        radii_labels_pi = VGroup(
            label2_pi,
            label3_pi,
            label4_pi
        ).shift(2*RIGHT)
        
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(Euler, shift=RIGHT),
                    FadeOut(tau, tau_RHS[0], pi2, radius, radius_label)
                ),
                VGroup(circle, circle_center).animate.shift(2*RIGHT),
                lag_ratio=0.5
            )
        )
        self.play(Write(VGroup(radii, radii_labels)))
        self.wait(5)
        self.play(ReplacementTransform(radii_labels, radii_labels_pi))
        self.play(Indicate(radii_labels_pi))
        self.wait(5)
        
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        pi = MathTex(r"\pi = 3.141592653589\dots").shift(0.5*UP)
        tau = MathTex(r"\tau = 6.283185307178\dots").shift(0.5*DOWN)
        
        self.play(Write(pi))
        self.wait(2)
        self.play(Write(tau))
        self.wait(4)
        
        triangle = Polygon(ORIGIN,3*RIGHT,3*UP, color=RED)
        
        triangle_lines =  VGroup(
            Line(ORIGIN,3*RIGHT),
            Line(3*RIGHT,3*UP),
            Line(3*UP,ORIGIN)
        )
        right_angle = RightAngle(triangle_lines[-1], triangle_lines[0], length=0.4, quadrant=(-1,1))
        angles = VGroup(
            Angle(triangle_lines[1], triangle_lines[0], radius = 0.7, quadrant=(1,-1)),
            Angle(triangle_lines[2], triangle_lines[1], radius=0.7, quadrant=(1,-1))
        )
        angle_labels = VGroup(
            MathTex(r"\frac{\pi}{4}").scale(0.8).next_to(angles[0].point_from_proportion(0.5), UL, buff=0).shift(0.3*LEFT + 0.15*DOWN),
            MathTex(r"\frac{\pi}{4}").scale(0.8).next_to(angles[1].point_from_proportion(0.5),DR,buff=0).shift(0.1*DR)
        )
        side_labels = VGroup(
            MathTex(r"1").next_to(triangle_lines[-1], LEFT, buff=0.5),
            MathTex(r"1").next_to(triangle_lines[0], DOWN, buff=0.5),
            MathTex(r"\sqrt{2}").next_to(triangle_lines[1].point_from_proportion(0.5), UR)
        )
        
        sqrt2 = MathTex(r" = 1.414213562373\dots").next_to(side_labels[2])
        
        sqrt2_triangle = VGroup(
            triangle,
            right_angle,
            angles,
            angle_labels,
            side_labels,
            sqrt2
        ).scale(0.7).move_to(3.5*LEFT)
        
        self.play(
            AnimationGroup(
                VGroup(pi, tau).animate.scale(0.8).to_edge(UP).set_opacity(0.5),
                Write(sqrt2_triangle)
            )
        )
        self.wait(2)
        
        phi = MathTex(r"\varphi = \frac{1+\sqrt{5}}{2} = 1.618033988749\dots").scale(0.8).move_to(3*RIGHT)
        
        self.play(
            AnimationGroup(
                VGroup(triangle, right_angle, angles).animate.set_stroke(opacity=0.5),
                VGroup(angle_labels, side_labels, sqrt2).animate.set_opacity(0.5),
                Write(phi)
            )
        )
        self.wait(2)
        
        e = MathTex(r"e = \lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n = 2.718281828459\dots").scale(0.8).move_to(2.5*DOWN)
        
        self.play(
            AnimationGroup(
                phi.animate.set_opacity(0.5),
                Write(e)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                VGroup(pi, tau, phi, angle_labels, side_labels, sqrt2).animate.set_opacity(1),
                VGroup(triangle, right_angle, angles).animate.set_stroke(opacity=1)
            )
        )
        self.wait(5)
        
        ##Section 21
        self.next_section(name="Set diagram of the Real numbers", skip_animations=True)
        self.play(FadeOut(*self.mobjects))
        self.wait()
        
        real_set = VGroup(Ellipse(7,7, color=WHITE))
        real_set.add(MathTex(r"\mathbb{R}", font_size=40).move_to(real_set.get_corner(DR) + 1.25*UL))
        
        VGroup(natural_numbers_set, integer_set, rational_set)
        
        self.play(Write(VGroup(natural_numbers_set, integer_set, rational_set)))
        self.wait(2)
        self.play(
            LaggedStart(
                VGroup(natural_numbers_set, integer_set, rational_set).animate.scale(5/7),
                Write(real_set),
                lag_ratio=0.5
            )
        )
        self.play(Indicate(real_set[1]))
        self.wait(5)
        
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
        
        
class Test(Scene):
    def construct(self):
        self.add(NumberPlane())
        