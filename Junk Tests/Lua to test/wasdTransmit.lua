modem = peripheral.wrap("right")
while true do
    event, key, bool = os.pullEvent("key")
    if key == 87 then --w
        modem.transmit(1,2,1)
    elseif key == 65 then --a  
        modem.transmit(1,2,2)  
    elseif key == 83 then --s 
        modem.transmit(1,2,3)
    elseif key == 68 then --d 
        modem.transmit(1,2,4)
    elseif key == 262 then --arrow right
        modem.transmit(1,2,5)
    elseif key == 263 then --arrow left
        modem.transmit(1,2,6)
    end
end
