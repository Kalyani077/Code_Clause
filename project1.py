import sounddevice as sd
import soundfile as sf
import tkinter as tk
from tkinter import messagebox
import os

class AudioRecorder:
    def __init__(self):
        self.frames = []
        self.samplerate = 44100
        self.filename = 'audio.wav'
        self.recording = False

    def start_recording(self):
        self.frames = []
        self.recording = True
        messagebox.showinfo("Recording", "Recording started...")

    def stop_recording(self):
        if self.recording:
            self.recording = False
            sd.stop()
            messagebox.showinfo("Recording", "Recording stopped.")
            self.save_file()

    def save_file(self):
        if self.frames:
            sf.write(self.filename, self.frames, self.samplerate)
            messagebox.showinfo("Recording", f"Recording saved as {self.filename}")
        else:
            messagebox.showerror("Recording", "No audio recorded.")

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.frames.extend(indata)

    def run(self):
        root = tk.Tk()
        root.title("Audio Recorder")

        start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        start_button.pack()

        stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording)
        stop_button.pack()

        save_button = tk.Button(root, text="Save Recording", command=self.save_file)
        save_button.pack()

        root.mainloop()

if __name__ == "__main__":
    recorder = AudioRecorder()
    with sd.InputStream(callback=recorder.callback):
        recorder.run()

