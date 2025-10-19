import matplotlib.pyplot as plt
import json

def main():

    try:
        with open('Coolors Palettes.json', 'r') as file:
            content = file.read()
            data = json.loads(content)
            print(data)
        
    except FileNotFoundError:
        print("The file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")

    # Define a color palette
    colors = [
        "#0D3B66", 
        "#FAF0CA", 
        "#F4D35E", 
        "#EE964B", 
        "#F95738"
        ]

    # Create a figure
    plt.figure(figsize=(8, 2))

    # Display the colors
    for i, color in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=color)

    # Set the title and remove axes
    plt.title('My new palette')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
