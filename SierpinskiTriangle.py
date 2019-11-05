from SelfSimilarity import *
import numpy as np

def car2pol(x,y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y,x)
    return(rho, phi)

def pol2car(rho,phi):
    x = rho*np.cos(2*np.pi*phi/360.0)
    y = rho*np.sin(2*np.pi*phi/360.0)
    return x, y



### Sierpinski Carpet
canvas_sierpinski = canvas.canvas()

width = 2
height = 0.5*np.sqrt(3)*width

R = 1.5*height
Tri = []
for j in range(3):
    x, y = pol2car(R,120*j+90)
    Tri.append((x,y))


    
base_shape = path.line(Tri[2][0],Tri[2][1],Tri[0][0],Tri[0][1])
for j in range(2):
    base_shape = base_shape << path.line(Tri[j][0],Tri[j][1],Tri[j+1][0],Tri[j+1][1])
base_shape.append(path.closepath())
    
#canvas_sierpinski.stroke(path.circle(0,0,R))
canvas_sierpinski.stroke(base_shape)


ifs_scaling = 0.5
ifs_xshift = 0.5*width
ifs_yshift = 0.5*height
scaling_matrix = ((ifs_scaling,0),(0,ifs_scaling))

maps = []
for j in range(3):
    map = trafo.trafo(matrix = scaling_matrix, vector = (0.5*Tri[j][0],0.5*Tri[j][1]))
    maps.append(map)


# Draw the steps

canvas_sierpinski.writePDFfile("bugging")


canvas_sierpinski.fill(base_shape)
sierpinski_steps = canvas.canvas()
N = 5
sierpinski_steps = print_steps(N, maps, canvas_sierpinski, 3*width)

canvas_sierpinski = IFS(N, maps, canvas_sierpinski)

canvas_sierpinski.writePDFfile("SierpinskiTriangle")
sierpinski_steps.writePDFfile("SierpinskiTriangleSteps")
    

