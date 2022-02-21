ran = 1
function basicFor()
    turtle.forward()
    turtle.placeDown()
    ran = math.random(2, 4)
    for a=1, ran do
        turtle.forward()
    end
    turtle.placeDown()
    ran = math.random(3, 4)
    for b=1, ran do
        turtle.forward()
    end
    turtle.placeDown()
end

function basicUp()
    turtle.forward()
    turtle.placeDown()
    turtle.up()
    ran = math.random(3, 4)
    for c=1, ran do
        turtle.forward()
    end
    turtle.placeDown()
end

function basicDown()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.down()
    for d=1, 5 do
        turtle.forward()
    end
    turtle.placeDown()
    turtle.back()
    turtle.select(2)
    turtle.placeDown()
    turtle.select(1)
    turtle.forward()
end

function basicAround()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.up()
    turtle.placeDown()
    turtle.up()
    turtle.placeDown()
    turtle.forward()
    turtle.down()
    turtle.down()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
end

function ladderClimb()
    turtle.forward()
    turtle.forward()
    turtle.forward()
    turtle.up()
    turtle.placeDown()
    turtle.back()
    turtle.select(2)
    turtle.placeDown()
    turtle.select(1)
    turtle.forward()
    turtle.up()
    turtle.placeDown()
    turtle.turnLeft()
    turtle.forward()
    turtle.select(2)
    turtle.placeDown()
    turtle.select(1)
    turtle.back()
    turtle.turnRight()
    turtle.up()
    turtle.placeDown()
    turtle.forward()
    turtle.select(2)
    turtle.placeDown()
    turtle.select(1)
    turtle.back()
    turtle.up()
    turtle.placeDown()
    for e=1, 4 do
        turtle.forward()
    end
    turtle.up()
    turtle.placeDown()
end

function basicBar()
    turtle.forward()
    turtle.select(4)
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    ran = math.random(3,4)
    for f=1, ran do
        turtle.forward()
    end
    turtle.placeDown()
    for f=1, ran do
        turtle.forward()
    end
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.select(1)
    turtle.forward()
    turtle.placeDown()
end

function barWalk()
    turtle.select(4)
    ran = math.random(4,5)
    for f=1, ran do
        turtle.forward()
        turtle.placeDown()
    end
    turtle.turnRight()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.turnLeft()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.forward()
    turtle.forward()
    if ran==4 then
        turtle.forward()
    end
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.turnLeft()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.placeDown()
    turtle.turnRight()
    turtle.forward()
    turtle.placeDown()
    turtle.forward()
    turtle.select(1)
    turtle.placeDown()
end
