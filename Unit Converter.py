import tkinter as tk
from tkinter import ttk


# Conversion functions
def convert_length():
    try:
        value = float(length_entry.get())
        if value < 0:
            raise ValueError("Negative number entered.")
        #Meter, Kilometer, Centimeter, Millimeter, Miles, Yards, Inches
        if length_from.get() == "Meters" and length_to.get() == "Kilometers":
            result = value / 1000

        elif length_from.get() == "Meters" and length_to.get() == "Centimeters":
            result = value * 100

        elif length_from.get() == "Meters" and length_to.get() == "Millimeters":
            result = value * 1000

        elif length_from.get() == "Meters" and length_to.get() == "Miles":
            result= value/1609

        elif length_from.get() == "Meters" and length_to.get() == "Yards":
            result = value * 1.09361

        elif length_from.get() == "Kilometers" and length_to.get() == "Meters":
            result=value * 1000

        elif length_from.get() == "Kilometers" and length_to.get() == "Centimeters":
            result=value * 100000

        elif length_from.get() == "Kilometers" and length_to.get() == "Millimeters":
            result=value * 1000000

        elif length_from.get() == "Kilometers" and length_to.get() == "Miles":
            result=value * 0.621371

        elif length_from.get() == "Kilometers" and length_to.get() == "Yards":
            result=value * 1093.61

        elif length_from.get() == "Kilometers" and length_to.get() == "Inches":
            result=value * 39370.1

        elif length_from.get() == "Centimeters" and length_to.get() == "Meters":
            result = value * 0.01
        elif length_from.get() == "Centimeters" and length_to.get() == "Kilometers":
            result = value / 100000
        elif length_from.get() == "Centimeters" and length_to.get() == "Millimeters":
            result = value * 10
        elif length_from.get() == "Centimeters" and length_to.get() == "Miles":
            result = value / 160900
        elif length_from.get() == "Centimeters" and length_to.get() == "Yards":
            result = value / 91.44
        elif length_from.get() == "Centimeters" and length_to.get() == "Inches":
            result = value / 2.54

            #Millimeters
        elif length_from.get() == "Millimeters" and length_to.get() == "Meters":
            result = value * 0.001
        elif length_from.get() == "Millimeters" and length_to.get() == "Kilometers":
            result = value / 1000000
        elif length_from.get() == "Millimeters" and length_to.get() == "Centimeters":
            result = value * 0.1

        elif length_from.get() == "Millimeters" and length_to.get() == "Miles":
            result = value / 1609000
        elif length_from.get() == "Millimeters" and length_to.get() == "Yards":
            result = value / 914.4
        elif length_from.get() == "Millimeters" and length_to.get() == "Inches":
            result = value / 25.4

            #Miles
        elif length_from.get() == "Miles" and length_to.get() == "Meters":
            result = value * 1609.34
        elif length_from.get() == "Miles" and length_to.get() == "Kilometers":
            result = value * 1.60934
        elif length_from.get() == "Miles" and length_to.get() == "Centimeters":
            result = value * 160934
        elif length_from.get() == "Miles" and length_to.get() == "Millimeters":
            result = value * 1609000
        elif length_from.get() == "Miles" and length_to.get() == "Yards":
            result = value * 1760
        elif length_from.get() == "Miles" and length_to.get() == "Inches":
            result = value * 63360

            #Yards
        elif length_from.get() == "Yards" and length_to.get() == "Meters":
            result = value * 0.9144
        elif length_from.get() == "Yards" and length_to.get() == "Kilometers":
            result = value * 0.0009144
        elif length_from.get() == "Yards" and length_to.get() == "Centimeters":
            result = value * 91.44
        elif length_from.get() == "Yards" and length_to.get() == "Millimeters":
            result = value * 914.4
        elif length_from.get() == "Yards" and length_to.get() == "Miles":
            result = value / 1760
        elif length_from.get() == "Yards" and length_to.get() == "Inches":
            result = value * 36

            #Inches
        elif length_from.get() == "Inches" and length_to.get() == "Meters":
            result = value * 0.0254
        elif length_from.get() == "Inches" and length_to.get() == "Kilometers":
            result = value / 39370
        elif length_from.get() == "Inches" and length_to.get() == "Centimeters":
            result = value * 2.54
        elif length_from.get() == "Inches" and length_to.get() == "Millimeters":
            result = value * 25.4
        elif length_from.get() == "Inches" and length_to.get() == "Miles":
            result = value / 63360
        elif length_from.get() == "Inches" and length_to.get() == "Yards":
            result = value /36

        else:
            result = value  # same unit
        length_result.config(text=f"Result: {result}")
    except ValueError:
        length_result.config(text="What are you even converting... Positive number only.")


