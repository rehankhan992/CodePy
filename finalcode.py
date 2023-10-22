try:
    import pandas as pd
    import xlsxwriter
    from tkinter import Tk, Canvas, Button
    from datetime import datetime
    from random import choice
except:
    print("Please install Required Packages:  Pandas,xlsxwriter,tkinter,datetime,random")

df = pd.DataFrame({'TITLE': [], 'DESCRIPTION': [], 'DATE': [], 'TIME': []})
writer = pd.ExcelWriter('Report1.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

nor = int(input(" Enter the number of reminders you want to enter: "))
while nor > 0:
    title1 = input("\nEnter the Title: ")
    Description1 = input("Enter the Description: ")
    Date1 = input("Enter the date (YYYY-MM-DD): ")
    Time1 = input("Enter the time: ")

    reader = pd.read_excel(r'Report1.xlsx')
    df2 = pd.DataFrame({'TITLE': [title1], 'DESCRIPTION': [Description1], 'DATE': [Date1], 'TIME': [Time1]})
    df3 = reader.append(df2)
    writer2 = pd.ExcelWriter('Report1.xlsx', engine='xlsxwriter')
    df3 = df3.sort_values('TIME')
    df3 = df3.sort_values('DATE')
    df3.to_excel(writer2, sheet_name='Sheet1', index=False)
    writer2.save()
    nor = nor - 1


class DisplayMessage:
    def __init__(self, title, time, message):
        self.root = Tk()

        self.colorPrimary = choice(["red", "green", "purple", "blue", "orange", "black"])
        self.colorSecondry = choice(["#cd000e", "#20cc16", "#014242", "#19024a", "#59690c", "#172917", "#FF4500"])
        self.colortertiary = choice(["#cd000e", "#20cc16", "#014242", "#19024a", "#59690c", "#172917", "#FF4500"])

        self.Windowtitle()
        self.Canbox(title, time, message)
        self.root.mainloop()

    def Windowtitle(self):
        self.root.title("NIIT REMINDER PROGRAM")
        self.root.config(background="#defaf4")
        self.root.geometry("600x600")

    def Canbox(self, title, time, message):
        c1 = Canvas(self.root, width="600", height="600", background="#defaf4")
        c1.pack()

        c1.create_text(200, 100, width=800, fill=self.colorPrimary, font=('Helvetica', '30', 'bold'), text=title)

        c1.create_text(200, 150, width=800, fill=self.colorPrimary, font=('Helvetica', '25', 'bold'), text=time)

        c1.create_text(200, 300, width=800, fill=self.colortertiary, font=('Helvetica', '20'), text=message)

        b1 = Button(self.root, text="Dismiss", command=self.root.destroy)
        b1.pack(pady=40)


class RunMessage:
    def __init__(self, i, data):
        Title = data["TITLE"][i]
        Time = data["TIME"][i]
        Message = data["DESCRIPTION"][i]
        DisplayMessage(Title, Time, Message)


class Controllerfn:
    def __init__(self):
        self.ReadExcelFile()
        self.Checkdatetime()

    def ReadExcelFile(self):
        self.data = pd.read_excel("Report1.xlsx")

    def datasep(self, DateStamp, TimeStamp):
        raw_year = DateStamp[0]
        raw_month = DateStamp[1]
        raw_date = DateStamp[2]
        date = raw_year + raw_month + raw_date

        raw_hrs = TimeStamp[0]
        raw_min = TimeStamp[1]
        time = raw_hrs + raw_min

        return (date + time)

    def Checkdatetime(self):
        for i in range(len(self.data)):
            DateStamp = str(self.data["DATE"][i]).split(" ")[0].split("-")
            TimeStamp = str(self.data["TIME"][i]).split(":")

            CurrentDate = str(datetime.now()).split(" ")[0].split("-")
            CurrentTime = str(datetime.now()).split(" ")[1].split(":")

            recordTime = self.datasep(DateStamp, TimeStamp)
            myTime = self.datasep(CurrentDate, CurrentTime)

            if recordTime == myTime:
                RunMessage(i, self.data)

                NewDf = self.data.drop(i)
                NewDf.to_excel("Report1.xlsx", index=False)


while True:
    Controllerfn()
