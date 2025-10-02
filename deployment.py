import tkinter as tk   # Imports the tkinter library for GUI, including themed widgets (ttk) and message boxes.
from tkinter import ttk, messagebox
import pandas as pd #Imports pandas for data handling.
import joblib   # Imports joblib to load the saved machine learning model.
from PIL import Image, ImageTk  #Imports Pillow modules to handle and display images in Tkinter.

# Load the trained model (Best model) pipeline
model = joblib.load(r'best_model.pkl')

root = tk.Tk()  # Creates the main Tkinter window
root.title("Coffee Health Prediction") #Sets window title.
root.geometry("450x700") #Sets fixed window size 450x700 pixels.
root.resizable(False, False) #Disables window resizing.

# Load and set background image (coffee beans)
try:
# open and resize background image to fill window space.
    bg_image = Image.open(r"coffee4.png")  
    bg_image = bg_image.resize((450, 700), Image.LANCZOS) 
    bg_photo = ImageTk.PhotoImage(bg_image) # convert to Tkinter image format
    bg_label = tk.Label(root, image=bg_photo) # create labels widget with image to fill window
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo  # make a reference to image and keep it 
# print error if image loading fails
except Exception as e:
    print("Background image not loaded:", e)
# make Tkinter variables according to features in used dataset
fields = {
    'Age': tk.IntVar(),
    'Gender': tk.StringVar(),
    'Country': tk.StringVar(),
    'Coffee_Intake': tk.IntVar(),
    'Caffeine_mg': tk.IntVar(),
    'Sleep_Hours': tk.IntVar(),
    'Sleep_Quality': tk.StringVar(),
    'BMI': tk.DoubleVar(),
    'Heart_Rate': tk.IntVar(),
    'Stress_Level': tk.StringVar(),
    'Physical_Activity_Hours': tk.DoubleVar(),
    'Occupation': tk.StringVar(),
    'Smoking': tk.IntVar(),
    'Alcohol_Consumption': tk.IntVar()
}
# According to this type of data (Categorical) we need to list choices
gender_options = ['Male', 'Female']
country_options = ['USA', 'Brazil', 'Italy', 'Japan', 'India', 'Other']
sleep_quality_options = ['Poor', 'Fair', 'Good', 'Excellent']
stress_level_options = ['Low', 'Medium', 'High']
occupation_options = ['Office', 'Manual', 'Student', 'Retired', 'Healthcare', 'Other']

# Coffee cream/brown colors
FORM_BG = '#d8c3a5'          # Light coffee cream (frame background)
LABEL_BG = '#d8c3a5'         # Label background
ENTRY_BG = '#f6f1eb'         # Entry/combobox background
RESULT_BG = '#b08a68'        # Result box rich coffee-brown
BTN_BG = '#c97a35'           # Coffee orange-brown (button)

#Creates a frame widget as container for all input fields.

#Sets its background, border width, and relief style.

form_frame = tk.Frame(root, bg=FORM_BG, bd=2, relief=tk.RIDGE)
form_frame.place(x=55, y=30, width=340, height=410)  #Places it at position (55,30) with fixed size.

#Defines a function that creates one labeled input line in the form ,Then creates a label with specified text, styling, 
#and position Depending on widget_type, creates either a dropdown (combobox) or text entry box.
#Positions inputs right-aligned to labels,sets fonts and colors

def create_field(frame, label_text, var, y_position, widget_type='entry', options=None):
    label = tk.Label(frame, text=label_text, bg=LABEL_BG, font=('Arial', 10, 'bold'), anchor='w', fg='#613613')
    label.place(x=5, y=y_position, width=130, height=21)
    if widget_type == 'combobox':
        cb = ttk.Combobox(frame, textvariable=var, values=options, state='readonly', font=('Arial', 10))
        cb.place(x=142, y=y_position, width=180, height=21)
        cb.current(0)
        cb.configure(background=ENTRY_BG)
    else:
        entry = ttk.Entry(frame, textvariable=var, font=('Arial', 10), background=ENTRY_BG, foreground='#613613')
        entry.place(x=142, y=y_position, width=180, height=21)

# Calls the function repeatedly to add all input fields vertically, incrementing y-position by step for spacing.
y = 8
step = 27
create_field(form_frame, 'Age', fields['Age'], y); y += step
create_field(form_frame, 'Gender', fields['Gender'], y, 'combobox', gender_options); y += step
create_field(form_frame, 'Country', fields['Country'], y, 'combobox', country_options); y += step
create_field(form_frame, 'Coffee Intake (cups)', fields['Coffee_Intake'], y); y += step
create_field(form_frame, 'Caffeine (mg/day)', fields['Caffeine_mg'], y); y += step
create_field(form_frame, 'Sleep Hours', fields['Sleep_Hours'], y); y += step
create_field(form_frame, 'Sleep Quality', fields['Sleep_Quality'], y, 'combobox', sleep_quality_options); y += step
create_field(form_frame, 'BMI', fields['BMI'], y); y += step
create_field(form_frame, 'Heart Rate', fields['Heart_Rate'], y); y += step
create_field(form_frame, 'Stress Level', fields['Stress_Level'], y, 'combobox', stress_level_options); y += step
create_field(form_frame, 'Physical Activity (hours)', fields['Physical_Activity_Hours'], y); y += step
create_field(form_frame, 'Occupation', fields['Occupation'], y, 'combobox', occupation_options); y += step
create_field(form_frame, 'Smoking (0:No,1:Yes)', fields['Smoking'], y); y += step
create_field(form_frame, 'Alcohol Consumption', fields['Alcohol_Consumption'], y)

#Creates a multi-line text widget to display prediction outputs ,Styles it with matching coffee brown background and white text.
#Places it below the form.
result_box = tk.Text(root, height=5, width=60, font=('Arial', 12), bg=RESULT_BG, bd=2, relief=tk.SUNKEN, fg='#ffffff')
result_box.place(x=55, y=450, width=340, height=95)
result_box.configure(state='disabled')

#1.Defines the function triggered on clicking the Predict button.

#2.Reads current user inputs from Tkinter variables.

#3.Creates a pandas DataFrame for model input.

#4.Runs the prediction and probability methods of the model pipeline.

#5.Displays formatted prediction and confidence in the result box.

def predict():
    try:
        result_box.configure(state='normal')
        result_box.delete('1.0', tk.END)
        input_dict = {key: var.get() for key, var in fields.items()}
        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]
        result_text = f"Prediction: Class {prediction}\nConfidence: {max(proba):.2%}"
        result_box.insert(tk.END, result_text)
        result_box.configure(state='disabled')
#shows an error popup if prediction fails.
    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed:\n{str(e)}")
#Creates a "Predict" button that calls the predict() function on click.[Places the button under the result box.]
predict_button = tk.Button(root, text="Predict", command=predict, bg=BTN_BG, font=('Arial', 11, 'bold'), fg='#fff')
predict_button.place(x=175, y=560, width=100, height=32)

#Starts the Tkinter event loop; keeps the window open and responsive until closed.

root.mainloop()