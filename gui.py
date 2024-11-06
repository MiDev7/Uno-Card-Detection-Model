import customtkinter as ctk
from PIL import Image
import cv2
from tkinter import filedialog
import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.utils import img_to_array, load_img
class UNOGui:
    def __init__(self):
        self.gui = ctk.CTk()
        self.gui.title("UNO Card Detector")
        self.gui.geometry("1400x900")
        self.camera_on = False
        self.cap = None
        self.model = tf.keras.models.load_model("best_model_07_11_2024_01_43_32.keras")
        self.camera_image = None
        self.img_width = 224
        self.img_height = 224
        self.class_names = ["blue_0","blue_1","blue_2","blue_3","blue_4","blue_5","blue_6","blue_7","blue_8","blue_9","blue_draw_2","blue_reverse","blue_skip","green_0","green_1","green_2","green_3","green_4","green_5","green_6","green_7","green_8","green_9","green_draw_2","green_reverse","green_skip","red_0","red_1","red_2","red_3","red_4","red_5","red_6","red_7","red_8","red_9","red_draw_2","red_reverse","red_skip","wild_change_colour","wild_draw_four","yellow_0","yellow_1","yellow_2","yellow_3","yellow_4","yellow_5","yellow_6","yellow_7","yellow_8","yellow_9","yellow_draw_2","yellow_reverse","yellow_skip",]
        ctk.set_appearance_mode("dark")

        self.place_grid()
        self.background_window()
        self.gui_header_section()
        self.gui_main_frame()
        self.display_background_Section()
        self.right_side_section()
    
    def place_grid(self):
        self.gui.grid_columnconfigure(0, weight=1)
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(1, weight=1)
        
    def background_window(self):
        self.bg_frame = ctk.CTkFrame(
            self.gui,
            fg_color=("#0d1117", "#060606")
        )
        self.bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
    def gui_header_section(self):
        """
        This function creates a header section 
        """
        self.header_Frame = ctk.CTkFrame (
            self.gui,
            fg_color= "transparent"
        )
        self.header_Frame.grid(row=0,column=0,columnspan=2,sticky="ew")
        
        
        self.bar = ctk.CTkFrame(
            self.header_Frame,
            height=4,
            fg_color=("#3a7ebf", "#1f538d")
        )
        self.bar.pack(fill="x", pady=(0, 15))
        
        self.header = ctk.CTkLabel(
            self.header_Frame,
            text="UNO Card Detector",
            font=ctk.CTkFont(family="Montserrat", size=32, weight="bold"),
            text_color=("#ffffff")
        )
        self.header.pack(pady=(0, 5))
    
    def gui_main_frame(self):
        """
        This function creates a background frame 
        """
        self.main_frame = ctk.CTkFrame(
            self.gui,
            fg_color=("#1e293b"),
            corner_radius=25,
            border_color=("#2d3748")
        )
        self.main_frame.grid(
            row=1, 
            column=0, 
            columnspan=2,
            padx=35,
            pady=30,
            sticky="nsew")
        
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.rowconfigure(0, weight=1)
    
    def display_background_Section(self):
        """
        This function call all the function for the right side
        """
        
        self.display_bg_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=("#161e2e"),
            corner_radius=15,
            border_width=2,
            border_color=("#2d3748", "#1e293b"),
        )
        self.display_bg_frame.grid(
            row=0, 
            column=0,   
            padx=27,
            pady=27, 
            sticky="nsew")

        self.camera_bg_frame = ctk.CTkFrame(
            self.display_bg_frame,
            corner_radius=12,
            border_width=2,
            border_color=("#3b82f6", "#2563eb"),
            fg_color=("#0f172a", "#020617")
        )
        self.camera_bg_frame.pack(
                            expand=True,
                            fill="both",
                            padx=27,
                            pady=27,
                            )
        
        self.camera_label = ctk.CTkLabel(
            self.camera_bg_frame,
            font=ctk.CTkFont(family="Montserrat", size=16),
            text_color=("#94a3b8", "#94a3b8"),
            text="Camera/Image Display"
        )
        self.camera_label.pack(expand=True)
        
    
    def right_side_section(self):
        """
        This function call all the function for the right side
        """
        self.right_side_frame()
        self.result_display_frame()
        self.result_textbox()
        self.button_Section()
        self.status_section()
        
        
    def right_side_frame(self):
        """
        This function a frame on the right side
        """
        self.right_side_bg_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=("#161e2e"),
            corner_radius=15,
            border_color=("#2d3748")
        )
        self.right_side_bg_frame.grid(
            row=0, 
            column=1, 
            padx=27,
            pady=27,
            sticky="nsew")
    
    def result_display_frame(self): 
        """
        This function create status section,status,label
        """   
        self.display_result_frame = ctk.CTkFrame(
            self.right_side_bg_frame,
            fg_color=("#0f172a", "#020617"),
            corner_radius=15,
            border_color=("#2d3748")
        )
        
        self.display_result_frame.pack(
            fill="x",
            padx="21",
            pady="21"
        )
        self.result_title_label = ctk.CTkLabel(
            self.display_result_frame,
            font=ctk.CTkFont(family="Montserrat", size=24),
            text="Detection Results",
            text_color=("#3b82f6")   
        )
        self.result_title_label.pack(pady=(10,16))
    
    def result_textbox(self):
        """
        This function display result in textbox
        """
        self.display_result_information = ctk.CTkTextbox(
            self.display_result_frame,
            corner_radius=11,
            fg_color=("#1e293b"),
            border_color=("#2d3748"),
            font=ctk.CTkFont(family="Montserrat", size=16),
            width=306,
            height=210,
            text_color=("#e2e8f0")
        )
        
        self.display_result_information.pack(
            padx=22,
            pady=(22,22),
            fill="x"
        )
        
        self.display_result_information.insert(
            ctk.INSERT,
            "Card Details:\nNo card detected"
        )
        
        # self.display_result_information.configure(state="disabled")
    
    def button_Section(self):
        """
        This function create buttons for file & camera
        """
        
        self.buttons_frame =  ctk.CTkFrame(
            self.right_side_bg_frame,
            fg_color="transparent"
        )
        self.buttons_frame.pack(fill="x", padx=22, pady=22)

        self.button_camera = ctk.CTkButton(
            self.buttons_frame,
            corner_radius=11,
            fg_color=("#3b82f6", "#2563eb"),
            font=ctk.CTkFont(family="Montserrat", size=16),
            width=400,
            height=52,
            text="Start Camera",
            command=self.press_camera_button
        )
        
        self.button_camera.pack(pady=(22,22))
        
        self.button_file = ctk.CTkButton(
            self.buttons_frame,
            corner_radius=11,
            fg_color=("#3b82f6", "#2563eb"),
            font=ctk.CTkFont(family="Montserrat", size=16),
            width=400,
            height=52,
            text="Start File",
            command=self.open_file
        )
        
        self.button_file.pack(pady=(0,22))
        
    def status_section(self):
        """
        This function create status section
        """
        self.current_status_frame = ctk.CTkFrame(
            self.right_side_bg_frame,
            corner_radius=11,
            fg_color=("#0f172a"),
            border_width=2,
            border_color=("#2d3748", "#1e293b"),
        )
        
        self.current_status_frame.pack(padx=20, pady=(0, 22), fill="x")
        
        self.current_status = ctk.CTkLabel(
            self.current_status_frame,
            text="●",
            font=ctk.CTkFont(family="Montserrat", size=24),
            fg_color=("#0f172a"),
            text_color="#10b981"
        )
        
        self.current_status.pack(pady=16, padx=(21,6), side="left")
        
        self.current_status_label = ctk.CTkLabel(
            self.current_status_frame,
            text="System Ready",
            font=ctk.CTkFont(family="Montserrat", size=16),
            text_color=("#94a3b8", "#94a3b8"),
        )
        
        self.current_status_label.pack(pady=16, side="left")

        
    def modify_status(self, text, color="#10b981"):
        """
        This function modify the current status
        """
        self.current_status.configure(text_color=color)
        self.current_status_label.configure(text=text)
    
    def press_camera_button(self):
        """
        This called one of the these below fucntion
        """
        if not self.camera_on:
            self.open_camera()
        else:
            self.close_camera()
    
    def open_camera(self):
        """
        This fucntion turn on the camera and modify the status 
        """
        self.cap = cv2.VideoCapture(1)
        if self.cap.isOpened():
            self.camera_on = True
            self.button_camera.configure(
                text="Stop Camera",
                fg_color=("#ef4444", "#dc2626"),
            )
            self.modify_status("Camera is ON", "#3b82f6")
            self.modify_camera()

    def close_camera(self):
        """
        This function is used to stop the camera and modify the status
        """
        self.camera_on = False
        if self.cap:
            self.cap.release()
        self.button_camera.configure(
            text="Start Camera",
            fg_color=("#3b82f6", "#2563eb"),
        )
        self.modify_status("Camera is OFF", "#ef4444")
        self.camera_label.configure(text="Camera / Image Display")
    
    def modify_camera(self):
        if self.camera_on:
            self.detect_card(None)
            rect, frame = self.cap.read()
            if rect:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(frame)
                output_width = 950
                output_height = int(output_width * pil_image.height / pil_image.width)
                
                pil_image = pil_image.resize((output_width, output_height))
                
                self.camera_image = ctk.CTkImage(
                    size=(output_width, output_height),
                    light_image=pil_image,
                    dark_image=pil_image
                )
                
                self.camera_label.configure(image=self.camera_image, text="")
            self.gui.after(4, self.modify_camera)


    def detect_card(self, file):
        """
        This function is used to detect the card
        """

        if self.camera_on:
            rect, frame = self.cap.read()
            
            if not rect:
                self.display_result_information.insert(ctk.INSERT,
                                                       "An error occurred while capturing the frame")
                return
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img_array = cv2.resize(frame, (self.img_height, self.img_width))

            img_array = np.expand_dims(img_array, axis=0)

            img_array = img_array.astype("float32") / 255.0

            predictions = self.model.predict(img_array)
            
            predicted_class = np.argmax(predictions, axis=1)

            self.display_result_information.insert(ctk.INSERT,f"\nP: {self.class_names[predicted_class[0]]}")


            self.display_result_information.see(ctk.END)
        

        elif file:
            tf_image = tf.keras.preprocessing.image.load_img(file, target_size=(self.img_height, self.img_width))
            img_array = img_to_array(tf_image)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0
            predictions = self.model.predict(img_array)
            predicted_class = np.argmax(predictions, axis=1)
            
            self.display_result_information.insert(ctk.INSERT,f"\nP: {self.class_names[predicted_class[0]]}")
            self.display_result_information.see(ctk.END)

        else:
            self.display_result_information.insert(ctk.INSERT, "No card detected\n")
            self.display_result_information.see(ctk.END)

        return




    def open_file(self):
        print("open_file called")
        # existing code
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if file_path:
            pil_image = Image.open(file_path)
            output_width = 500  
            output_height = int(output_width * pil_image.height / pil_image.width)
            
            
            pil_image = pil_image.resize((output_width, output_height))
            
            self.camera_image = ctk.CTkImage(
                size=(output_width, output_height),
                light_image=pil_image,
                dark_image=pil_image
            )
            
            self.camera_label.configure(image=self.camera_image, text="")
            
            self.modify_status(f"Loaded: {os.path.basename(file_path)}","#eab308")
            
            if self.camera_on:
                self.close_camera()

            self.detect_card(file_path)
        
        return

    def run (self):
        self.gui.mainloop()
        
if __name__ == "__main__":
    gui = UNOGui()
    gui.run()