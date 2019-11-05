from pyx import *

# Iterated function system
def IFS(iterations, maps, canvas_input):
    for j in range(iterations):
        temp_canvas = canvas.canvas()

        for k in range(len(maps)):
            temp_canvas.insert(canvas_input,[maps[k]])
        canvas_input = temp_canvas

    return canvas_input

# Prints the steps constructing the fractal
def print_steps(steps, maps, canvas_input, separation):
    canvas_output = canvas.canvas()
    for j in range(steps):
        translate = trafo.translate(separation*j,0)
        canvas_output.insert(IFS(j,maps,canvas_input),[translate])
        
    return canvas_output


# Prints the steps constructing the fractal, vertically
def print_steps_vert(steps, maps, canvas_input, separation):
    canvas_output = canvas.canvas()
    for j in range(steps):
        translate = trafo.translate(0,separation*j)
        canvas_output.insert(IFS(j,maps,canvas_input),[translate])
        
    return canvas_output






        
