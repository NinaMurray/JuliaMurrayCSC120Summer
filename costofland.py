def getDims():
    length = float(input("Enter length:  "))
    width = float(input("Enter width: "))
    return length, width

def calc_area(length, width):
    return length * width

def cost_sqft():
    length, width = getDims()
    area =calc_area(length, width)
    cost_per_sq = float(input("Enter cost per square foot: "))
    land_cost = cost_per_sq * area

    print(f"\nDimensions: {int(length)} ft. x {int(width)} ft.")
    print(f"Area: {int(area):,} sq. ft.")
    print(f"Cost Per Square: ${cost_per_sq:.2f}")
    print(f"Land Cost: ${land_cost:,.2f}")

def getplot_type():
    valid_plots = ["A", "B++", "C", "C++", "D"]

    while True:
        plot_type = input("Enter the type of plot (A, B++, C, C++, D): ").strip()
        if plot_type in valid_plots:
            return plot_type
        else:
            print("Invalid type. PLease enter a valid plot type.")

def chosen_plot(plot_type):
    if plot_type =="A":
        cst = 2.5
    elif plot_type == "B++":
        cst = 2
    elif plot_type == "C":
        cst = 1.5
    elif plot_type == "C++":
        cst = 1
    elif plot_type == "D":
        cst = 0.5
    else:
        print("Plot type not valid.")
        return None    
    return 100 * cst


cost_sqft()
plot_type = getplot_type()
plot_cost = chosen_plot(plot_type)
print(f"Plot Type Selected: {plot_type}")
print(f"Plot Cost: ${plot_cost:,.2f}")



























      