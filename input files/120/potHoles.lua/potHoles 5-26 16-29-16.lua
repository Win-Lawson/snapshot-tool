
for i=1, 20, 1 do
    turtle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
    else
        turtle.select(2) 
        turtle.placeUp()
    end
    turtle.select(1)
end
