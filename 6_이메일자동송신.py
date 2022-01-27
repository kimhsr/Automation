import openpyxl
import smtplib
from email.mime.text import MIMEText  # 편지봉투
from email.mime.base import MIMEBase  # 택배상자
from email.mime.multipart import MIMEMultipart  # 택배 + 편지
from email import encoders
import os

naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
naver_server.login("본인_아이디", "본인_비밀번호")

book = openpyxl.load_workbook("./list.xlsx")
sheet = book.active
num = 0
for row in sheet.rows:
    if row[4].value == "X":
        continue
    date = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = "{} 님, XX 쇼핑몰입니다. ".format(name)
    content = """ 안녕하세요, XX 쇼핑몰에서 결제 완료 안내 메일 보내드립니다.

성함 : {}
구매 날짜 : {}
구매물 건 : {}

감사합니다.
""".format(name, date, product)

    email_content = MIMEMultipart()  # 택배+편지봉투
    email_content["From"] = "이메일"
    email_content["Cc"] = "test@naver.com, test2@naver.com, test3@naver.com"
    email_content["To"] = your_mail
    email_content["Subject"] = title
    msg = MIMEText(content, _charset="euc-kr")
    email_content.attach(msg)

    path = "./list.xlsx"  # 보낼 파일 지정
    file = open(path, "rb")  # read binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=" + os.path.basename(path))
    email_content.attach(part)

    naver_server.sendmail("이메일", your_mail, email_content.as_string())
    print("{}님께 이메일을 보냈습니다.".format(name))
    num += 1
    if num % 20 == 0:
        naver_server.quit()
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
        naver_server.login("본인_아이디", "본인_비밀번호")
