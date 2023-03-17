public class BurgerStand{
    private String burgerStand_id;
    private int soldBurger;
    private static int totalBurgerSold = 0;

    public static int getTotalBurger(){
        return totalBurgerSold;
    }
    public BurgerStand(){
        this.burgerStand_id = "Unassigned";
        this.soldBurger = 0;
    }
    public BurgerStand(String bsID, int soldBurger){
        this.burgerStand_id = bsID;
        this.soldBurger = soldBurger;
        totalBurgerSold += this.soldBurger;
    }

    public void justSold(){
        this.soldBurger+=1;
        totalBurgerSold +=1;
    }

    public void setStandID(String ID){
        this.burgerStand_id = ID;
    }

    public String getStandID(){
        return this.burgerStand_id;
    }
    public int getSoldBurger(){
        return this.soldBurger;
    }
}