turtle.up()

function forward_x(x)
    for i=1, x-1 do
        turtle.placeDown()
        turtle.forward()
    end
end
forward_x(7)
turtle.turnLeft()
forward_x(6)
turtle.turnLeft()
forward_x(7)

turtle.placeDown()
