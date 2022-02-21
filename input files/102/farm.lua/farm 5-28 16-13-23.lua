turtle.up()
size=9
for i=1, size do
    for i=1, size do
        turtle.digDown()
        turtle.placeDown()
        turtle.forward()
    end
    turtle.turnRight()
    turtle.turnRight()
    for i=1, size do
        turtle.forward()
    end
    turtle.turnLeft()
    turtle.forward()
    turtle.turnLeft()
end