def convert_volume():
    try:
        value = float(volume_entry.get())
        if value < 0:
            raise ValueError("Negative number entered.")
        if volume_from.get() == 'Milliliters' and volume_to.get() == 'Liters':
            result = value / 1000

        elif volume_from.get() == 'Milliliters' and volume_to.get() == 'Fluid Ounces':
            result = value * 0.033814

        elif volume_from.get() == 'Milliliters' and volume_to.get() == 'Pint':
            result = value * 0.00211338

        elif volume_from.get() == 'Milliliters' and volume_to.get() == 'Quart':
            result = value * 0.00105669

        elif volume_from.get() == 'Milliliters' and volume_to.get() == 'Gallon':
            result = value * 0.000264172

        elif volume_from.get() == 'Liters' and volume_to.get() == 'Milliliters':
            result = value * 1000

        elif volume_from.get() == 'Liters' and volume_to.get() == 'Fluid Ounces':
            result = value * 33.814

        elif volume_from.get()== 'Liters' and volume_to.get() == 'Pint':
            result = value * 2.11338

        elif volume_from.get() == 'Liters' and volume_to.get() == 'Quart':
            result = value * 1.05669

        elif volume_from.get() == 'Liters' and volume_to.get() == 'Gallon':
            result = value*0.2645172

        elif volume_from.get() == 'Fluid Ounces' and volume_to.get() == 'Liters':
            result = value * 0.0295735

        elif volume_from.get() == 'Fluid Ounces' and volume_to.get() == 'Milliliters':
            result = value * 29.5735

        elif volume_from.get() == 'Fluid Ounces' and volume_to.get() == 'Pint':
            result = value * 0.0625

        elif volume_from.get() == 'Fluid Ounces' and volume_to.get() == 'Quart':
            result = value * 0.03125

        elif volume_from.get() == 'Fluid Ounces' and volume_to.get() == 'Gallon':
            result = value * 0.0078125

        elif volume_from.get() == 'Pint' and volume_to.get() == 'Liters':
            result = value * 0.473176

        elif volume_from.get() == 'Pint' and volume_to.get() == 'Milliliters':
            result = value * 473.176

        elif volume_from.get() == 'Pint' and volume_to.get() == 'Fluid Ounces':
            result = value * 16

        elif volume_from.get() == 'Pint' and volume_to.get() == 'Quart':
            result = value * 0.5

        elif volume_from.get() == 'Pint' and volume_to.get() == 'Gallon':
            result = value * 0.125

        elif volume_from.get() == 'Quart' and volume_to.get() == 'Liters':
            result = value * 0.946353

        elif volume_from.get() == 'Quart' and volume_to.get() == 'Milliliters':
            result = value * 946.353

        elif volume_from.get() == 'Quart' and volume_to.get() == 'Pint':
            result = value * 2

        elif volume_from.get() == 'Quart' and volume_to.get() == 'Fluid Ounces':
            result = value * 32

        elif volume_from.get() == 'Quart' and volume_to.get() == 'Gallon':
            result = value * 0.25

            # gallons
        elif volume_from.get() == 'Gallon' and volume_to.get() == 'Liters':
            result = value * 3.78541

        elif volume_from.get() == 'Gallon' and volume_to.get() == 'Milliliters':
            result = value * 3785.41

        elif volume_from.get() == 'Gallon' and volume_to.get() == 'Pint':
            result = value * 8

        elif volume_from.get() == 'Gallon' and volume_to.get() == 'Quart':
            result = value * 4

        elif volume_from.get() == 'Gallon' and volume_to.get() == 'Fluid Ounces':
            result = value * 128

        else:
            result = value  # same unit
        volume_result.config(text=f"Result: {result}")
    except ValueError:
        volume_result.config(text="you know you have to positive numbers only.")


def convert_temperature():
    try:
        value = float(temp_entry.get())
        if value < 0:
            raise ValueError("Negative number entered.")
        if temp_from.get() == "Celsius" and temp_to.get() == "Fahrenheit":
            result = (value * 9 / 5) + 32
        elif temp_from.get() == "Fahrenheit" and temp_to.get() == "Celsius":
            result = (value - 32) * 5 / 9
        elif temp_from.get() == "Celsius" and temp_to.get() == "Kelvin":
            result = value + 273.15
        elif temp_from.get() == "Kelvin" and temp_to.get() == "Celsius":
            result = value - 273.15
        elif temp_from.get() == "Kelvin" and temp_to.get() == "Fahrenheit":
            result = (value-273.15) * 1.8 + 32
        elif temp_from.get() == "Fahrenheit" and temp_to.get() == "Kelvin":
            result = (value-32) * (5/9) + 273.15
        else:
            result = value  # same unit
        temp_result.config(text=f"Result: {result}")
    except ValueError:
        temp_result.config(text="Positive number only!!!! >:( .")


