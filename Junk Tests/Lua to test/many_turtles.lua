modem = peripheral.wrap("right")
modem.open(1)
event, modemSide, senderChannel, replyChannel,
    message, senderDistance = os.pullEvent("modem_message")

for i = 1, message do
    turtle.forward()
end
 
