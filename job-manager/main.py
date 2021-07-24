from tkinter import *
from tkinter import messagebox
import csv

# ---------------------------- SAVE JOBS ------------------------------- #
def save():
    job_data = job_input.get()
    company_data = company_input.get()
    interview_data = interview_input.get()
    if len(job_data) == 0 or len(company_data) == 0 or len(interview_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=job_data, message=f"There are details entered: \nCompany: {company_data}\n"
                                                               f"Interview: {interview_data}\n Is it ok to save?")
        if is_ok:
            try:
                with open("job_applied_data.csv") as file:
                    csv.reader(file)
            except FileNotFoundError:
                with open("job_applied_data.csv", mode="a") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Job Title", "Company", "Interview"])
                    writer.writerow([job_data, company_data, interview_data])
            else:
                with open("job_applied_data.csv", mode="a") as file:
                    csv.writer(file).writerow([job_data, company_data, interview_data])

            job_input.delete(0, END)
            company_input.delete(0, END)
            interview_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Job Applied Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=256, height=256)
job_icon = PhotoImage(file="job.png")
canvas.create_image(128, 128, image=job_icon)
canvas.grid(column=0, row=0, columnspan=2)

# label
job_label = Label(text="Job Title:")
job_label.grid(column=0, row=1)

company = Label(text="Company:")
company.grid(column=0, row=2)

Interview = Label(text="Interview:")
Interview.grid(column=0, row=3)

# entry
job_input = Entry(width=35)
job_input.grid(column=1, row=1)
job_input.focus()

company_input = Entry(width=35)
company_input.grid(column=1, row=2)

interview_input = Entry(width=35)
interview_input.grid(column=1, row=3)

# button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

