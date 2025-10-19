import matplotlib.pyplot as plt
import json

def main():

    try:
        with open('Coolors Palettes.json', 'r') as file:
            content = file.read()
            data = json.loads(content)
            colors = []
            for color_dyad in data['palettes'][0]['palette_colors']:
                colors.append('#' + color_dyad[1])

            print(colors)
        
    except FileNotFoundError:
        print("The file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")

    # Create a figure
    plt.figure(figsize=(8, 2))

    # Display the colors
    for i, color in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=color)

    # Set the title and remove axes
    plt.title(data['palettes'][0]['palette_name'])
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
