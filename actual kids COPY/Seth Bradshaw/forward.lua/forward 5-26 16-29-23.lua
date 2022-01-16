for i=1, 11 do
    turtle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
    end
    end
