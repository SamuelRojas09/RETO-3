import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length: float | None = None
        self.slope: float | None = None
        self.discretized_points: list[Point] | None = None
        
    def compute_length(self) -> float:
        self.length = math.sqrt(
            (self.end.x - self.start.x)** 2 + 
            (self.end.y - self.start.y)** 2
        )
        return self.length
    
    def compute_slope(self) -> float | None:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        
        if dx == 0:
            self.slope = None
            return None
        
        slope_rad = math.atan(dy / dx)
        self.slope = math.degrees(slope_rad)
        return self.slope
    
    def compute_horizontal_cross(self) -> bool:
        return (
            (self.start.y > 0 and self.end.y < 0) or 
            (self.start.y < 0 and self.end.y > 0)
        )   
                                                                                              
    def compute_vertical_cross(self) -> bool:
        return (
            (self.start.x > 0 and self.end.x < 0) or 
            (self.start.x < 0 and self.end.x > 0)
        )
    
    def discretize_line(self, n: int) -> list[Point]:
        
        if n < 2:
            raise ValueError("n debe ser mayor o igual a 2")
        
        points: list[Point] = []
        
        for i in range(n):
            progress = i / (n - 1)
            
            x = self.start.x + progress * (self.end.x - self.start.x)
            y = self.start.y + progress * (self.end.y - self.start.y)

            points.append(Point(x, y))
            
        self.discretized_points = points
        return points            
            
                
class Rectangle:
    def __init__(self, line1: Line, line2: Line, line3: Line, line4: Line):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
    
    def compute_perimeter(self) -> float:
        return sum((
            self.line1.compute_length(),
            self.line2.compute_length(),
            self.line3.compute_length(),
            self.line4.compute_length()
        ))
    
    def compute_area(self) -> float:
        base = self.line1.compute_length()
        height = self.line2.compute_length()
        return base * height
        

if __name__ == "__main__":
    
    # Prueba de Line
    p1 = Point(0, 2)
    p2 = Point(3, -1)
    line = Line(p1, p2)

    print(f"Length: {line.compute_length()}")
    print(f"Slope (deg): {line.compute_slope()}°")
    print(f"Crosses X-axis: {line.compute_horizontal_cross()}")
    print(f"Crosses Y-axis: {line.compute_vertical_cross()}")

    # Prueba de Rectangle 
    p1 = Point(0, 0)
    p2 = Point(6, 0)
    p3 = Point(6, 2)
    p4 = Point(0, 2)

    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    rec = Rectangle(line1, line2, line3, line4)

    print(f"Perimeter: {rec.compute_perimeter()}")
    print(f"Area: {rec.compute_area()}")

    # Prueba de discretize_line
    print("Discretization of the line:")
    points = line.discretize_line(5)

    for i, point in enumerate(points, start=1):
        print(f"Point {i}: {point}")
        
