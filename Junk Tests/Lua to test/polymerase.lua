--
-- Created by IntelliJ IDEA.
-- User: nwlla
-- Date: 4/20/2021
-- Time: 12:21 PM
-- To change this template use File | Settings | File Templates.
--

os.loadAPI("shape.lua")

function complete()
    local success, data = turtle.inspectDown()
    material = string.sub(data.name,11)
    if material == "red_concrete" then material = "yellow_concrete"
    elseif material == "yellow_concrete" then material = "red_concrete"
    elseif material == "lime_concrete" then material = "blue_concrete"
    elseif material == "blue_concrete" then material = "lime_concrete"
    else print("unexpected material")
    end

    turtle.turnRight()
    turtle.forward()
    shape.line(3,material)
    turtle.turnRight()
    turtle.turnRight()
    for x = 1, 3 do
        turtle.forward()
    end
    turtle.turnRight()
end

while(turtle.detectDown()) do
    complete()
    turtle.forward()
    turtle.forward()
end

