import java.util.Scanner;

public class MainBurgerStand {
    private static void Menu() {
        System.out.println("::Menu::");
        System.out.println("1. Cheese Burger");
        System.out.println("2. Chicken Burger");
        System.out.println("3. Beef Burger");
        System.out.println("4. Special Chicken Burger");
        System.out.println("5. Special Beef Burger");
        System.out.println("6. Double Beef Burger");
        System.out.println("7. Double Chicken Burger");

    }

    private static boolean StandSystem(BurgerStand OperatingBS, Scanner input) {
        int BSoperation, burgerChoice;
        
        // Scanner input = new Scanner(System.in);
        System.out.println("Burger Stand " + OperatingBS.getStandID());
        System.out.println("1. Display Burger Stand sale");
        System.out.println("2. Add Sale");
        System.out.println("3. Change Burger Stand ID");
        System.out.print("Input: ");
        BSoperation = input.nextInt();
        if (BSoperation == 1) {
            System.out.println(
                    "Burger Stand " + OperatingBS.getStandID() + " sale is " + OperatingBS.getSoldBurger()
                            + " burgers.");
            return false;
        }
        else if (BSoperation == 2) {
            do {
                Menu();
                System.out.println("Press 0 to stop adding sale");
                System.out.print("Pick burger of your choice: ");
                burgerChoice = input.nextInt();
                if (0 < burgerChoice && burgerChoice < 8)
                    OperatingBS.justSold();

            } while (burgerChoice > 0);
            return false;
        } 
        else if(BSoperation == 3){
            String newStandID;
            System.out.println("Current Burger Stand ID: "+OperatingBS.getStandID());
            System.out.print("Enter new Burger Stand ID you would like to assign: BS00");
            newStandID = input.next();
            newStandID = "BS00"+newStandID;
            OperatingBS.setStandID(newStandID);
            return true;
        }
        else
            return true;
    }

    public static void main(String[] args) {
        BurgerStand standOne = new BurgerStand("BS001", 0);
        BurgerStand standTwo = new BurgerStand("BS002", 10);
        BurgerStand standThree = new BurgerStand("BS003", 20);

        int choice;
        BurgerStand OperatingBS = null;
        Scanner input = new Scanner(System.in);
        boolean exist = true, exitBS = true;
        String bsID;
        do {
            System.out.println("::Welcome to Main Burger Stand System::");
            System.out.println("1. Display total burgers sold by all Stand");
            System.out.println("2. Access a Burger Stand system");
            System.out.println("0. Exit the program");
            System.out.print("What operation do you want to do? ");
            choice = input.nextInt();
            if (choice == 1) {
                System.out.println("Total burger sold by all burger Stands for today is: "
                        + BurgerStand.getTotalBurger() + "\n\n");
            } else if (choice == 2) {
                System.out.print("Please insert your Burger Stand ID(BS00X): BS");
                bsID = input.next();
                bsID = "BS"+bsID;
                switch (bsID) {
                    case "BS001":
                        OperatingBS = standOne;
                        exitBS = false;
                        break;
                    case "BS002":
                        OperatingBS = standTwo;
                        exitBS = false;
                        break;
                    case "BS003":
                        OperatingBS = standThree;
                        exitBS = false;
                        break;
                    default:
                        System.out.println("The Burger Stand ID " + bsID + " does not exist in the record.");
                        exist = false;
                }
                while (exist && !exitBS) {
                    exitBS = StandSystem(OperatingBS, input);
                }
            }
        } while (choice > 0);

        input.close();
    }

}
