i=1

while i <10 do 
    turtle.forward()
    if turtle.detect() then
        turtle.turnRight()
    end
    i=i+1
end