def convert_currency():
    try:
        # Convert input to float and handle potential errors
        value = float(currency_entry.get())

        # Check for non-numeric input or negative values
        if value < 0:
            currency_result.config(text="Cmon :/")
            return

            # Define conversion rates (one-way conversion rates)
        conversion_rates = {
            ("USD", "USD"): 1,
            ("Euros", "Euros"): 1,
            ("Indian Rupee", "Indian Rupee"): 1,
            ("Mexican Pesos", "Mexican Pesos"): 1,
            ("Yen", "Yen"): 1,
            ("USD", "Euros"): 0.95,
            ("USD", "Indian Rupee"): 84.74,
            ("USD", "Mexican Pesos"): 20.40,
            ("USD", "Yen"): 149.58,
            ("Euros", "Indian Rupee"): 88.76,
            ("Euros", "Mexican Pesos"): 21.40,
            ("Euros", "USD"): 1 / 0.95,
            ("Euros", "Yen"): 156.90,
            ("Indian Rupee", "Euros"): 1 / 88.76,
            ("Indian Rupee", "Mexican Peso"): 1 / 0.24,
            ("Indian Rupee", "USD"): 1 / 0.012,
            ("Indian Rupee", "Yen"): 1.76,
            ("Mexican Pesos", "Euros"): 1 / 21.40,
            ("Mexican Pesos", "USD"): 1 / 0.049,
            ("Mexican Pesos", "Indian Rupee"): 0.24,
            ("Mexican Pesos", "Yen"): 7.33,
            ("Yen", "Mexican Pesos"): 0.136,
            ("Yen", "USD"): 1 / 0.0067,
            ("Yen", "Euro"): 1 / 0.0064,
            ("Yen", "Indian Rupee"): 1 / 0.57
        }

        # Get the selected currencies
        from_currency = currency_from.get()
        to_currency = currency_to.get()
        # Currency symbols
        currency_symbols = {
            "USD": "$",
            "Euros": "€",
            "Indian Rupee": "₹",
            "Mexican Pesos": "₱",
            "Yen": "¥"
        }
        # Check if the selected currencies are in the conversion dictionary
        if (from_currency, to_currency) in conversion_rates:
            # Perform the conversion
            result = value * conversion_rates[(from_currency, to_currency)]
        elif (to_currency, from_currency) in conversion_rates:
            # Perform the conversion in reverse direction
            result = value * conversion_rates[(to_currency, from_currency)]
        else:
            # Handle case where no valid conversion is found
            currency_result.config(text="Invalid currency pair selected.")
            return

            # Display result with currency symbols
        from_symbol = currency_symbols.get(from_currency, "")
        to_symbol = currency_symbols.get(to_currency, "")
        currency_result.config(text=f"Result: {from_symbol}{value} = {to_symbol}{result:.2f}")

    except ValueError:
        # Handle invalid input (non-numeric input)
        currency_result.config(text="Please enter a valid number bruh :/.")

        # Check if the selected currencies are in the conversion dictionary
        if (from_currency, to_currency) in conversion_rates:
            # Perform the conversion
            result = value * conversion_rates[(from_currency, to_currency)]
        elif (to_currency, from_currency) in conversion_rates:
            # Perform the conversion in reverse direction
            result = value * conversion_rates[(to_currency, from_currency)]
        else:
            # Handle case where no valid conversion is found
            currency_result.config(text="Invalid currency pair selected.")
            return

            # Display result, formatted to two decimal places
        currency_result.config(text=f"Result: {result:.2f}")

    except ValueError:
        # Handle invalid input (non-numeric input)
        currency_result.config(text="Please enter a valid number.")


common_font = ("Arial", 14)

# Create main window
root = tk.Tk()
root.title("Unit Converter")

# Create Notebook (Tabs)
tab_control = ttk.Notebook(root)

# Length Tab
length_tab = ttk.Frame(tab_control)
tab_control.add(length_tab, text="Length")

length_label = tk.Label(length_tab, text="Enter Length:", font=common_font, background="light blue")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(length_tab)
length_entry.grid(row=0, column=1)

length_from_label = tk.Label(length_tab, text="From:")
length_from_label.grid(row=1, column=0)

length_from_label = tk.Label(length_tab, text="To:")
length_from_label.grid(row=2, column=0)

