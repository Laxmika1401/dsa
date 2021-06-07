// https://leetcode.com/problems/richest-customer-wealth/
/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    let maxWealth=-1;
    for(let i=0;i<accounts.length;i++){
        let currentCustomer=0;
        for(let j=0;j<accounts[i].length;j++){
            currentCustomer+=accounts[i][j]
            
        }
        if(currentCustomer>maxWealth){
            maxWealth=currentCustomer;
            
        }
   
        
    }
     return maxWealth;
    
    
};