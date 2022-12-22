from flask import Flask, request

app = Flask(__name__)

@app.route("/submit-report", methods=["POST"])
def submit_report():
  name = request.form["name"]
  email = request.form["email"]
  report = request.form["report"]

  # scrie informatiile din formular intr-un fisier
  with open("reports.txt", "C:\Users\satno\Desktop\BullySite\Raporturi") as f:
    f.write(f"Nume: {name}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Raport:\n{report}\n\n")

  return "Raportul a fost trimis cu succes!"

if __name__ == "__main__":
  app.run()
