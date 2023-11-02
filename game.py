import tkinter as tk
import random
CANVAS_WIDTH = 1700
CANVAS_HEIGHT = 1000

def start_rectangle(event):
    global x1, y1, rectangle
    x1 = canvas.canvasx(event.x)
    y1 = canvas.canvasy(event.y)
    rectangle = canvas.create_rectangle(x1, y1, x1, y1, outline="red")

def draw_rectangle(event):
    global rectangle
    x2 = canvas.canvasx(event.x)
    y2 = canvas.canvasy(event.y)

    canvas.coords(rectangle, x1, y1, x2, y2)

def select_numbers(event, numbers):
    x1, y1, x2, y2 = canvas.coords(rectangle)
    selected = []
    sum = 0

    for number_item in numbers:
        item_x, item_y = canvas.coords(number_item)
        if x1 < item_x < x2 and y1 < item_y < y2:
            selected.append(number_item)
            sum += int(canvas.itemcget(number_item, "text"))

    if sum == 10 or sum == 20 or sum == 30:
        for item in selected:
            canvas.delete(item)
            numbers.remove(item)

    canvas.delete(rectangle)

def draw_numbers(canvas, num_rows, num_cols):
    width = CANVAS_WIDTH / num_cols
    height = CANVAS_HEIGHT / num_rows
    numbers = []
    sum = 0
    
    for i in range(num_rows):
        for j in range(num_cols):
            x1 = j * width
            y1 = i * height
            x2 = x1 + width
            y2 = y1 + height

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            number = random.randint(1,9)
            sum += number

            if(i == num_rows - 1 and j == num_cols - 2):
                remainder = sum % 10
                if(remainder == 0):
                    num1 = random.randint(1,9)
                    num2 = 10 - num1

                    num_item = canvas.create_text(center_x, center_y, text = str(num1), font=("Comic Sans MS", 30))
                    numbers.append(num_item)

                    num_item = canvas.create_text(center_x + width, center_y, text = str(num2), font=("Comic Sans MS", 30))
                    numbers.append(num_item)
                    
                    return numbers
                else:

                    num1 = random.choice([num for num in range(1, 10) if num != 10 - remainder])

                    if(num1 + remainder < 10):
                        num2 = 10 - num1 - remainder
                    else:
                        num2 = 20 - num1 - remainder

                    num_item = canvas.create_text(center_x, center_y, text = str(num1), font=("Comic Sans MS", 30))
                    numbers.append(num_item)

                    num_item = canvas.create_text(center_x + width, center_y, text = str(num2), font=("Comic Sans MS", 30))
                    numbers.append(num_item)

                    return numbers

            num_item = canvas.create_text(center_x, center_y, text = str(number), font=("Comic Sans MS", 30))
            numbers.append(num_item)

    return numbers



if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Tenfold Tactics")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    numbers = draw_numbers(canvas, 10, 17)

    canvas.bind("<ButtonPress-1>", start_rectangle)
    canvas.bind("<B1-Motion>", draw_rectangle)
    canvas.bind("<ButtonRelease-1>", lambda event: select_numbers(event, numbers))

    root.mainloop()


