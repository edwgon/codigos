from bokeh.plotting import figure, output_file,show
if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    print(str(type(fig)))
    #print(str(help(figure)))
    valores = int(input('Cuantos valores quieres graficar'))
    x_vals = list(range(valores))
    y_vals = []
    for i in x_vals:
        val = int(input(f'Ingrese valor y para {i}'))
        y_vals.append(val)

    fig.line(x_vals,y_vals,line_width=2)
    show(fig)
