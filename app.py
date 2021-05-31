from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/msg", methods=["POST"])

def main():

    msg = request.form.get('Body')

    try:

        if int(msg) in range(1, 17):
            useroutput= {
                1: "Lecture Time Table\n https://drive.google.com/file/d/17zqFTseiq5lLJxePfXqpPCzHIkiXloZz/view?usp=drivesdk",
                2: "exam time table has not come yet",


                3: "Lectures Links\n1.Computer Programming:\nhttps://teams.microsoft.com/l/meetup-join/19:meeting_MzQ4OGQ5ZGYtNDgyNi00ODkxLTllMGItNjc3M2VkYTNhMzQ2@thread.v2/0?context=%7B%22Tid%22:%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22,%22Oid%22:%22146aabe7-f82a-4e86-b3db-c9a1b8175d61%22%7D\n2.Engineering Mathematics 2:\nhttps://teams.microsoft.com/l/meetup-join/19%3ameeting_NGVkYTFiNDMtN2JmNi00NDJmLWJmZmUtOWE5YzM1YTZjOGMz%40thread.v2/0?context=%7b%22Tid%22%3a%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2c%22Oid%22%3a%2208354639-3c00-4621-89da-732097c9983a%22%7d\n3.Engineering Graphics:\nhttps://teams.microsoft.com/l/meetup-join/19%3ameeting_YmEwMjBhNzAtNDAyYy00MGYxLWEwOTAtMTI3YzMwNDY2OGNm%40thread.v2/0?context=%7b%22Tid%22%3a%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2c%22Oid%22%3a%2222d3e36b-a884-4d1e-9fa9-003a9f05aeeb%22%7d\n4.Engieering Chemistry 2:\nhttps://teams.microsoft.com/l/meetup-join/19%3ameeting_ODk5NDU1ZjItODJhMi00MTJhLThkOTQtMzFiNWY4ZWU2MmYx%40thread.v2/0?context=%7b%22Tid%22%3a%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2c%22Oid%22%3a%22941edb8b-470a-4841-b162-cb26e9f7a96f%22%7d\n5.Engineering Physics 2:\nhttps://teams.microsoft.com/l/meetup-join/19%3Ameeting_ZjhmOGUxMWMtMTcwZC00OTMyLWExNmItMGM2M2E2NDQ0NjU4%40thread.v2/0?context=%7B%22Tid%22%3A%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2C%22Oid%22%3A%227700c105-50c1-4503-ba58-0d3ed52cce3e%22%2C%22MessageId%22%3A%220%22%7D",

                4: "Lab Links \n1.AUTOCAD Link:\nhttps://teams.microsoft.com/l/meetup-join/19%3ameeting_OTdjYzMyZmItMzQ2OC00YmJlLTkxZjctNGE0NGNlZjA5OWY5%40thread.v2/0?context=%7b%22Tid%22%3a%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2c%22Oid%22%3a%2270e5edcc-b299-4be9-b5fb-9077d3edb592%22%7d\n2.Engieering Chemistry 2:\nhttps://teams.microsoft.com/l/meetup-join/19%3ameeting_ODk5NDU1ZjItODJhMi00MTJhLThkOTQtMzFiNWY4ZWU2MmYx%40thread.v2/0?context=%7b%22Tid%22%3a%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2c%22Oid%22%3a%22941edb8b-470a-4841-b162-cb26e9f7a96f%22%7d\n3.Engineering Physics 2:\nhttps://teams.microsoft.com/l/meetup-join/19%3Ameeting_ZjhmOGUxMWMtMTcwZC00OTMyLWExNmItMGM2M2E2NDQ0NjU4%40thread.v2/0?context=%7B%22Tid%22%3A%22405ddc34-d660-46e5-b52d-bfd0be156bb5%22%2C%22Oid%22%3A%227700c105-50c1-4503-ba58-0d3ed52cce3e%22%2C%22MessageId%22%3A%220%22%7D",

                5: "Assingment Submission links\n1.Physics Assingment \nhttps://siescms-my.sharepoint.com/:f:/g/personal/hodfe_sies_edu_in/Ekr38KwRwRVClQlbT_t_3s0BaIgiLPDiTmf39txPFN7amg?e=DbRHBu",

                6: "Practicle Submission Links\n1.Physics Practicle\nhttps://siescms-my.sharepoint.com/:f:/g/personal/hodfe_sies_edu_in/EkWVdLT4HiVApOgIRpXxUS0B_h0eHhT608fMBBVaBvq_vQ?e=edJXTD",

                7: "Textbook & Refrencebook\n1.C Programming\nhttps://drive.google.com/folderview?id=1XF1fLe0pLZN9fEYcVSsAMYZzVuno4Fjz\n2.Engineering Chemistry 2\nhttps://drive.google.com/folderview?id=1XB7IiPVgN-rtC4q35pH0W3oTqLBM6kDr\n3.Engineering Graphics\nhttps://drive.google.com/folderview?id=1XDT0iCNqWg8KR1tS6zNMG03jxD4TgJYK\n4.Engineering Mathematics 2\nhttps://drive.google.com/folderview?id=1X4pOHpcr1yCX7-mn-p32Jb6YatJfQkvC\n5.Engineering Physics\nhttps://drive.google.com/folderview?id=1XCCYnuALCSBpITLoy_AT5R07Yd1ZhcN4\n6.Professional Comunication and Etichs\nhttps://drive.google.com/folderview?id=1XFGh2ZqfhI1yvQVp3g8kmWMkqzx90hkR",

                8: "Juno Portal\nhttps://play.google.com/store/apps/details?id=com.gems",

                9: "Past Year Questions Paper\nhttps://muquestionpapers.com/solutions/be/first-year-engineering/semester-2",

                10: "Youtube Channel\n1.Vijya Maam (Maths Virtuoso)\nhttps://youtube.com/channel/UCUTRnhWrpfNynNKNAsjoosw\n2.Manasi Karkare\nhttps://youtube.com/channel/UCE8rBKRzHTWOjfChRjgZdXQ",

                11: "College Website\nhttps://siesedu.in/login.htm",

                12: "Viva Question\nhttps://drive.google.com/folderview?id=1bowPfuyalEreQPyl3A6ZXhzkjimzbD9a",

                13: "virtual lab link\nhttps://vlab.amrita.edu/\n1.Diffraction Physics Parcticle 1\nhttps://vlab.amrita.edu/?sub=1&brch=281&sim=334&cnt=3",

                14: "Microsoft Teams:\nhttps://www.microsoft.com/en-in/campaign/small-and-medium-business/Teams.aspx?utm_source=search&utm_medium=cpc&utm_campaign=microsoft_teams_brand&utm_term=teams&utm_content=responsive_text_ads&gclid=CjwKCAjwy42FBhB2EiwAJY0yQpsCRFuDHua_uPXMCIzeKnG8d0Z57a9zeUxlldLI9vZrDpZvarPDLxoCug8QAvD_BwE",

                15: "Outlook: \nhttps://outlook.live.com/owa/",
                16: "Lab Mauals\n1. Engineering Chemistry2\na.Practicle 1 Corrosion\nhttps://drive.google.com/file/d/17xoOH9qfrjb5yDh4c0qo56XoF0KmqX5O/view?usp=drivesdk\n Practicle 3 emf of cu-zn\nhttps://drive.google.com/file/d/1ChL-L1-NKgCIbFBgLwEyzYmGM5ku2jx-/view?usp=drivesdk\n2. Engineering Graphics\na.Component 2\nhttps://siescms-my.sharepoint.com/:b:/g/personal/onkarp_sies_edu_in/EasO8R70OxdGi4UI7jcPMgMBryfJ7K4oWt1mGKZ4G6WDrQ\nb.Component 1\nhttps://siescms-my.sharepoint.com/:b:/g/personal/onkarp_sies_edu_in/ESR-IRy4159Np2BteVbbo_MBluRusiXsh6huUmYFLqV1Lw",
            }

            main_msg_output = MessagingResponse()
            main_msg_output.message(useroutput.get(int(msg),"Invalid Option"))
            return str(main_msg_output)
        
    except:

        intromsg = '''Hey  there, welcome to the LifeLine Bot for FE's.Created by the Moiz&Salman.
    Instruction: Well its's a bot so he will only accept the aproppriate command don't say hi hello and all this just type the corressponding Numbers 
        Enter the Following Number to oprate the commands
        1.Lecture Time Table
        2.Exam Time Table
        3.Lectures Links
        4.Lab Links
        5.Assingnment Submission Links
        6.Parcticle Submission Links
        7.Textbooks & Refrence book
        8.Juno Portal
        9.Past Year Paper
        10. Youtube Channel
        11. College Website
        12.Viva Questions
        13.Virtual Lab
        14.Microsoft Teams
        15.Outlook
        16.Lab Manuals'''
        main_msg = MessagingResponse()
        main_msg.message(intromsg)
        return str(main_msg)


if __name__ == "__main__":
 app.run()
