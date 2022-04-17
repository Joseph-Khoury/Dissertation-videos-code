from typing import Sequence
from manim import *
from manim.utils.deprecation import deprecated

class Pyramid(VGroup):
    """Create a pyramid, either truncated or not, and return as a VGroup of VMObject."""
    def __init__(
        self,
        major_base_length: float = 1.0,
        minor_base_length: float = 0.2,
        vertical_height: float = 1.0,
        is_truncated: bool = True,
        fill_opacity: float = 0.75,
        fill_color: str = BLUE,
        stroke_width: float = 0,
        **kwargs
    ):
        self.major_base_length=major_base_length
        self.minor_base_length=minor_base_length
        self.vertical_height=vertical_height
        self.is_truncated=is_truncated
        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            **kwargs
        )
        
           
    def generate_points(self):
        v = []
        h = []
        if self.is_truncated==True:
            v.append([self.major_base_length/2, -self.major_base_length/2, 0]) #v0
            v.append([self.major_base_length/2, self.major_base_length/2, 0]) #v1
            h.append([self.minor_base_length/2, -self.minor_base_length/2, self.vertical_height]) #h0
            h.append([self.minor_base_length/2, self.minor_base_length/2, self.vertical_height]) #h1
            v.append([-self.major_base_length/2, self.major_base_length/2, 0]) #v2
            h.append([-self.minor_base_length/2, self.minor_base_length/2, self.vertical_height]) #h2
            v.append([-self.major_base_length/2, -self.major_base_length/2, 0]) #v3
            h.append([-self.minor_base_length/2, -self.minor_base_length/2, self.vertical_height]) #h3
            v.append(v[0]) #v4
            h.append(h[0]) #h4
            
            faces = []
            for x in range(4):
                faces.append(Polygon(v[x],v[x+1],h[x+1],h[x],v[x], shade_in_3d=True))
                self.add(faces[x])
                
            top_face = Polygon(*[h[x] for x in range(5)], shade_in_3d=True)
            bottom_face = Polygon(*[v[x] for x in range(5)], shade_in_3d=True)
            self.add(top_face,bottom_face)
            
            v.extend(h)
            
        else:
            v = []
            v.append([self.major_base_length/2, -self.major_base_length/2, 0]) #v0
            v.append([self.major_base_length/2, self.major_base_length/2, 0]) #v1
            v.append([-self.major_base_length/2, self.major_base_length/2, 0]) #v2
            v.append([-self.major_base_length/2, -self.major_base_length/2, 0]) #v3
            v.append([self.major_base_length/2, -self.major_base_length/2, 0]) #v4
            h = [0, 0, self.vertical_height]
            
            faces = []
            for x in range(4):
                faces.append(Polygon(v[x],v[x+1],h,v[x], shade_in_3d=True))
                self.add(faces[x])
                
            bottom_face = Polygon(*[v[x] for x in range(5)], shade_in_3d=True)
            self.add(bottom_face)
            
            v.append(h)
        
        #Instance variables
        self.vertices=v
        
    init_points = generate_points
    
    
    def get_vertices(self, radius: float = 0, **kwargs) -> VGroup:
        """Return the vertices at the time of object definition as a group of Dot mobjects"""
        vertices = VGroup(*[Dot3D(point, radius=radius, **kwargs) for point in self.vertices])
        return vertices
    
    
    @deprecated
    def generate_arrows(self):
        raise Exception("This instance method is currently dysfunctional")
        vertices = self.vertices
        base_arrow = Line(vertices[-2], vertices[-1]).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1)
        point1 = Line(vertices[0], vertices[1]).point_from_proportion(0.4)
        if self.is_truncated == True:
            point2 = Line(vertices[5], vertices[6]).point_from_proportion(0.5)
            top_arrow = Line(vertices[-2], vertices[-1]).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1)
            height_arrow = Line(point1, point2).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1)
            arrows = VGroup(base_arrow, height_arrow, top_arrow) 
        else:
            point2 = vertices[-1]
            height_arrow = Line(point1, point2).add_tip(at_start=True, tip_length=0.1).add_tip(tip_length=0.1)
            arrows = VGroup(base_arrow, height_arrow)
        
        return arrows
    
    @deprecated
    def generate_labels(
        self,
        labels: list[str],
        **kwargs
    ):
        raise Exception("This instance method is currently dysfunctional")
        arrows = self.generate_arrows()
        if len(labels) <= 3:
            base_label = MathTex(labels[0], **kwargs)
            height_label = MathTex(labels[1], **kwargs)
            if self.is_truncated == True:
                top_label = MathTex(labels[2], **kwargs)
                label_group = VGroup(base_label, height_label, top_label)
                
                base_label_location = arrows[0].point_from_proportion(0.5) + 0.1*IN
                height_label_location = arrows[1].point_from_proportion(0.5) + 0.1*RIGHT
                top_label_location = arrows[2].point_from_proportion(0.5) + 0.1*IN
                
                label_group = VGroup(
                    arrows,
                    base_label.move_to(base_label_location),
                    height_label.move_to(height_label_location),
                    top_label.move_to(top_label_location)
                )
            else:
                label_group = VGroup(base_label, height_label)
                
                base_label_location = arrows[0].point_from_proportion(0.5) + 0.1*IN
                height_label_location = arrows[1].point_from_proportion(0.5) + 0.1*RIGHT
                
                label_group = VGroup(
                    arrows,
                    base_label.move_to(base_label_location),
                    height_label.move_to(height_label_location)
                )
                
        else:
            raise ValueError("You have entered too many labels!")
        
        return label_group
        
    
     

