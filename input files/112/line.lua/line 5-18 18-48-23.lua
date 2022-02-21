x=8
turtle.up()
for i=1,x do
    for i=1, x do
        turtle.placeDown()
        turtle.forward()  
    end
    turtle.turnRight() 
    x=x-1 
end    
     
