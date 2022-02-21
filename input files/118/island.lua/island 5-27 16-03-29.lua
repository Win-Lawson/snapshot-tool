height= 1
while not turtle.compareDown(1) do

    turtle.down()
    turtle.digDown()
    height= height+1
end

for i=1, height do
    turtle.up()
end

