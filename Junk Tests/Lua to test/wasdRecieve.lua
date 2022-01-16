modem = peripheral.wrap("right")
modem.open(1)
while true do
    event, modemSide, senderChannel,
    replyChannel, message, senderDistance = os.pullEvent("modem_message")
    if message == 1 then
        turtle.forward() 
    elseif message == 2 then
        turtle.turnLeft()
        turtle.forward()
        turtle.turnRight()
    elseif message == 3 then
        turtle.turnLeft()
        turtle.turnLeft()
        turtle.forward()
        turtle.turnLeft()
        turtle.turnLeft()
    elseif message == 4 then
        turtle.turnRight()
        turtle.forward()
        turtle.turnLeft()
    elseif message == 5 then
        turtle.turnRight()
    elseif message == 6 then
        turtle.turnLeft()
    end
end
