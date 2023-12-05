#this file includes functions related to the beginner level in miniproject 1

from specs_configurator import * #imports the list and tier function which will be used in this program

# the function below gives out the appropriate specs based on price range and use case(gaming)
def pc_specs_g(tier):#this function uses the same tier value used in the tier_function and then makes a build based on it
    print("You have chosen Gaming as your use case, as such the GPU would be the priority because it is the main component used in rendering games and its directly related to your PCs gaming performance")
    print("the appropriate PC specs for your use case are:")
    print("CPU: " + cpu[tier],"GPU: " + gpu[tier+1],"RAM: " + ram[tier],"Motherboard: " + motherboard[tier],"CPU cooling: " + cpu_cooling[tier],"storage: " + storage[tier],"PSU: " + psu[tier],sep='\n')
    return

#the function below gives out the appropriate specs based on price range and use case(pro work)
def pc_specs_p(tier):
    print("You have chosen Professional work as your use case, as such the CPU and Memory would be the priority Because those components directly affect your computers performance in professional workloads")
    print("the appropriate PC specs for your use case are:")
    if tier == 0: #if the tier is 0 meaning that the price is 500dollars, then there will be no GPU and the cpu and ram will be prioritized
        print("CPU: " + cpu[tier+1],"RAM: " + ram[tier+1],"Motherboard: " + motherboard[tier],"CPU cooling: " + cpu_cooling[tier],"storage: " + storage[tier],"PSU: " + psu[tier],sep='\n')
        print("these are the current recomended specs to match your budget, the total price is around", price_range, "dollars")
    else:# else if the tier is greater than 0, meaning the price is more than 500, a GPU would be added but reduced by 1 tier, while the cpu and ram will be prioritized
        print("CPU: " + cpu[tier+1],"GPU: " + gpu[tier-1],"RAM: " + ram[tier+1],"Motherboard: " + motherboard[tier],"CPU cooling: " + cpu_cooling[tier],"storage: " + storage[tier],"PSU: " + psu[tier],sep='\n')
    return


