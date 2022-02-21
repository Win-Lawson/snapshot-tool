invintoryslot=1

for i=1, 18, 1 do
    turtle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
        invintoryslot = invitoryslot+1
        turtle.select(invintorySlot)
    else
        turtle.placeUp() 
    end
    
end
