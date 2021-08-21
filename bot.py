import vonage

client = vonage.Client(key="", secret="")
sms = vonage.Sms(client)

sender = "Kebabiste"
message = "Vends kebab 15 euros sauce algérienne."

numList = open("num.txt", "r")
lines = numList.readlines()

cout = 0
for line in lines:
    cout += 1
    phone = line.replace("0", "+33", 1)

    responseData = sms.send_message({
            "from": sender,
            "to": phone,
            "text": message,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print(f"Message sent successfully to {phone}.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