class RightTriangle(Polygon):
    """Create a right angled triangle and return the object and its parameters."""
    def __init__(
            self,
            base_length: float=3,
            height_length: float=4,
            **kwargs
            ):
        

        vertices = [
            ORIGIN,
            base_length*RIGHT,
            height_length*UP + base_length*RIGHT
        ]
        
        triangle = super().__init__(*vertices, **kwargs)
        
        #Instance variables
        self.base_length=base_length
        self.height_length=height_length
        self.vertices=vertices
        
        return triangle

    
    
    def get_triangle_vertices(self):        
        return self.vertices
    
    
    def get_lines(self):
        """Create right triangle outline for reference; not meant to be plotted."""
        lines = {                                                     
            "base_line": Line(self.vertices[0], self.vertices[1]),    
            "height_line": Line(self.vertices[1], self.vertices[2]),  
            "hypotneuse": Line(self.vertices[0], self.vertices[2])    
    }                                                                           
        return lines
    
    
    def get_angle(self, angle_position: str = {"bottom", "top", "both"}) -> list[float]:
        """return specified angle in radians."""
        if angle_position == "bottom":
            angle = np.arctan(self.height_length/self.base_length)
        elif angle_position == "top":
            angle = np.arctan(self.base_length/self.height_length)
        elif angle_position == "both":
            angle = [
                np.arctan(self.height_length/self.base_length),
                np.arctan(self.base_length/self.height_length)
            ]
            
        return angle
        
    
    def generate_labels(
        self,
        side_labels: dict={
            'base_label': "",
            'height_label': "",
            'hypotneuse_label': ""
        },
        angle_position: str={"bottom", "top", "both"},
        add_angle_label: bool=True,
        angle_label_font_size: int=DEFAULT_FONT_SIZE,
        accurate_angle_label: bool=False,
        font_size: int=DEFAULT_FONT_SIZE,
        stroke_width: float=DEFAULT_STROKE_WIDTH,
        stroke_color: str=WHITE,
        ):
        
        var1 = np.sign(self.base_length)
        var2 = np.sign(self.height_length)
        
        if var1 == var2:
            var3 = False
        else:
            var3 = True
        
        lines = self.get_lines()
        
        side_label_group = VGroup(
            MathTex(side_labels['base_label'], font_size=font_size).next_to(lines['base_line'], np.sign(self.height_length)*DOWN, buff=0.4),
            MathTex(side_labels['height_label'], font_size=font_size).next_to(lines['height_line'], np.sign(self.base_length)*RIGHT, buff=0.4),
            MathTex(side_labels['hypotneuse_label'], font_size=font_size).next_to(lines['hypotneuse'].point_from_proportion(0.5), np.sign(self.height_length)*UP + np.sign(self.base_length)*LEFT, buff=0.4/np.sqrt(2))  
)                                                                                                                   
                                                                                                                    
        right_triangle_labels = VGroup(side_label_group)
            
        right_angle_indicator = RightAngle(
            lines['base_line'],
            lines['height_line'], 
            length = min([abs(self.base_length), abs(self.height_length)])/6,  
            stroke_width=stroke_width, 
            stroke_color=stroke_color,
            quadrant=(-1,1)
        )
        
        if angle_position == "bottom":
            angle = round(self.get_angle("bottom"), 2)
            angle_indicator = Angle(
                lines['base_line'], 
                lines['hypotneuse'], 
                radius = self.base_length/6, 
                stroke_width=stroke_width, 
                stroke_color=stroke_color,
                other_angle = var3
            )
            
            if add_angle_label == True:
                angle_label_position = Angle(
                    lines['base_line'], 
                    lines['hypotneuse'], 
                    radius = abs(self.base_length)/6 + angle_indicator.get_arc_length(),
                    other_angle = var3
                ).point_from_proportion(0.5)
                
                if accurate_angle_label == True:
                    angle_label = MathTex(str(angle), font_size=angle_label_font_size).move_to(angle_label_position)
                else:
                    angle_label = MathTex(r"\theta", font_size=angle_label_font_size).move_to(angle_label_position)
                    
                angle_indicators = VGroup(right_angle_indicator, angle_indicator, angle_label)
                right_triangle_labels += angle_indicators
            else:
                angle_indicators = VGroup(right_angle_indicator, angle_indicator)
                right_triangle_labels += angle_indicators
                
        elif angle_position == "top":
            
            angle = round(self.get_angle("top"), 2)
            angle_indicator = Angle(
                lines['hypotneuse'], 
                lines['height_line'], 
                radius = self.height_length/6,
                stroke_width=stroke_width, 
                stroke_color=stroke_color,
                quadrant = (-1,-1),
                other_angle=var3
            )
            
            if add_angle_label == True:
                angle_label_position = Angle(
                    lines['hypotneuse'], 
                    lines['height_line'], 
                    radius = abs(self.height_length)/6 + angle_indicator.get_arc_length(), 
                    quadrant=(-1,-1),
                    other_angle=var3
                ).point_from_proportion(0.5)
                
                if accurate_angle_label == True:
                    angle_label = MathTex(str(angle), font_size=angle_label_font_size).move_to(angle_label_position)
                else:
                    angle_label = MathTex(r"\varphi", font_size=angle_label_font_size).move_to(angle_label_position)
                    
                angle_indicators = VGroup(right_angle_indicator, angle_indicator, angle_label)
                right_triangle_labels += angle_indicators
            else:
                angle_indicators = VGroup(right_angle_indicator, angle_indicator)
                right_triangle_labels += angle_indicators
        
        elif angle_position == "both":
            
            angle = [
                round(self.get_angle("bottom"), 2),
                round(self.get_angle("top"), 2)
            ]
            
            angle_indicator = [
                Angle(
                    lines['base_line'], 
                    lines['hypotneuse'], 
                    radius = self.base_length/6, 
                    stroke_width=stroke_width, 
                    stroke_color=stroke_color,
                    other_angle = var3
                ),
                Angle(
                    lines['hypotneuse'], 
                    lines['height_line'], 
                    radius = self.height_length/6, 
                    stroke_width=stroke_width, 
                    stroke_color=stroke_color,
                    quadrant = (-1,-1),
                    other_angle=var3
                )
            ]
            
            if add_angle_label == True:
                angle_label_position = [
                    Angle(
                        lines['base_line'], 
                        lines['hypotneuse'], 
                        radius = abs(self.base_length)/6 + angle_indicator[0].get_arc_length(),
                        other_angle = var3
                    ).point_from_proportion(0.5),
                    Angle(
                        lines['hypotneuse'], 
                        lines['height_line'], 
                        radius = abs(self.height_length)/6 + angle_indicator[1].get_arc_length(), 
                        quadrant = (-1,-1),
                        other_angle=var3
                    ).point_from_proportion(0.5)
                ]
                
                if accurate_angle_label == True:
                    angle_label = [
                        MathTex(str(angle[0]), angle_label_font_size).move_to(angle_label_position[0]),
                        MathTex(str(angle[1]), angle_label_font_size).move_to(angle_label_position[1])
                    ]
                else:
                    angle_label = [
                        MathTex(r"\theta", font_size=angle_label_font_size).move_to(angle_label_position[0]),
                        MathTex(r"\varphi", font_size=angle_label_font_size).move_to(angle_label_position[1])
                    ]
                
                angle_indicators = VGroup(right_angle_indicator, *angle_indicator, *angle_label)
                right_triangle_labels += angle_indicators
            else:
                angle_indicators = VGroup(right_angle_indicator, *angle_indicator)
                right_triangle_labels += angle_indicators

        #Instance variables   
        self.labels=right_triangle_labels #A Vgroup containing side_label_group and angle_indicators, respectively.
        self.side_label_group=side_label_group
        self.angle_indicators=angle_indicators
        self.angle=angle
        
        return right_triangle_labels  
       
         
         
         
         