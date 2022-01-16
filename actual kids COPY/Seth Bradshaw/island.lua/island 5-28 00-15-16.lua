height= 1
while turtle.compareDown() do

    turtle.digDown()
    turtle.down()
    height= height+1
end

for i=1, height do
    turtle.up()
end