length_from = ttk.Combobox(length_tab, values=["Meters", "Kilometers", "Miles", "Centimeters", 'Millimeters', 'Yards', 'Inches'])
length_from.grid(row=1, column=1)
length_from.set("Meters")

length_to = ttk.Combobox(length_tab, values=["Meters", "Kilometers", "Miles","Centimeters", 'Millimeters', 'Yards', 'Inches'])
length_to.grid(row=2, column=1)
length_to.set("Meters")

length_convert_button = tk.Button(length_tab, text="Convert", command=convert_length)
length_convert_button.grid(row=3, column=0)

length_result = tk.Label(length_tab, text="Result: ")
length_result.grid(row=4, column=0)

# Volume Tab
volume_tab = ttk.Frame(tab_control)
tab_control.add(volume_tab, text="Volume")

volume_label = tk.Label(volume_tab, text="Enter Volume:", font=common_font, background="light blue")
volume_label.grid(row=0, column=0)

volume_entry = tk.Entry(volume_tab)
volume_entry.grid(row=0, column=1)

volume_from_label = tk.Label(volume_tab, text="From:")
volume_from_label.grid(row=1, column=0)

volume_from_label = tk.Label(volume_tab, text="To:")
volume_from_label.grid(row=2, column=0)

volume_from = ttk.Combobox(volume_tab, values=["Liters", "Milliliters", "Gallon","Fluid Ounces", 'Pint', "Quart"])
volume_from.grid(row=1, column=1)
volume_from.set("Liters")

volume_to = ttk.Combobox(volume_tab, values=["Liters", "Milliliters", "Gallon","Fluid Ounces", 'Pint', "Quart"])
volume_to.grid(row=2, column=1)
volume_to.set("Liters")

volume_convert_button = tk.Button(volume_tab, text="Convert", command=convert_volume)
volume_convert_button.grid(row=3, column=0)

volume_result = tk.Label(volume_tab, text="Result: ")
volume_result.grid(row=4, column=0)

# Temperature Tab
temp_tab = ttk.Frame(tab_control)
tab_control.add(temp_tab, text="Temperature")

temp_label = tk.Label(temp_tab, text="Enter Temperature:", font=common_font, background="light blue")
temp_label.grid(row=0, column=0)

temp_entry = tk.Entry(temp_tab)
temp_entry.grid(row=0, column=1)

temp_from_label = tk.Label(temp_tab, text="From:")
temp_from_label.grid(row=1, column=0)

temp_from_label = tk.Label(temp_tab, text="To:")
temp_from_label.grid(row=2, column=0)

temp_from = ttk.Combobox(temp_tab, values=["Celsius", "Fahrenheit", "Kelvin"])
temp_from.grid(row=1, column=1)
temp_from.set("Celsius")

temp_to = ttk.Combobox(temp_tab, values=["Celsius", "Fahrenheit", "Kelvin"])
temp_to.grid(row=2, column=1, columnspan=2)
temp_to.set("Celsius")

temp_convert_button = tk.Button(temp_tab, text="Convert", command=convert_temperature)
temp_convert_button.grid(row=3, column=0)

temp_result = tk.Label(temp_tab, text="Result: ")
temp_result.grid(row=4, column=0)

# Currency Tab
currency_tab = ttk.Frame(tab_control)
tab_control.add(currency_tab, text="Currency")

currency_label = tk.Label(currency_tab, text="Enter Currency:", font=common_font, background="light blue")
currency_label.grid(row=0, column=0)

currency_entry = tk.Entry(currency_tab)
currency_entry.grid(row=0, column=1)

currency_from_label = tk.Label(currency_tab, text="From:")
currency_from_label.grid(row=1, column=0)

currency_from_label = tk.Label(currency_tab, text="To:")
currency_from_label.grid(row=2, column=0)

currency_from = ttk.Combobox(currency_tab, values=["Euros", "Mexican Pesos", "Indian Rupee", "USD", "Yen"])
currency_from.grid(row=1, column=1)
currency_from.set("Euros")

currency_to = ttk.Combobox(currency_tab, values=["Euros", "Mexican Pesos", "Indian Rupee", "USD", "Yen"])
currency_to.grid(row=2, column=1)
currency_to.set("Yen")

currency_convert_button = tk.Button(currency_tab, text="Convert", command=convert_currency)
currency_convert_button.grid(row=3, column=0)

currency_result = tk.Label(currency_tab, text="Result: ")
currency_result.grid(row=4, column=0)

# Pack and start the main loop
tab_control.pack(expand=1, fill="both")
root.mainloop()


