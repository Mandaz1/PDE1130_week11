#this file includes the pc parts lists and tier function


#All the different PC specs are arranged in arrays below for ease of access when configuring the PCs
cpu = ["i3 13100f" ,"i5 13400f" , "i5 13600k" , "i7 13700k" , "i9 13900k"]
gpu = ["rtx 3050" , "rtx 4060" , "rtx 4070" , "rtx 4080" , "rtx 4090"]
ram = ["8gb" , "16gb" , "32gb" , "64gb" , "128gb"]
motherboard = ["H610" , "B760" , "Z690" , "Z790"]
cpu_cooling = ["stock" , "Air cooling" , "240 aio" , "360 aio" ]
storage = ["500gb ssd" , "1tb ssd" , "2tb ssd" , "8tb ssd"]
psu = ["550w" , "650w" , "750w" , "850w" , "1000w"]
prices = [ "500" , "750" , "1000" , "2000" ]
tier = 0 #tier is the price range level, its takes the index value for the prices list and uses it to determine the pc parts 0 for <500 , 1 for 750, 2 for 1000, 3 for 2000. 


# the function below determines the tier based on the price range
def tier_function(price_range):#it takes the value price_range then decides what tier it is, finally it returns the tier value
    if (price_range==500):
        tier = 0 #tier is the price range level, its takes the index value for the prices list and uses it to determine the pc parts 0 for <500 , 1 for 750, 2 for 1000, 3 for 2000.
    elif (price_range==750):
        tier = 1
    elif (price_range==1000):
        tier = 2
    elif (price_range>1000):
        tier = 3
    return tier