import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import matplotlib
from matplotlib.colors import ListedColormap



data = pd.DataFrame.from_csv("geography_countries.csv")


df = data.T
df = df.reset_index()


print(df)



def make_spider( row, title, color):
    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(1,3, row+1, polar=True, )


    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=11)
    ax.tick_params(axis='x', which='major', pad=20)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=11)
    plt.ylim(0, 40)

    # Ind1
    values = df.loc[row].drop('index').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=13, color=color, y=1.2)

# initialize the figure
my_dpi = 600


# Create a color palette:
my_palette = plt.cm.get_cmap("Set1", len(df.index))

my_map = matplotlib.colors.ListedColormap(["blue","red","green"])


# Loop to plot
for row in range(0, len(df.index)):
    make_spider(row=row, title= df['index'][row], color=my_map(row))

plt.subplots_adjust(wspace=0.5)
plt.show()

